
# Helios
Multi-threaded open-source web application security scanner

The current version can detect the following vulnerabilities:
- SQL-Injections
    - Error Based
    - Boolean Based
    - Time Based
- Cross-Site-Scripting
    - Reflected
    - Stored
- File-inclusion
    - Local file inclusion
    - Remote file inclusion
- File uploads
- Command Injection
- Backup-files
- Generic error disclosure
- Source code disclosure
- Web application fingerprint
- CMS Vulerability scanner for:
    - WordPress
    - Drupal
    - Joomla
    - Typo3
    - Textpattern
    - Magento
    - Subrion
    - CMS made simple
    - Concrete5
    - MODX Revolution
- Automatic launching of Metasploit modules (through msfrpc)
    - unsafe at the moment


# How to install
Download the repository
```
cd helios-patched
pip install .
```

# How to use (Command Line)
scan types
1. "1" - Crawl and scan an entire domain
2. "2" - Safe scan
3. "3" - Full scan
4. "4" - Scan a single url
```
import helios
from helios.run import run
run("www.example.com","2")
```
