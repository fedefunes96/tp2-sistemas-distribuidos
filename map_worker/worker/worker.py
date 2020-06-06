import csv
from protocol.protocol import Protocol
from named_point.named_point import NamedPoint
from point.point import Point

class Worker:
    def __init__(self):
        self.protocol = Protocol()
        self.places = []

    def start(self, route):
        with open(route) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    point = NamedPoint(row[0], float(row[2]), float(row[1]))
                    self.places.append(point)
                    line_count += 1

        self.protocol.start_connection(self.data_read, self.eof_read)

    def data_read(self, date, latitude, longitude, result):
        point = Point(longitude, latitude)

        closest_place = point.closest_point(self.places).name

        self.protocol.send_located_data(date, closest_place, result)
    
    def eof_read(self):
        self.protocol.send_ended()
