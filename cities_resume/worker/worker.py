from protocol.protocol import Protocol

class Worker:
    def __init__(self):
        self.protocol = Protocol()
        self.positives_per_city = {}

    def start(self):
        self.protocol.start_connection(self.data_read)

        self.process_results()

    def data_read(self, place):
        if place not in self.positives_per_city:
            self.positives_per_city[place] = 0
            
        self.positives_per_city[place] += 1
    
    def process_results(self):
        for place in self.positives_per_city:
            self.protocol.send_data(place, self.positives_per_city[place])
