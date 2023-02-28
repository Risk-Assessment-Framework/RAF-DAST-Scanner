from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)


@app.route('/scan', methods=['POST'])
def get_data():
    url = request.json['url']
    print(f"Scanning for: {url}")

    cmd = f"sudo docker run -v $(pwd):/zap/wrk/:rw -t owasp/zap2docker-stable zap-baseline.py -t {url} -r report.html"

    process = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 2:
        print(f"Error running command: {stderr.decode('utf-8')}")
    else:
        print(f"Command executed successfully.")

    data = {'result': 'success'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
