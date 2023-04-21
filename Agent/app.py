from flask import Flask, request, jsonify
from Agent import read_credentials_file, connect_zap, report_generator

app = Flask(__name__)


@app.route('/scan', methods=['POST'])
def scan():
    try:
        target_url = request.json['target_url']
        scan_list = request.json['scan_list']
        apikey, http_proxy, https_proxy = read_credentials_file()
        zap = connect_zap(apikey, http_proxy, https_proxy)
        report = report_generator(zap, scan_list, target_url)
        return jsonify({'status': 'success', 'report': report})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


if __name__ == '__main__':
    app.run()
