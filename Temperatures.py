import csv

class TemperaturesHandler:

    def __init__(self):
        self.temperatures = self.import_temperatures()

    def import_temperatures(self):
        with open('data.csv', newline='') as f:
            reader = csv.reader(f)
            temperatures = list(reader)
        return temperatures

    def lowest_temperature(self):
        """
            I: list
            O: tuple
        """
        min_temperature = float("inf")
        min_element = None
        for i in range(1, len(self.temperatures)):
            temperature = float(self.temperatures[i][2])
            if temperature < min_temperature:
                min_temperature = temperature
                min_element = self.temperatures[i]
        return min_element