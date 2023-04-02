#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import requests

from helios.core.scripts import *
from helios.core.request import Request
from helios.core.login import LoginAction
from helios.core.crawler import Crawler, WebFinder
from helios.core.utils import uniquinize
from helios.core.database import SQLiteWriter
from helios.core.webapps import WebAppModuleLoader
from helios.ext.mefjus.ghost import Mefjus
from helios.core.scope import Scope
from helios.core import scanner, modules
from helios.ext.libcms.cms_scanner_core import CustomModuleLoader
from helios.ext.metamonster import metamonster

try:
    import urlparse
except ImportError:
    # python 3 imports
    import urllib.parse as urlparse


class Helios:
    logger = None
    crawler_max_urls = 200
    output_file = None
    _max_safe_threads = 25
    thread_count = 10

    proxy_port = 3333
    driver_show = False

    use_proxy = True
    db = None
    scan_cookies = {}
    options = None

    def __init__(self, options):
        self.options = options

    def start(self):
        self.logger = logging.getLogger("Helios")
        self.logger.setLevel(logging.DEBUG if self.options.verbose else logging.INFO)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG if self.options.verbose else logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(ch)
        self.logger.info("Starting Helios")

        try:
            self.thread_count = int(self.options.threads)
        except:
            # None or invalid format
            pass
        if self.thread_count > self._max_safe_threads:
            self.logger.warning("Number of threads %d is too high, defaulting to %d" %
                                (self.thread_count, self._max_safe_threads))
            self.thread_count = self._max_safe_threads
        if not self.options.sslverify:
            requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
            self.logger.info("Disabled SSL verification")

        self.db = SQLiteWriter()
        self.db.open_db(self.options.db)
        self.logger.info("Using SQLite database %s" % self.options.db)

    def run(self, start_urls, scopes=None):
        start_url = start_urls[0]
        self.start()
        start_time = time.time()
        scope = Scope(start_url, options=self.options.scope_options)
        if scopes:
            scope.scopes = [x.strip() for x in scopes.split(',')]
        self.db.start(start_url, scope.host)
        c = None
        s = None
        loader = None

        self.logger.debug("Parsing scan options")
        login = LoginAction(logger=self.logger.getEffectiveLevel())
        pre_run = login.pre_parse(self.options)
        if pre_run:
            self.scan_cookies = dict(login.session_obj.cookies)
        scanoptions = []
        if self.options.custom_options:
            scan_vars = self.options.custom_options.split(',')
            for v in scan_vars:
                opt = v.strip()
                scanoptions.append(opt)
                self.logger.debug("Enabled option %s" % opt)
        if self.options.scanner or self.options.allin:
            s = ScriptEngine(options=scanoptions, logger=self.logger.getEffectiveLevel(), database=self.db)

        if self.options.use_adv_scripts or self.options.allin:
            loader = modules.CustomModuleLoader(options=scanoptions,
                                                logger=self.logger.getEffectiveLevel(),
                                                database=self.db,
                                                scope=scope)

            loader.sslverify = self.options.sslverify
            loader.headers = login.headers
            loader.cookies = self.scan_cookies

        todo = []

        c = Crawler(base_url=start_url, logger=self.logger.getEffectiveLevel())
        for login_header in login.headers:
            c.headers[login_header] = login.headers[login_header]
        if self.options.use_crawler or self.options.allin:
            if pre_run:
                c.login = True
                # set cookies from Login module
                cookies = dict(login.session_obj.cookies)
                if cookies and len(cookies):
                    self.logger.debug("Setting crawler cookies from login module: %s" % str(cookies))
                    c.cookie.append(cookies)
            c.thread_count = self.thread_count
            c.max_urls = int(self.options.maxurls)
            c.scope = scope
            if self.options.user_agent:
                c.headers = {'User-Agent': self.options.user_agent}
            if len(start_urls) != 1:
                for extra_url in start_urls[1:]:
                    c.parse_url(extra_url, extra_url)
            # discovery scripts, pre-run scripts and advanced modules
            if self.options.scanner or self.options.allin:
                self.logger.info("Starting filesystem discovery (pre-crawler)")
                new_links = s.run_fs(start_url)

                for newlink in new_links:
                    c.parse_url(newlink[0], newlink[0])
                if self.options.use_adv_scripts or self.options.allin:
                    self.logger.info("Running custom scripts (pre-crawler)")
                    links = loader.base_crawler(start_url)
                    for link in links:
                        self.logger.debug("Adding link %s from post scripts" % link)
                        c.parse_url(link, link)

            if self.options.wl_file or self.options.allin:
                wf = WebFinder(url=start_url,
                               logger=self.logger.getEffectiveLevel(),
                               word_list=self.options.wl_file,
                               append=self.options.wl_ext,
                               ok_status_codes=self.options.wl_codes,
                               invalid_text=self.options.wl_404,
                               threads=self.thread_count)
                for wf_result in wf.output:
                    c.parse_url(wf_result, start_url)

            self.logger.info("Starting Crawler")
            c.run_scraper()
            self.logger.debug("Cookies set during scan: %s" % (str(c.cookie.cookies)))
            self.scan_cookies = c.cookie.cookies

            self.logger.info("Creating unique link/post data list")
            todo = uniquinize(c.scraped_pages)
        else:
            todo = [[start_url, None]]

        if self.options.driver:
            self.logger.info("Running GhostDriver")

            m = Mefjus(logger=self.logger.getEffectiveLevel(),
                       driver_path=self.options.driver_path,
                       use_proxy=self.options.proxy,
                       proxy_port=self.options.proxy_port,
                       use_https=scope.is_https,
                       show_driver=self.options.show_driver or self.options.interactive)
            results = m.run(todo, interactive=self.options.interactive)
            for res in results:
                if not scope.in_scope(res[0]):
                    self.logger.debug("IGNORE %s.. out-of-scope" % res)
                    continue
                if c.get_filetype(res[0]) in c.blocked_filetypes:
                    self.logger.debug("IGNORE %s.. bad file-type" % res)
                    continue
                if res in c.scraped_pages:
                    self.logger.debug("IGNORE %s.. exists" % res)
                    continue
                else:
                    todo.append(res)
                    self.logger.debug("QUEUE %s" % res)
            self.logger.info("Creating unique link/post data list")
            old_num = len(todo)
            todo = uniquinize(todo)
            self.logger.debug("WebDriver discovered %d more url/post data pairs" % (len(todo) - old_num))

        scanner_obj = None
        if self.options.scanner or self.options.allin:
            self.logger.info("Starting scan sequence")
            if len(todo) < self.thread_count:
                # for performance sake
                self.thread_count = len(todo)
            scanner_obj = scanner.Scanner(logger=self.logger.getEffectiveLevel(),
                                          script_engine=s, thread_count=self.thread_count)
            scanner_obj.copy_engine = self.options.optimize
            for page in todo:
                url, data = page
                req = Request(url, data=data, agent=self.options.user_agent,
                              headers=login.headers, cookies=self.scan_cookies)
                req.run()
                scanner_obj.queue.put(req)
                scanner_obj.logger.debug("Queued %s %s" % (url, data))
            scanner_obj.run()

        post_results = []
        if self.options.use_adv_scripts or self.options.allin:
            self.logger.info("Running post scripts")
            post_results = loader.run_post(todo, cookies=self.scan_cookies)
        cms_results = None
        if self.options.cms_enabled or self.options.allin:
            cms_loader = CustomModuleLoader(log_level=self.logger.getEffectiveLevel())
            cms_results = cms_loader.run_scripts(start_url)
            if cms_results:
                for cms in cms_results:
                    for cms_result in cms_results[cms]:
                        self.db.put(result_type="CMS Script", script=cms,
                                    severity=0, text=cms_result)

        webapp_results = None
        if self.options.webapp_enabled or self.options.allin:
            webapp_loader = WebAppModuleLoader(log_level=self.logger.getEffectiveLevel())
            webapp_loader.load_modules()
            webapp_results = webapp_loader.run_scripts(start_url, scope=scope,
                                                       cookies=self.scan_cookies, headers=login.headers)
            if webapp_results:
                for webapp in webapp_results:
                    for webapp_result in webapp_results[webapp]:
                        self.db.put(result_type="WebApp Script", script=webapp,
                                    severity=0, text=json.dumps(webapp_result))
        meta = {}
        if self.options.msf:
            monster = metamonster.MetaMonster(log_level=self.logger.getEffectiveLevel())
            creds = self.options.msf_creds.split(':')
            monster.username = creds[0]
            monster.password = creds[1]
            monster.host = self.options.msf_host
            monster.port = self.options.msf_port
            monster.ssl = self.options.msf_ssl
            monster.endpoint = self.options.msf_uri
            monster.should_start = self.options.msf_autostart

            monster.connect(start_url)
            if monster.client and monster.client.is_working:
                monster.get_exploits()
                monster.detect()
                queries = monster.create_queries()
                monster.run_queries(queries)
                meta = monster.results
                for working in meta['working']:
                    msf_module, msf_output = working
                    self.db.put(result_type="Metasploit", script=msf_module,
                                severity=3, text=json.dumps(msf_output))

        scan_tree = {
            'start': start_time,
            'end': time.time(),
            'scope': scope.host,
            'starturl': start_url,
            'crawled': len(c.scraped_pages) if c else 0,
            'scanned': len(todo) if self.options.scanner else 0,
            'results': scanner_obj.script_engine.results if scanner_obj else [],
            'metasploit': meta,
            'cms': cms_results,
            'webapps': webapp_results,
            'post': post_results if self.options.use_adv_scripts else []
        }

        self.db.end()

        if self.options.outfile:
            self.logger.info("returned %s" % self.options.outfile)
            return json.dumps(scan_tree)




