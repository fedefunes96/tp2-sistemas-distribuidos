import pika
import sys
import random
import time

#from middleware.receiver import Receiver
#from middleware.sender import Sender
from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self):
        #self.receiver = Receiver()
        #self.sender = Sender()
        self.connection = Connection()
        self.receiver = self.connection.create_distributed_work_receiver("map_city")
        self.sender = self.connection.create_direct_sender("cities_resume")

    def start_connection(self, callback_normal, callback_eof):
        self.callback_normal = callback_normal
        self.callback_eof = callback_eof

        self.receiver.start_receiving(self.data_read)

        #self.receiver.receive_distributed_work("map_city", self.data_read)
    
    def send_located_data(self, date, place, result):
        message = date + ',' + place + ',' + result
        self.sender.send(NORMAL, message)
        #self.sender.send_to_topic("resume_city", NORMAL, message)

    def send_ended(self):
        print("Sending END to master")
        self.sender = self.connection.create_direct_sender("master_map")
        self.sender.send(EOF, "")
        print("Map controller STOP")
        self.connection.close()
        #self.sender.send_to_topic("master_map", EOF, "")

    def data_read(self, method, msg_type, msg):
        #print("Received messsage")
        if msg_type == EOF:
            print("Received EOF")
            self.receiver.send_ack(method)
            #self.receiver.ack_work_done("master_map", method)
            self.receiver.close()
            self.callback_eof()
        else:
            [date, latitude, longitude, result] = msg.split(",")
            
            self.callback_normal(date, float(latitude), float(longitude), result)
            self.receiver.send_ack(method)
            #self.receiver.ack_work_done("master_map", method)

