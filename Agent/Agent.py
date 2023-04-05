import json
import time
from zapv2 import ZAPv2

def read_credentials_file():
    with open('credentials.json', 'r') as f:
        credentials = json.load(f)
    apikey = credentials['apikey']
    http_proxy = credentials['http_proxy']
    https_proxy = credentials['https_proxy']
    return apikey, http_proxy, https_proxy

# Connect to the ZAP API using the API key and proxy configuration
def connect_zap(apikey, http_proxy, https_proxy):
    proxies = {'http': http_proxy, 'https': https_proxy}
    return ZAPv2(apikey=apikey, proxies=proxies)

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
    zap.ascan.disable_all_scanners()
    zap.ascan.enable_scanners(['0'])
    zap.ascan.scan(target_url)
    scan_id = zap.ascan.scan(target_url)
    while scan_id and int(zap.ascan.status(scan_id)) < 100:
        time.sleep(5)
    cves = zap.scripts.scripts(scriptType='cve').splitlines()
    mitres = zap.scripts.scripts(scriptType='mitre').splitlines()

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
def report_generator(zap,scan_list,target_url):
    report={}
    for i in scan_list:
        if i == 0:
                report["owasp_top_10"]=owasp_top_10_scan(zap,target_url)
                report["cve_mitre"]=cve_mitre_scan(zap,target_url)
                report["sans_top_25"]=sans_top_25_errors_scan(zap,target_url)
                report["iso_27k"]=iso_27001_scan(zap,target_url)
        elif i == 1:
                report["owasp_top_10"]=owasp_top_10_scan(zap,target_url)
        elif i == 2:
                report["cve_mitre"]=cve_mitre_scan(zap,target_url)
        elif i == 3:
                report["sans_top_25"]=sans_top_25_errors_scan(zap,target_url)
        elif i == 4:
                report["iso_27k"]=iso_27001_scan(zap,target_url)
        else:
                report["error"]="Invalid scan type"
    return report
        
zap=connect_zap(read_credentials_file())
target_url="https://example.com"
# Testing the script
print(report_generator(zap,[1],target_url))
