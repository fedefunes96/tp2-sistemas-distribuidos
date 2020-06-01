import pika
import sys
import random
import time

class Protocol:
    def __init__(self):
        self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )

        self.channel = self.connection.channel()

        self.channel.exchange_declare(exchange='map_city', exchange_type='fanout')
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result
        #print("Sending {}".format(message))
        self.channel.basic_publish(exchange='map_city', routing_key='', body=message)

    def close(self):
        self.connection.close()