from protocol.protocol import Protocol
import json

class SummaryController:
    def __init__(self, recv_queue):
        self.protocol = Protocol(recv_queue)
        self.top_cities = {}

    def start(self):
        self.protocol.start_connection(self.top_cities_read)

        self.write_summary()

    def top_cities_read(self, top_cities):
        print(top_cities)
        self.top_cities = top_cities
    
    def write_summary(self):
        with open('summary/summary.txt', 'w') as file:
            file.write(json.dumps(self.top_cities))
