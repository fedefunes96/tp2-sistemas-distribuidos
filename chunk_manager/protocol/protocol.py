import pika
import sys
import random
import time

from middleware.sender import Sender

class Protocol:
    def __init__(self):
        self.sender = Sender()
    
    def process(self, date, latitude, longitude, result):
        message = date + "," + latitude + "," + longitude + "," + result
        #print("Sending {}".format(message))
        self.sender.send_to_topic('map_city', message)

    def close(self):
        self.sender.close()