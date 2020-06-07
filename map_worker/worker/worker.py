import csv
from map_controller.map_controller import MapController
from named_point.named_point import NamedPoint
from point.point import Point

class Worker:
    def __init__(self):
        self.map_controller = MapController(
            "map_city",
            "cities_resume",
            "master_map",
            self.process_data
        )
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

        self.map_controller.start()

    def process_data(self, latitude, longitude):
        point = Point(longitude, latitude)

        return point.closest_point(self.places).name        
