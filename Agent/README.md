# ZAP Scanner

ZAP Scanner is a Python script that uses the OWASP ZAP API to scan web applications for security vulnerabilities based on different Industry Standards.

## Requirements

- Python 3.x
- OWASP ZAP API key
- `credentials.json` file

## Installation

1. Install the required dependencies: `pip install -r requirements.txt`

## Usage

```python main.py -c <credentials_file_path> -u <target_url> -s <scan_level>```

## Arguments

- `-c, --credentials`: File path for `credentials.json` file containing API key and proxy configuration.
- `-u, --url`: Target URL for the web application to be scanned.
- `-s, --sl`: Scan level (1-4) based on different security standards.

## Supported Security Standards

1. OWASP Top 10
2. CVE-Mitre
3. SANS Top 25 Errors
4. ISO 27K

## Output

The script generates an HTML report in the project directory with the results of the scan and also opens it for the user.

