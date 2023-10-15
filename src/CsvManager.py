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
            fieldnames = data[0].keys()  # Assumes all dictionaries have the same keys
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write the header (field names)
            csv_writer.writeheader()

            # Write the data
            csv_writer.writerows(data)
