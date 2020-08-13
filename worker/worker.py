#!/usr/bin/env python 
import pika
from app.modules.pymq import PyMQConnection
import json



def callback(ch, method, props, body):
    temp = json.loads(body.decode('utf-8'))
    response = temp['testdata'] 
    print(" [x] Received {}".format(response))

listener = PyMQConnection()
listener.listen('testqueue', callback)