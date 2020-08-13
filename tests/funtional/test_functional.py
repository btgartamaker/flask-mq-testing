import requests
import json


def test_server_is_running():
    response = requests.get('http://127.0.0.1:5000')
    assert response.status_code == 200
    assert 'Hello World' in response.text, print(response.text)

def test_mqservice():
    body = {'testdata': 'hello world'}
    response = requests.post(url='http://127.0.0.1:5000/api/v1/mqtest', json=body)
    assert response.status_code == 200
    print(response.text)
    assert '[x] Sent {}'.format(json.dumps(body)) == response.text