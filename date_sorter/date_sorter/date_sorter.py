from protocol.protocol import Protocol
from collections import OrderedDict

class DateSorter:
    def __init__(self, recv_queue, send_queue):
        self.protocol = Protocol(recv_queue, send_queue)
        self.date_data = OrderedDict()

    def start(self):
        self.protocol.start_connection(self.data_read)

        self.process_results()

    def data_read(self, data):
        self.date_data.update(sorted(data.items()))
    
    def process_results(self):
        print(self.date_data)

        self.protocol.send_data(self.date_data)
