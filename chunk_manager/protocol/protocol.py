import pika
import sys
import random
import time

from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self):
        self.connection = Connection()
        #self.sender = self.connection.create_topic_sender("chunks")
        self.sender = self.connection.create_direct_sender("chunks")
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result
        #print("Sending {}".format(message))
        #self.sender.send_to_topic('chunks', NORMAL, message)
        self.sender.send(NORMAL, message)

    def close(self):
        print("Sending EOF")
        self.sender.send(EOF, "")
        self.connection.close()
        #self.sender.send_to_topic('chunks', EOF, '')
        #self.sender.close()
