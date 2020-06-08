from protocol.protocol import Protocol

class Worker:
    def __init__(self, recv_queue, send_queue, master_queue):
        self.protocol = Protocol(
            recv_queue,
            send_queue,
            master_queue
        )
        #self.positives_per_date = {}
        #self.deceased_per_date = {}
        self.results_per_date = {}

    def start(self):
        self.protocol.start_connection(self.data_read)

        self.process_results()

    def data_read(self, date, result):
        if date not in self.results_per_date:
            self.results_per_date[date] = [0, 0]
        
        if result == "positivi":
            self.results_per_date[date][0] += 1
        else:
            self.results_per_date[date][1] += 1
        '''if result == "positivi":
            if date not in self.positives_per_date:
                self.positives_per_date[date] = 0
            
            self.positives_per_date[date] += 1
        else:
            if date not in self.deceased_per_date:
                self.deceased_per_date[date] = 0
            
            self.deceased_per_date[date] += 1 '''
    
    def process_results(self):
        #self.protocol.send_data(self.positives_per_date, self.deceased_per_date)
        print("DATES RESUME: Sending results")
        self.protocol.send_data(self.results_per_date)
