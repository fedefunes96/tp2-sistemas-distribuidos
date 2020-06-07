from middleware.connection import Connection
import json

TOP_CITIES = "TOP_CITIES"
EOF = "EOF"

class Protocol:
    def __init__(self, recv_queue):
        self.connection = Connection()

        self.receiver = self.connection.create_direct_receiver(recv_queue)

    def start_connection(self, callback_top):
        self.callback_top = callback_top
        self.receiver.start_receiving(self.data_read)

    def data_read(self, msg_type, msg):
        if msg_type == EOF:
            #Count and then close connection
            self.connection.close()
        elif msg_type == TOP_CITIES:
            self.callback_top(json.loads(msg))
