import pika
import sys
import random
import time

from middleware.sender import Sender

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self):
        self.sender = Sender()
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result
        #print("Sending {}".format(message))
        self.sender.send_to_topic('chunks', NORMAL, message)

    def close(self):
        self.sender.send_to_topic('chunks', EOF, '')
        self.sender.close()
