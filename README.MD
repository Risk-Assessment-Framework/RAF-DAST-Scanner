# RAF DAST 
RAF DAST tools are designed to perform comprehensive security testing on web applications and APIs, using a range of automated testing techniques such as vulnerability scanning, penetration testing, and fuzzing. These tools typically include advanced features such as support for custom scripts, integration with other security tools, and detailed reporting capabilities.


The REST API uses OWASP ZAP and Nikto scanners for vulnerability scanning.

## Installation
1. Clone the repository to your local machine.
2. Install the required packages: ```pip install -r requirements.txt```
3. Start the API by running python api.py.

## Usage
The API provides two routes:

```/ping``` - GET route to test if the API is working. Returns a JSON message.

```/scan``` - POST route to initiate a vulnerability scan on a URL. Expects a JSON payload with a url parameter. Returns a JSON response with the scan results.

## Testing
You can test if the api is running by running ```python test.py``` after running the API

