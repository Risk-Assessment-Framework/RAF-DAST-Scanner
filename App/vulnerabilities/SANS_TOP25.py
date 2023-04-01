# import requests
from flask import Flask, request, jsonify
import subprocess
import re

# initialize the Flask app
app = Flask(__name__)

# List of SANS Top 25 vulnerabilities
# SOURCE: https://www.sans.org/top25-software-errors/
SANS_TOP_25 = [
    'Injection', 'Broken Authentication and Session Management', 'Cross-Site Scripting (XSS)',
    'Broken Access Control', 'Security Misconfiguration', 'Insecure Cryptographic Storage',
    'Insufficient Transport Layer Protection', 'Unvalidated Redirects and Forwards',
    'Insecure Communication Between Components', 'Poor Coding Practices', 'Code Injection',
    'Memory Leak and Buffer Overflow', 'Race Conditions', 'Malicious File Execution',
    'Insecure Initialization and Termination', 'Insufficient Authorization',
    'SQL Injection (SQLi)', 'LDAP Injection', 'Command Injection', 'XPath Injection',
    'CSRF (Cross-Site Request Forgery)', 'OS Command Injection', 'DOM-Based XSS',
    'Security Decisions Via Untrusted Inputs', 'Web and Application Server Misconfiguration'
]


# define a route for the web application
@app.route('/scan', methods=['POST'])
def scan_website():
    # Get the URL to scan from the request data
    url = request.json['url']

    # Run the Nikto scanner and capture the output
    # output = subprocess.check_output(['nikto','-Format', 'txt']) : not working on my machine
    output = subprocess.check_output(['nikto', '-h', url, '-o', '-', '-Format', 'txt'])

    # Extract the vulnerability information from the Nikto output
    vulnerabilities = []
    for line in output.splitlines():
        # Check if the line contains a vulnerability description becuase we need to extract the vulnerability name from it
        match = re.search(r'\+[^\n]*\b(OSVDB-\d+|CVE-\d+-\d+)\b', line.decode('utf-8'))
        if not match:
            continue

        # Extract the severity level and vulnerability name from the line
        severity = re.search(r'\s+Severity: ([^,]+),', line.decode('utf-8')).group(1)
        vulnerability = match.group(1)

        # Check if the vulnerability matches any of the SANS Top 25 list items
        for item in SANS_TOP_25:
            if item.lower() in line.decode('utf-8').lower():
                # Add the vulnerability to the list to be matched against the SANS Top 25 list
                vulnerabilities.append({
                    'name': vulnerability,
                    'severity': severity,
                    'description': line.decode('utf-8').strip()
                })
                break

    # Return the list of vulnerabilities found
    return jsonify(vulnerabilities)

# start the Flask app
if __name__ == '__main__':
    app.run(debug=True)



# for line in output.splitlines():
 # The vulnerability name is either an OSVDB ID or a CVE ID
        # The OSVDB ID is in the format OSVDB-XXXXX
        # The CVE ID is in the format CVE-XXXX-XXXX
        # The OSVDB ID is deprecated and is no longer used, but it is still present in the Nikto output
        # The CVE ID is the current standard for vulnerability naming
        # The OSVDB ID is used as a fallback in case the CVE ID is not present
        # The OSVDB ID is also used for vulnerabilities that are not assigned a CVE ID