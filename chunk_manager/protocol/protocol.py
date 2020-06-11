import pika
import sys
import random
import time

from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self, queue_map, queue_date, queue_count):
        self.connection = Connection()

        self.sender_map = self.connection.create_direct_sender(queue_map)
        self.sender_date = self.connection.create_direct_sender(queue_date)
        self.sender_count = self.connection.create_direct_sender(queue_count)
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result

        self.sender_map.send(NORMAL, message)
        self.sender_date.send(NORMAL, message)
        self.sender_count.send(NORMAL, message)

    def close(self):
        self.sender_map.send(EOF, "")
        self.sender_date.send(EOF, "")
        self.sender_count.send(EOF, "")
        self.connection.close()
