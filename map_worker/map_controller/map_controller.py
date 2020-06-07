from redirector.redirector import Redirector

class MapController(Redirector):
    def __init__(self, recv_queue, send_queue, master_send_queue, apply_func):
        self.apply_func = apply_func
        Redirector.__init__(self, recv_queue, send_queue, master_send_queue)

    def data_received(self, data):
        [date, latitude, longitude, result] = data.split(",")

        if result != "positivi":
            return

        place = self.apply_func(float(latitude), float(longitude))

        Redirector.data_received(self, place)
