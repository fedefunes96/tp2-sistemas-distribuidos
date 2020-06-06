from protocol.protocol import Protocol

class MasterController:
    def __init__(self):
        self.protocol = Protocol()

    def start(self):
        #print("Here is called")
        self.protocol.start_connection(self.data_read, self.eof_read)
        print("Is this ever called?")

    def data_read(self, data):
       self.protocol.send_data(data)

    def eof_read(self):
        self.protocol.send_eof()