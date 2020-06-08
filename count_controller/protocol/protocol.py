import pika
import sys
import random
import time

from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self, recv_queue, send_queue, master_send_queue):
        self.connection = Connection()
        self.receiver = self.connection.create_distributed_work_receiver(recv_queue)
        self.sender = self.connection.create_direct_sender(send_queue)
        self.master_sender = self.connection.create_direct_sender(master_send_queue)

    def start_connection(self, callback):
        self.callback = callback

        self.receiver.start_receiving(self.data_read)
    
    def send_data(self, total_positivi, total_deceduti):
        msg = str(total_positivi) + "," + str(total_deceduti)
        self.sender.send(NORMAL, msg)
        self.master_sender.send(EOF, "")
        self.connection.close()

    def data_read(self, method, msg_type, msg):
        if msg_type == EOF:
            print("RECEIVED EOF WORKER!!!!!!!!!!!!!!!!!!!")
            self.receiver.send_ack(method)
            self.receiver.close()
        else:            
            self.callback(msg)
            self.receiver.send_ack(method)
