import csv

class TemperaturesHandler:

    def __init__(self, filename):
        self.temperatures = self.import_temperatures(filename)

    def import_temperatures(self, filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            temperatures = list(reader)
        return temperatures

    # Part 1
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

    #Part 2
    def largest_fluctuation_station(self, ranges=None):
        """
            I: list
            O: tuple
        """
        # sort by station depending on ranges
        if ranges:
            temperatures_by_sorted_station = sorted(ranges, key=lambda x: int(x[0]))
        else:
            temperatures_by_sorted_station = sorted(self.temperatures[1:], key=lambda x: int(x[0]))
        max_total_fluct = 0
        temp_total_fluct = 0
        fluct_station = None
        for i in range(1, len(temperatures_by_sorted_station)):
            if temperatures_by_sorted_station[i][0] != temperatures_by_sorted_station[i - 1][0]:
                if temp_total_fluct > max_total_fluct:
                    max_total_fluct = temp_total_fluct
                    fluct_station = temperatures_by_sorted_station[i - 1][0]
                temp_total_fluct = 0
            else:
                temp_total_fluct += abs(float(temperatures_by_sorted_station[i][2]) - float(temperatures_by_sorted_station[i - 1][2]))
        return fluct_station, max_total_fluct

    # Part 3
    def largest_fluctuation_station_by_dates(self, range_dates):
        """
            I: list
            O: tuple
        """
        # filter by dates
        temperatures_by_dates = [x for x in self.temperatures[1:] if (range_dates[0] <= float(x[1]) <= range_dates[1])]
        station_result = self.largest_fluctuation_station(temperatures_by_dates)
        return station_result



if __name__ == "__main__":
    temp_handler = TemperaturesHandler('data.csv')
    res = temp_handler.largest_fluctuation_station_by_dates([2000.000, 2002.000])
    print(res)
    new_temphandler = TemperaturesHandler('./tests/data2.csv')
    res = new_temphandler.largest_fluctuation_station_by_dates([2000.000, 2002.000])
    print(res)

