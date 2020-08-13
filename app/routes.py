from app import app
from app.modules.pymq import PyMQConnection
from flask import request
import json
import pika





@app.route('/')
def home():
    return 'Hello World'

@app.route('/api/v1/mqtest',methods=['POST'])
def mqservice():
    mq_connection = PyMQConnection()
    data = request.data
    mq_connection.call(data)

    return '[x] Sent {}'.format(data.decode('utf-8'))