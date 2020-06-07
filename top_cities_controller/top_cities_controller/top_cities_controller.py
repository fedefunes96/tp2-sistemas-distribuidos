from protocol.protocol import Protocol

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
        self.top_cities = sorted(
            self.cities_data,
            key=self.cities_data.get,
            reverse=True
        )[:3]

        print("Top cities are")
        print(self.top_cities)
