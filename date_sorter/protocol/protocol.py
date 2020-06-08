import pika
import sys
import random
import time
import json

from middleware.connection import Connection

NORMAL = "NORMAL"
DATE_RESULTS = "DATE_RESULTS"
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
            print("Received eoF")
            self.receiver.close()
        else:
            self.callback(json.loads(msg))

    def send_data(self, date_data):
        self.sender.send(DATE_RESULTS, json.dumps(date_data))
        self.sender.send(EOF, '')
