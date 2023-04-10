import json
import time
from zapv2 import ZAPv2
import webbrowser
import os

def read_credentials_file(file):
    with open(file, 'r') as f:
        credentials = json.load(f)
    apikey = credentials['apikey']
    http_proxy = credentials['http_proxy']
    https_proxy = credentials['https_proxy']
    return [apikey, http_proxy, https_proxy]

# Connect to the ZAP API using the API key and proxy configuration
def connect_zap(list):
    proxies = {'http': list[1], 'https': list[2]}
    return ZAPv2(apikey=list[0], proxies=proxies)

# Owasp Top 10
def owasp_top_10_scan(zap,target_url):
# disable scanners
    zap.ascan.disable_all_scanners()
    zap.ascan.enable_scanners(['10015', '10016', '10017', '10018', '10019', '10020', '10021', '10022', '10024', '10045'])
    zap.ascan.scan(target_url)
    scan_id = zap.ascan.scan(target_url)
    print(scan_id)
    time.sleep(10)
    print(scan_id)
    while scan_id and int(zap.ascan.status(scan_id)) < 100:
        time.sleep(5)
    report= zap.core.jsonreport()
    return report

# cve_mitre
def cve_mitre_scan(zap,target_url):
    cves="test1"
    mitres="test2"

    vulnerabilities = {}
    vulnerabilities['cve'] = cves
    vulnerabilities['mitre'] = mitres
    return json.dumps(vulnerabilities)
    

# SANS Top 25
def sans_top_25_errors_scan(zap,target_url):
    zap.ascan.disable_all_scanners()
    zap.ascan.enable_scanners(['90011'])
    zap.ascan.scan(target_url)
    scan_id = zap.ascan.scan(target_url)
    while scan_id and int(zap.ascan.status(scan_id)) < 100:
        time.sleep(5)
    report = zap.core.jsonreport()
    return report

# ISO 27K
def iso_27001_scan(zap,target_url):
    zap.ascan.disable_all_scanners()
    zap.ascan.enable_scanners(['30013']) 
    zap.ascan.scan(target_url)
    scan_id = zap.ascan.scan(target_url)
    while scan_id and int(zap.ascan.status(scan_id)) < 100:
        time.sleep(5)
    report = zap.core.jsonreport()
    return report

# generate report
def report_generator(zap,i,target_url):
        if i == "1":
                owasp_top_10_scan(zap,target_url)
        elif i == "2":
                cve_mitre_scan(zap,target_url)
        elif i == "3":
                sans_top_25_errors_scan(zap,target_url)
        elif i == "4":
                iso_27001_scan(zap,target_url)
        else:
                print("Invalid standard type")

def spider(zap,target_url):
    zap.spider.scan(target_url)
    time.sleep(10)

def report_html(zap):
    report_html = zap.core.htmlreport()
    with open('report.html', 'w') as f:
        f.write(report_html)

    file = "report.html"
    filename = 'file:///'+os.getcwd()+'/' + file
    webbrowser.open_new_tab(filename)
