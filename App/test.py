import requests
import json
url = 'http://127.0.0.1:5000/ping'
response = requests.get(url)

print(response.json())
