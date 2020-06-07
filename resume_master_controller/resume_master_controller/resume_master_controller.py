from protocol.protocol import Protocol

class ResumeMasterController:
    def __init__(self, recv_queue, send_queue):
        self.protocol = Protocol(recv_queue, send_queue)

    def start(self):
        self.protocol.start_connection()
        print("Is this ever called?")
