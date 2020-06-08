from redirector.redirector import Redirector

class DateRedirector(Redirector):
    def __init__(self, recv_queue, send_queue, master_send_queue):
        Redirector.__init__(self, recv_queue, send_queue, master_send_queue)

    def data_received(self, data):
        [date, latitude, longitude, result] = data.split(",")

        new_data = date + ',' + result

        Redirector.data_received(self, new_data)
