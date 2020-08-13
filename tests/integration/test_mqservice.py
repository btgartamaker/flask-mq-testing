import pika
from app import app
from app.modules.pymq import PyMQConnection
import json


def test_connection_to_mqservice(app):
    connection = PyMQConnection()
    assert connection

def test_add_to_mqservice(app, client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {'testdata': 'hello world'}
    rabbit_url = app.config['RABBIT_URL']
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_url))
    channel = connection.channel()
    result = channel.queue_declare(queue=app.config['MQTEST_ROUTINGKEY'])
    expected_result = int(result.method.message_count) +1
    print(result)
    #channel.basic_publish(exchange='', routing_key=app.config['MQTEST_ROUTINGKEY'], body=json.dumps(data))

    response = client.post('/api/v1/mqtest', data=json.dumps(data), headers=headers)
    print(response.status_code)
    new_results = channel.queue_declare(queue=app.config['MQTEST_ROUTINGKEY'])
    new_len = new_results.method.message_count
    print(new_results)

    assert new_len == expected_result
    assert '[x] Sent {}'.format(json.dumps(data)) == response.get_data(as_text=True)
    
