import pika
import sys
import random
import time

from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self, send_queue):
        self.connection = Connection()
        self.sender = self.connection.create_direct_sender(send_queue)
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result

        self.sender.send(NORMAL, message)

    def close(self):
        print("Sending EOF")
        self.sender.send(EOF, "")
        self.connection.close()

