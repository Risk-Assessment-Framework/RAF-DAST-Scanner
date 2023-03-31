# DAST Tool Features

This DAST (Dynamic Application Security Testing) tool has the following features:

- Checks for OWASP Top 10 vulnerabilities using OWASP ZAP.
- Checks for CVE (Common Vulnerabilities and Exposures) vulnerabilities using CVE API.
- Checks for SANS Top 25 vulnerabilities using Nikto scanner and matching with the list.

## OWASP Top 10 Vulnerabilities

OWASP (Open Web Application Security Project) is a community-driven organization focused on improving the security of software. The OWASP Top 10 list includes the most critical security risks to web applications. The DAST tool uses **OWASP ZAP** to scan for these vulnerabilities.

## CVE Vulnerabilities

CVE (Common Vulnerabilities and Exposures) is a list of publicly disclosed cybersecurity vulnerabilities and exposures. The **CVE API** provides access to the **CVE database**, which includes information on known vulnerabilities. The DAST tool uses the CVE API to scan for these vulnerabilities.

## SANS Top 25 Vulnerabilities

SANS (SysAdmin, Audit, Network, Security) is a cooperative research and education organization focused on cybersecurity training and awareness. The SANS Top 25 list includes the most dangerous programming errors that can lead to serious vulnerabilities. The DAST tool uses **Nikto scanner** to scan for these vulnerabilities and **matches them with the SANS Top 25 list**.

### To Do

Build an API to scan for ISO 22k vulnerabilities.