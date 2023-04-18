# RAF DAST 
RAF DAST tools are designed to perform comprehensive security testing on web applications and APIs, using a range of automated testing techniques such as vulnerability scanning, penetration testing, and fuzzing. These tools typically include advanced features such as support for custom scripts, integration with other security tools, and detailed reporting capabilities.

## Folder Structure
The repository has the following folder structure:
1 .api/ - Contains the REST API implementation. 
2. agents/ - Contains the agent implementation.
3. vulnerability.py - Contains the implementation of various vulnerability scanners.
4. server.py - Contains the implementation of the server to receive and store scan reports.
5. test.py - Contains test cases for the REST API.
6. The REST API uses OWASP ZAP and Nikto scanners for vulnerability scanning.

## Installation
1. Clone the repository to your local machine.
2. Install the required packages: ```pip install -r requirements.txt```
3. Start the API by running python api.py.

## To Do list
- [ ] Implement a URL scan API using existing OWASP ZAP, other open source scanners.
- [ ] Implement different vulnerability tests.
- [ ] Implement a scheduler to schedule and manage scans.
- [ ] Combine all these tools with already existing framework.
- [ ] Integrate with already existing framework.


## Usage
The API provides two routes:

```/ping``` - GET route to test if the API is working. Returns a JSON message.

```/scan``` - POST route to initiate a vulnerability scan on a URL. Expects a JSON payload with a url parameter. Returns a JSON response with the scan results.

## Testing
You can test if the api is running by running ```python test.py``` after running the API

## Contribute
Contributions to the project are welcome. To contribute:

1. Fork the repository.
2. Make changes to your fork.
3. Submit a pull request with your changes.

## Contact
putra@appsec.asia
