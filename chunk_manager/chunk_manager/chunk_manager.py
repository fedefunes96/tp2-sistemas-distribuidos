import csv

CHUNK_SIZE = 64

class ChunkManager:
    def __init__(self, protocol):
        self.protocol = protocol

    def process_data(self, route):
        with open(route) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                    continue
                    #print(f'Column names are {", ".join(row)}')
                else:
                    date = row[0]
                    latitude = row[1]
                    longitude = row[2]
                    result = row[3]

                    line_count += 1
                    self.protocol.process(date, latitude, longitude, result)

        print("Everything sent")
        self.protocol.close()