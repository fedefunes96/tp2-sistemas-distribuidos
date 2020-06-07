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
        self.receiver = self.connection.create_direct_receiver("top_cities")

    def start_connection(self, callback):
        self.callback = callback
        self.receiver.start_receiving(self.data_read)

    def data_read(self, msg_type, msg):
        if msg_type == EOF:
            print("Received eoF")
            self.receiver.close()
        else:
            [place, cases] = msg.split(",")
            
            #print(place)

            self.callback(place, cases)
