from protocol.protocol import Protocol
from collections import Counter

class TopCitiesController:
    def __init__(self):
        self.protocol = Protocol()
        self.cities_data = {}
        self.top_cities = {}

    def start(self):
        self.protocol.start_connection(self.data_read)

        self.process_results()

    def data_read(self, place, cases):
        self.cities_data[place] = cases
    
    def process_results(self):
        print(self.cities_data)

        self.top_cities = dict(Counter(self.cities_data).most_common(3))

        print("Top cities are")
        print(self.top_cities)

        self.protocol.send_data(self.top_cities)
