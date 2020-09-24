# -*- coding: utf-8 -*-
import unittest
from flatten_array import flatten_array
from Temperatures import TemperaturesHandler


class TestCase(unittest.TestCase):
    """Functions unit tests"""

    @classmethod
    def setUpClass(cls):
        """Class configuration method
        """
        # Create Temperature Handlers
        cls.firstTempHandler = TemperaturesHandler('data.csv')
        cls.secondTempHandler = TemperaturesHandler('./tests/data2.csv')

    # @unittest.skip('Already tested')
    def test_1_flatten_array(self):
        """ Test to verify first given input
        """
        arr = [[1, 2, [3]], 4]
        print("\n****************** Flatten Array - First Given Array *******************\n")
        flatten_result = flatten_array(arr)
        print(flatten_result)
        self.assertEqual(flatten_result, [1, 2, 3, 4])

    # @unittest.skip('Already tested')
    def test_2_flatten_array(self):
        """ Test to verify empty input
        """
        arr = []
        print("\n****************** Flatten Array - Empty Array *******************\n")
        flatten_result = flatten_array(arr)
        print(flatten_result)
        self.assertEqual(flatten_result, [])

    # @unittest.skip('Already tested')
    def test_3_flatten_array(self):
        """ Test to verify empty input
        """
        arr = [1, 2, 3, 4]
        print("\n****************** Flatten Array - Flat array *******************\n")
        flatten_result = flatten_array(arr)
        print(flatten_result)
        self.assertEqual(flatten_result, [1, 2, 3, 4])

    # @unittest.skip('Already tested')
    def test_4_flatten_array(self):
        """ Test to verify one-elemen input
        """
        arr = [1]
        print("\n****************** Flatten Array - One Element array *******************\n")
        flatten_result = flatten_array(arr)
        print(flatten_result)
        self.assertEqual(flatten_result, [1])

    # @unittest.skip('Already tested')
    def test_5_part1_temperatures(self):
        """ Test to verify part 1 of temperatures problem using all data
        """
        print("\n****************** Temperatures - Lowest Temperature - All Data *******************\n")
        lowest_temperature = self.firstTempHandler.lowest_temperature()
        print(lowest_temperature)
        self.assertEqual(lowest_temperature[2], '-72.932')

    # @unittest.skip('Already tested')
    def test_6_part2_temperatures(self):
        """ Test to verify part 2 of temperatures problem using all data
        """
        print("\n****************** Temperatures - Largest Fluctuation - All Data *******************\n")
        largest_fluctuation = self.firstTempHandler.largest_fluctuation_station()
        print(largest_fluctuation)
        self.assertEqual(largest_fluctuation, ('735181', 2742.2999999999993))

    # @unittest.skip('Already tested')
    def test_6_part3_temperatures(self):
        """ Test to verify part 3 of temperatures problem using all data
        """
        print("\n****************** Temperatures - Largest Fluctuation between dates - All Data *******************\n")
        largest_fluctuation_dates = self.secondTempHandler.largest_fluctuation_station_by_dates([2000.000, 2002.000])
        print(largest_fluctuation_dates)
        self.assertEqual(largest_fluctuation_dates, ('68', 46.7))


if __name__ == "__main__":
    unittest.main()
