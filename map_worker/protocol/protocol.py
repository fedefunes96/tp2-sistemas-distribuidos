import pika
import sys
import random
import time

from middleware.receiver import Receiver
from middleware.sender import Sender

class Protocol:
    def __init__(self):
        self.receiver = Receiver()
        self.sender = Sender()

    def start_connection(self, callback):
        self.callback = callback
        self.receiver.receive_from_topic("map_city", self.data_read)
    
    def send_located_data(self, date, place, result):
        message = date + ',' + place + ',' + result
        self.sender.send_to_topic("resume_city", message)

    def data_read(self, msg):
        [date, latitude, longitude, result] = msg.split(",")
        
        self.callback(date, float(latitude), float(longitude), result)
