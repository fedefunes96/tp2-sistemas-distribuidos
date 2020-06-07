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
        self.receiver = self.connection.create_direct_receiver("cities_resume")
        self.sender = self.connection.create_direct_sender("top_cities")
        self.master_sender = self.connection.create_direct_sender("resume_master")

    def start_connection(self, callback):
        self.callback = callback
        self.receiver.start_receiving(self.data_read)

    def send_data(self, place, cases):
        msg = place + "," + str(cases)

        self.sender.send(NORMAL, msg)

        self.master_sender.send(EOF, "")

    def data_read(self, msg_type, msg):
        if msg_type == EOF:
            print("Received eoF")
            self.receiver.close()
        else:
            self.callback(msg)
