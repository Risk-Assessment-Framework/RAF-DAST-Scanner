import requests
from app.helper import parse_zap_report


def test_api():
    url = 'http://localhost:5000/spider'
    payload = {'url': 'https://public-firing-range.appspot.com', 'ascan': False}
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    # assert response.json()['status']
    print(response.json())


if __name__ == '__main__':
    test_api()
