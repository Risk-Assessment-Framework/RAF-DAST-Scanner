import requests
from app.helper import parse_zap_report
from pprint import pprint


def test_parse():
    filename = 'app/report.html'
    result = parse_zap_report(filename)
    # pprint(result[0])
    # print(len(result))


def test_api():
    url = 'http://localhost:5000/spider'
    payload = {'url': 'https://appsec.asia/'}
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json()['status']


if __name__ == '__main__':
    test_api()
    # test_parse()
