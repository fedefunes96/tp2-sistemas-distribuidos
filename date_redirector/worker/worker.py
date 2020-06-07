import csv
from protocol.protocol import Protocol
from named_point.named_point import NamedPoint
from point.point import Point

class Worker:
    def __init__(self):
        self.protocol = Protocol()
        self.places = []

    def start(self, route):
        self.protocol.start_connection(self.data_read, self.eof_read)

    def data_read(self, date, latitude, longitude, result):
        point = Point(longitude, latitude)

        closest_place = point.closest_point(self.places).name

        self.protocol.send_located_data(date, closest_place, result)
    
    def eof_read(self):
        self.protocol.send_ended()
