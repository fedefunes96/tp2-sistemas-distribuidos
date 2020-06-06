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

        self.receiver.receive_from_topic("chunks", self.data_read)
    
    def send_data(self, data):
        self.sender.distribute_work("map_city", NORMAL, data)

    def data_read(self, method, msg_type, msg):
        if msg_type == "EOF":
            self.receiver.close_topic("chunks")
            self.callback_eof()
        else:            
            self.callback_normal(msg)

    def send_eof(self):
        self.sender.distribute_work("map_city", EOF, '')
