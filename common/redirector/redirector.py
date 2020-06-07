from redirector.protocol.protocol import Protocol

class Redirector:
    def __init__(self, recv_queue, send_queue, master_send_queue):
        self.protocol = Protocol(recv_queue, send_queue, master_send_queue)

    def start(self):
        self.protocol.start_connection(self.data_received)

    def data_received(self, data):
        self.redirect_data(data)

    def redirect_data(self, data):
        self.protocol.send_data(data)
