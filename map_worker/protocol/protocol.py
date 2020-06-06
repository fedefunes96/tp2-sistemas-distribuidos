import pika
import sys
import random
import time

from middleware.receiver import Receiver
from middleware.sender import Sender

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self):
        self.receiver = Receiver()
        self.sender = Sender()

    def start_connection(self, callback_normal, callback_eof):
        self.callback_normal = callback_normal
        self.callback_eof = callback_eof

        self.receiver.receive_distributed_work("map_city", self.data_read)
    
    def send_located_data(self, date, place, result):
        message = date + ',' + place + ',' + result
        self.sender.send_to_topic("resume_city", NORMAL, message)

    def send_ended(self):
        self.sender.send_to_topic("master_map", EOF, "")

    def data_read(self, method, msg_type, msg):
        if msg_type == EOF:
            self.receiver.ack_work_done("master_map", method)
            self.receiver.close()
            self.callback_eof()
        else:
            [date, latitude, longitude, result] = msg.split(",")
            
            self.callback_normal(date, float(latitude), float(longitude), result)
            self.receiver.ack_work_done("master_map", method)

