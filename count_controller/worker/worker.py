import csv
#from protocol.protocol import Protocol
from count_redirector.count_redirector import CountRedirector

class Worker:
    def __init__(self, recv_queue, send_queue, master_queue):
        #self.protocol = Protocol(
        #    recv_queue,
        #    send_queue,
        #    master_queue
        #)

        self.redirector = CountRedirector(
            recv_queue,
            send_queue,
            master_queue,
            self.data_received,
            self.no_more_data
        )

        self.total_deceduti = 0
        self.total_positivi = 0

    def start(self):
        #self.protocol.start_connection(self.data_received)
        self.redirector.start()

        #self.protocol.send_data(self.total_positivi, self.total_deceduti)
    
    def no_more_data(self):
        self.redirector.send_data(self.total_positivi, self.total_deceduti)

    def data_received(self, result):
        if result == "positivi":
            self.total_positivi += 1
        else:
            self.total_deceduti += 1
