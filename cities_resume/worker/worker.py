from protocol.protocol import Protocol

class Worker:
    def __init__(self):
        self.protocol = Protocol()

    def start(self):
        self.protocol.start_connection(self.data_read)

    def data_read(self, date, place, result):
        print(place)