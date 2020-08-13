import app.routes
import json

def test_home(app, client):
    res = client.get('/')
    assert 'Hello World' == res.get_data(as_text=True)

def test_mqservice_available(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {'testdata': 'hello world'}
    res = client.post('/api/v1/mqtest', data=json.dumps(data), headers=headers)
    assert res.status_code == 200
    print(res.get_data(as_text=True))
    assert '[x] Sent {}'.format(json.dumps(data)) == res.get_data(as_text=True)