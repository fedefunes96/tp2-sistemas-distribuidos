import pika
import sys
import random
import time
import json

from middleware.connection import Connection

NORMAL = "NORMAL"
TOP_CITIES = "TOP_CITIES"
EOF = "EOF"

class Protocol:
    def __init__(self, recv_queue, send_queue):
        self.connection = Connection()
        self.receiver = self.connection.create_direct_receiver(recv_queue)
        self.sender = self.connection.create_direct_sender(send_queue)

    def start_connection(self, callback):
        self.callback = callback
        self.receiver.start_receiving(self.data_read)

    def data_read(self, msg_type, msg):
        if msg_type == EOF:
            self.receiver.close()
        else:
            self.callback(json.loads(msg))

    def send_data(self, top_cities):
        self.sender.send(TOP_CITIES, json.dumps(top_cities))
        self.sender.send(EOF, '')