from protocol.protocol import Protocol

class ResumeMasterController:
    def __init__(self, recv_queue, send_queue):
        self.protocol = Protocol(recv_queue, send_queue)

    def start(self):
        #print("Here is called")
        self.protocol.start_connection()
        print("Is this ever called?")
        #self.protocol.send_eof()

    #def data_read(self, data):
    #   self.protocol.send_data(data)

    #def eof_read(self):
    #    self.protocol.send_eof()