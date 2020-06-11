import csv
from protocol.protocol import Protocol

CHUNK_SIZE = 64

class ChunkManager:
    def __init__(self, queue_map, queue_date, queue_count):
        self.protocol = Protocol(queue_map, queue_date, queue_count)

    def process_data(self, route):
        with open(route) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                else:
                    date = row[0]
                    latitude = row[1]
                    longitude = row[2]
                    result = row[3]

                    line_count += 1
                    self.protocol.process(date, latitude, longitude, result)

        self.protocol.close()