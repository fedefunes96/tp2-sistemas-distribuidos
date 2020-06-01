import pika
import sys
import random
import time

class Protocol:
    def __init__(self, callback):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )

        self.callback = callback

        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='map_city', exchange_type='fanout')

        result = self.channel.queue_declare(queue='', durable=True)

        queue_name = result.method.queue

        self.channel.queue_bind(exchange='map_city', queue=queue_name)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            queue=queue_name, on_message_callback=self.data_read, auto_ack=True)
    
    def start_connection(self):
        self.channel.start_consuming()

    def data_read(self, ch, method, properties, body):
        [date, latitude, longitude, result] = body.decode("utf-8").split(",")
        
        self.callback(date, latitude, longitude, result)
