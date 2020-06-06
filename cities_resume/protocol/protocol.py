import pika
import sys
import random
import time

from middleware.receiver import Receiver

class Protocol:
    def __init__(self):
        self.receiver = Receiver()

    def start_connection(self, callback):
        self.callback = callback
        self.receiver.receive_from_topic("resume_city", self.data_read)

    def data_read(self, method, msg_type, msg):
        if msg_type == "EOF":
            print("Received eoF")
        else:
            [date, place, result] = msg.split(",")
            
            #print(place)

            self.callback(date, place, result)
