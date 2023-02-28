from flask import Flask, jsonify, request
import time
from flask_cors import CORS, cross_origin
from zapv2 import ZAPv2
import os
import urllib.request
import tarfile
from helper import dict_to_json_file
from pprint import pprint

# Define a global variable to store the ZAP API key
API_KEY = 'mk5f08maq9eh575sem'


# Define ZAP API client
zap = ZAPv2(apikey=API_KEY, proxies={
    'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})


# Define a Flask app and a Docker client
app = Flask(__name__)
CORS(app)


def verify_zap_running():
    """_summary_: Verify if ZAP is running.
    """

    try:
        urllib.request.urlopen('http://localhost:8080')
        print("ZAP is running.")
        return True
    except urllib.error.URLError:
        print("ZAP is not running. Please start ZAP and try again.")
        return False


def verify_zap_exists():
    """_summary_: Download ZAP.
    """
    filename = "ZAP_2.12.0_Linux.tar.gz"
    extractDir = "ZAP_2.12.0"
    zapDirname = "zap"

    if os.path.exists(os.path.join(".", zapDirname)):
        print("ZAP package already exists in current directory.")
    else:
        print("ZAP package not found in current directory. Downloading...")
        url = "https://github.com/zaproxy/zaproxy/releases/download/v2.12.0/ZAP_2.12.0_Linux.tar.gz"
        urllib.request.urlretrieve(url, filename)
        print("Download complete.")

        print("Extracting ZAP package...")
        tar = tarfile.open(filename, "r:gz")
        tar.extractall()
        tar.close()
        print("Extraction complete.")

        print("Renaming directory...")
        os.rename(os.path.join(".", extractDir),
                  os.path.join(".", zapDirname))
        print("Renaming complete.")

        print("Deleting tar.gz file...")
        os.remove(filename)
        print("Deletion complete.")

        print("ZAP package downloaded and extracted successfully.")


@app.route('/spider', methods=['POST'])
@cross_origin()
def get_data():
    url = request.json['url']
    isActiveScan = False
    isActiveScan = request.json.get('ascan', False)

    print(f"Scanning for: {url}")
    print('Spidering target {}'.format(url))
    # The scan returns a scan id to support concurrent scanning
    scanID = zap.spider.scan(url)
    while int(zap.spider.status(scanID)) < 100:
        # Poll the status until it completes
        print('Spider progress %: {}'.format(zap.spider.status(scanID)))
        time.sleep(1)
    print('Spider has completed!')

    # Passive scan
    print('Passive Scanning target {}'.format(url))
    while int(zap.pscan.records_to_scan) > 0:
        # Loop until the passive scan has finished
        print('Records to passive scan : ' + zap.pscan.records_to_scan)
        time.sleep(2)

    print('Passive Scan completed')

    # Active scan
    if isActiveScan:
        print("Active Scan for Target: {}".format(url))
        scan_id = zap.ascan.scan(url)

        while int(zap.ascan.status(scan_id)) < 100:
            print("Active scan completed: {} % ".format(
                zap.ascan.status(scan_id)))
            time.sleep(5)

        print("Active Scan Completed")

    # Save all scan results to a file
    dict_to_json_file({"Scan Results": {
                      "alerts": zap.alert.alerts(baseurl=url)}}, "scan_results.json")

    return jsonify({"Scan Results": {
        "alerts": zap.alert.alerts(baseurl=url)}})


@app.route('/pscan', methods=['POST'])
def passive_scan():
    while int(zap.pscan.records_to_scan) > 0:
        # Loop until the passive scan has finished
        print('Records to passive scan : ' + zap.pscan.records_to_scan)
        time.sleep(2)

    print('Passive Scan completed')

    # Print Passive scan results/alerts
    dict_to_json_file({"Passive Scan": {"hosts": zap.core.hosts,
                      "alerts": zap.core.alerts()}}, "passive_scan_results.json")
    return jsonify({"status": True})


if __name__ == '__main__':
    # To run ZAP in daemon mode, use the following command in terminal:
    # zap/zap.sh -daemon -config api.key=mk5f08maq9eh575sem
    # Or run ZAP in your local machine on port 8080
    verify_zap_exists()
    verify_zap_running()
    app.run(debug=True, port=5000)
    print("Stopping ZAP...")
