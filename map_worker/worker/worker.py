from protocol.protocol import Protocol

class Worker:
    def __init__(self):
        self.protocol = Protocol(self.data_read)

    def start(self):
        self.protocol.start_connection()

    def data_read(self, date, latitude, longitude, result):
        print("{} {} {} {}".format(date, latitude, longitude, result))