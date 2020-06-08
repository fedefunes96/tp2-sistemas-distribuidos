import csv
from protocol.protocol import Protocol

class Worker:
    def __init__(self, recv_queue, send_queue, master_queue):
        self.protocol = Protocol(
            recv_queue,
            send_queue,
            master_queue
        )

        self.total_deceduti = 0
        self.total_positivi = 0

    def start(self):
        self.protocol.start_connection(self.data_received)

        self.protocol.send_data(self.total_positivi, self.total_deceduti)
    
    def data_received(self, result):
        if result == "positivi":
            self.total_positivi += 1
        else:
            self.total_deceduti += 1
