import pika
import sys
import random
import time

class Sender:
    def __init__(self):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )

        self.channels = {}

    def connect_to_topic(self, topic):
        self.channels[topic] = self.connection.channel()

        self.channels[topic].exchange_declare(exchange=topic, exchange_type='fanout')
    
    def send_to_topic(self, topic, message):
        if topic not in self.channels:
            self.connect_to_topic(topic)

        self.channels[topic].basic_publish(exchange=topic, routing_key='', body=message)
    
    def close(self):
        self.connection.close()
