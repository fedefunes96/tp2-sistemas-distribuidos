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

        #self.receiver = self.connection.create_topic_receiver("chunks")
        self.receiver = self.connection.create_direct_receiver("chunks")
        self.sender = self.connection.create_distributed_work_sender("map_city")

    def start_connection(self, callback_normal):
        self.callback_normal = callback_normal
        #self.callback_eof = callback_eof

        self.receiver.start_receiving(self.data_read)

        #self.receiver.receive_from_topic("chunks", self.data_read)
    
    def send_data(self, data):
        self.sender.send(NORMAL, data)
        #self.sender.distribute_work("map_city", NORMAL, data)

    def data_read(self, msg_type, msg):
        if msg_type == "EOF":
            self.receiver.close()
            self.send_eof()
            #self.receiver.close_topic("chunks")
            #self.callback_eof()
        else:            
            self.callback_normal(msg)
        
    '''def status_read(self, msg_type, msg):
        print("Received EOF from map worker")
        self.sender = self.connection.create_direct_sender("cities_resume")
        self.sender.send(EOF, '')
        self.connection.close()

    def start_connection_workers(self, callback):
        self.receiver = self.connection.create_direct_receiver("master_map")
        self.receiver.start_receiving(self.status_read)'''

    def send_eof(self):
        print("Sending EOF to map workers")
        self.sender.send(EOF, '')
        self.connection.close()
        #self.receiver = self.connection.create_direct_receiver("master_map")
        #self.receiver.start_receiving(self.status_read)
        #self.sender.distribute_work("map_city", EOF, '')

        #self.receiver.receive_from_topic("chunks", self.data_read)