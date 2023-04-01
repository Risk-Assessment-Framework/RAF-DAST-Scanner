
# Helios

Helios is a multi-threaded open-source web application security scanner that can detect various vulnerabilities in web applications. The current version can detect the following vulnerabilities:

```mermaid

graph  LR

A[Helios]  -->  B[SQL-Injections]

B  -->  B1[Error Based]

B  -->  B2[Boolean Based]

B  -->  B3[Time Based]

A  -->  C[Cross-Site-Scripting]

C  -->  C1[Reflected]

C  -->  C2[Stored]

A  -->  D[File-inclusion]

D  -->  D1[Local file inclusion]

D  -->  D2[Remote file inclusion]

A  -->  E[File uploads]

A  -->  F[Command Injection]

A  -->  G[Backup-files]

A  -->  H[Generic error disclosure]

A  -->  I[Source code disclosure]

A  -->  J[Web application fingerprint]

A  -->  K[CMS Vulnerability scanner]

K  -->  K1[WordPress]

K  -->  K2[Drupal]

K  -->  K3[Joomla]

K  -->  K4[Typo3]

K  -->  K5[Textpattern]

K  -->  K6[Magento]

K  -->  K7[Subrion]

K  -->  K8[CMS made simple]

K  -->  K9[Concrete5]

K  -->  K10[MODX Revolution]

A  -->  L[Automatic launching of Metasploit modules]

L  -->  L1[unsafe at the moment]

```

## Functioning of new version

```mermaid
graph TD

A[Start] --> B[Parse Arguments]

B --> C{URL or File?}

C --> |URL| D[Create Helios Instance with URL]

C --> |File| E[Create Helios Instance with File]

D --> F[Run Helios Instance]

E --> F

F --> G[Exit]
```

## How Helios works?
```mermaid
graph LR

A[Command Line Arguments] --> B{Chromedriver Options}

B --> |"Run WebDriver for advanced discovery"| C((WebDriver))

C --> |"Show the WebDriver window"| D[Display Browser Window]

D --> |"Interact with the displayed webpage"| C

B --> |"Enable the crawler"| E{Crawler Options}

E --> |"Crawl and scan an entire domain"| F[Crawl and Scan Domain]

E --> |"Set max urls for the crawler"| G[Set Max URLs]

E --> |"Set extra allowed scopes"| H[Set Extra Scopes]

E --> |"Enable the scanner"| I{Scanner Options}

I --> |"Safe scan"| J[Safe Scan]

I --> |"Full scan"| K[Full Scan]

I --> |"Scan a single URL"| L[Scan Single URL]

I --> |"Enable scanning of web application frameworks"| M[Scan Webapps and CMS Systems]

I --> |"Enable the msfrpcd exploit module"| N{Metasploit Options}

N --> |"Pwn a web server"| O[Pwn Web Server]

A --> |"Show help message"| P[Display Help Message]
```

## Installation

To install Helios, download the repository and run the following command:
```
   cd helios-patched
   pip install . 
```

## Usage

You can use Helios through the command line. There are four types of scans available:

1.  "1" - Crawl and scan an entire domain
2.  "2" - Safe scan
3.  "3" - Full scan
4.  "4" - Scan a single URL

Here is an example of how to run a safe scan:


    import helios from helios.run 
    import run
    run("www.example.com","2")

## Credits


The original author of Helios is Stefan Vlems. The project is licensed under the Apache 2.0 license.

 - [PROJECT LINK](https://github.com/stefan2200/Helios) 
 - [GITHUB USER](https://github.com/stefan2200)

## Modified Package

 - Files changed by @Pranav0-0Aggarwal
 - Documented by @juhiechandra
 - Mentored by @adeyosemanputra

