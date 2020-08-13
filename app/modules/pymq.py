from app import app
import pika

class PyMQConnection(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=app.config['RABBIT_URL'], heartbeat=30))
        self.channel = self.connection.channel()

    
    def call(self, message):
        self.channel.basic_publish(exchange='', routing_key=app.config['MQTEST_ROUTINGKEY'], body=message, properties=pika.BasicProperties(delivery_mode = 2,))

    def listen(self, queue, callback):
        self.queue = queue
        self.channel.queue_declare(queue=self.queue)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue, auto_ack=True, on_message_callback=callback)
        self.channel.start_consuming()