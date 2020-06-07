#from middleware.receiver import Receiver
#from middleware.sender import Sender

from middleware.connection import Connection

NORMAL = "NORMAL"
EOF = "EOF"

class Protocol:
    def __init__(self, recv_queue, send_queue):
        self.connection = Connection()

        self.receiver = self.connection.create_direct_receiver(recv_queue)
        self.sender = self.connection.create_direct_sender(send_queue)

    def start_connection(self):
        self.receiver.start_receiving(self.data_read)

    def data_read(self, msg_type, msg):
        if msg_type == "EOF":
            self.receiver.close()
            print("Sending EOF to map workers")
            self.sender.send(EOF, '')
            self.connection.close()
