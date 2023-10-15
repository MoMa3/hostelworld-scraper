import csv


class CSVHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self):
        data = []
        with open(self.file_name, "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                data.append(row)
        return data

    def write_csv(self, data):
        with open(self.file_name, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(data)
