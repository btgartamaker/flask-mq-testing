import os

class Config(object):
    RABBIT_URL = os.environ.get('RABBIT_URL') or 'localhost'
    MQTEST_ROUTINGKEY = os.environ.get('RABBIT_MQTEST_ROUTINGKEY') or 'testqueue'
    MQTEST_EXCHANGE = os.environ.get('RABBIT_MQTEST_EXCHANGE') or 'testexchange'
    MQTEST_EXCHANGETYPE = os.environ.get('RABBIT_MQTEST_EXCHANGETYPE') or 'direct'