from protocol.protocol import Protocol

class SummaryController:
    def __init__(self, recv_queue):
        self.protocol = Protocol(recv_queue)

    def start(self):
        self.protocol.start_connection(self.top_cities_read)

    def top_cities_read(self, top_cities):
        print(top_cities)