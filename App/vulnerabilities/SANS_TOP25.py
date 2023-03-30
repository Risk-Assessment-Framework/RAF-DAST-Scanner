from flask import Flask, request, jsonify
import subprocess
import re

app = Flask(__name__)

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

