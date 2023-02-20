import requests

def test_api():
    url = 'http://localhost:5000/scan'
    payload = {'url': 'https://www.example.com'}
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert response.json() == {'result': 'success'}


if __name__ == '__main__':
    test_api()
