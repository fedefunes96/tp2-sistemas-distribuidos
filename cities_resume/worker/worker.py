from protocol.protocol import Protocol

class Worker:
    def __init__(self):
        self.protocol = Protocol()
        self.positives_per_city = {}

    def start(self):
        self.protocol.start_connection(self.data_read)

    def data_read(self, date, place, result):
        if result == 'positivi':
            if place not in self.positives_per_city:
                self.positives_per_city[place] = 0
            
            self.positives_per_city[place] += 1
