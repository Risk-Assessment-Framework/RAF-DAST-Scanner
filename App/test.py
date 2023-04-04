import requests
import json
baseUrl = "http://127.0.0.1:5000"
targetUrl = "https://public-firing-range.appspot.com"


def test_ping():
    url = baseUrl + '/ping'
    response = requests.get(url)
    assert response.status_code == 200
    print(response.json())


def test_scan():
    url = baseUrl + '/scan'
    data = {'url': targetUrl}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    print(response.json())


test_ping()
test_scan()
