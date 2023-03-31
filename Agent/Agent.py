import json
import os
import platform
from time import sleep
from datetime import datetime
from vulnerability import OwaspTop10Scanner, CVEMitreScanner, SANSTop25Scanner, ISO27001Scanner
import requests

os_name = platform.system() + " " + platform.release()

server_url = "http://localhost:8000/vuln_report"
scan_interval = 60 * 60  # Scan interval in seconds (1 hour)
agent_name = "Agent 1.0.1.2"
api_key = os.environ.get('API_KEY')

owasp_scanner = OwaspTop10Scanner()
cve_mitre_scanner = CVEMitreScanner()
sans_top25_scanner = SANSTop25Scanner()
iso_27001_scanner = ISO27001Scanner()

while True:
    time = datetime.now()

    owasp_results = owasp_scanner.run_scan()
    cve_mitre_results = cve_mitre_scanner.run_scan()
    sans_top25_results = sans_top25_scanner.run_scan()
    iso_27001_results = iso_27001_scanner.run_scan()

    all_results = owasp_results + cve_mitre_results + sans_top25_results + iso_27001_results

    report = {
        "agent_name": agent_name,
        "OS": os_name,
        "timestamp": time.timestamp(),
        "vulnerabilities": all_results
    }

    report_json = json.dumps(report)

    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.post(server_url, data=report_json, headers=headers)

    print(f"Report sent to server. Status code: {response.status_code}")

    sleep(scan_interval)
