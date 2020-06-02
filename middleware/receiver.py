import pika
import sys
import random
import time

class Receiver:
    def __init__(self):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
        
        self.topics = {}

    def receive_from_topic(self, topic, callback):
        channel = self.connection.channel()

        channel.exchange_declare(exchange=topic, exchange_type='fanout')

        result = channel.queue_declare(queue='', durable=True)

        queue_name = result.method.queue

        channel.queue_bind(exchange=topic, queue=queue_name)

        channel.basic_qos(prefetch_count=1)

        channel.basic_consume(
            queue=queue_name, on_message_callback=self.data_read, auto_ack=True
        )    

        self.topics[topic] = callback

        channel.start_consuming()

    def data_read(self, ch, method, properties, body):        
        self.topics[method.exchange](body.decode('utf-8'))

    def close(self):
        self.connection.close()
