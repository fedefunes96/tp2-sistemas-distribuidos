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
        self.work_queues = {}

    def connect_to_work_queue(self, queue):
        self.work_queues[queue] = self.connection.channel()

        self.work_queues[queue].queue_declare(queue=queue, durable=True)

    def distribute_work(self, queue, msg_type, message):
        if queue not in self.work_queues:
            self.connect_to_work_queue(queue)
        
        self.work_queues[queue].basic_publish(
            exchange='',
            routing_key=queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
                type=msg_type
            )
        )

    def connect_to_topic(self, topic):
        self.channels[topic] = self.connection.channel()

        self.channels[topic].exchange_declare(exchange=topic, exchange_type='fanout')
    
    def send_to_topic(self, topic, msg_type, message):
        if topic not in self.channels:
            self.connect_to_topic(topic)

        self.channels[topic].basic_publish(
            exchange=topic,
            routing_key='',
            body=message,
            properties=pika.BasicProperties(
                type=msg_type
            )
        )
    
    def close(self):
        self.connection.close()
