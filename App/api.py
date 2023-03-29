from flask import Flask, jsonify, request
import json
import requests
from owasp_scanner import OWASPScanner, NiktoScanner
#import vulnerability_tests

app = Flask(__name__)

# Define a route for testing the API
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'penetration testing API is working'})

# Define a route for scanning a URL
@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    url = data.get('url')
    
   # Code for scanning the URL and returning results using OWASP ZAP and Nikto scanners.
    zap_scanner = OWASPScanner(url)
    zap_spider_results = zap_scanner.spider()
    zap_active_scan_results = zap_scanner.active_scan()
    zap_port_scan_results = zap_scanner.port_scan()
    nikto_scanner = NiktoScanner(url)
    nikto_results = nikto_scanner.scan()
    message="Scan Completed succesfully"
    
    # Return the results
    return jsonify({'message':message,'owasp_spider_results': zap_spider_results, 'owasp_active_scan_results': zap_active_scan_results, 'owasp_port_scan_results': zap_port_scan_results, 'nikto_results': nikto_results})

if __name__ == '__main__':
    app.run(debug=True)
    print(app.url_map)
