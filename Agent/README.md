# Vulnerability Scanning System

This repository contains code for a vulnerability scanning system, consisting of three main components:

- `server.py`: A server that receives vulnerability reports from agents and stores them in a database and analyse the vulnerabilities.
- `agent.py`: An agent that runs on each machine to be scanned, performs scans using various vulnerability scanners, and sends reports to the server.
- `vulnerability.py`: A module containing several vulnerability scanners, including the OWASP Top 10 scanner, CVE MITRE scanner, SANS Top 25 scanner, and ISO 27001 scanner.

## Usage

To use the system, follow these steps:

1. Clone the repository to your local machine.
2. Modify `server.py` to set up your database connection and API endpoint URL.
3. Modify `agent.py` to set up your API endpoint URL and vulnerability scanners to run.
4. Start the server by running `python server.py`.
5. Install the agent on each machine to be scanned by running `python agent.py`.

## Dependencies

This system requires the following Python packages to be installed:

- `requests`
- `json`
- `os`
- `time`
- `datetime`
- `platform`
