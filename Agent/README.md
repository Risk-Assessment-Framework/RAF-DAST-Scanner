# Agent Scanner using ZAP API
This project is a Flask API that allows you to run Agent based security scans using the OWASP ZAP security tool. It provides the following scans:

* OWASP Top 10
* CVE-Mitre
* SANS Top 25
* ISO 27K

The API is based on the zapv2 module, which provides an interface to the ZAP API.

## API Endpoints
This API has the following endpoints:

### POST /scan
This endpoint initiates a security scan. It accepts a JSON payload with the following fields:

* url (string): the URL of the website to scan.
* scans (list of integers): the list of scans to perform. Valid scan IDs are:
  *  `0`: perform all scans.
  *  `1`: perform the OWASP Top 10 scan.
  *  `2`: perform the CVE-Mitre scan.
  *  `3`: perform the SANS Top 25 scan.
  *  `4`: perform the ISO 27K scan.
 
 ## Example Payload
 ```
 {
    "url": "https://example.com",
    "scans": [1, 2]
}
```
