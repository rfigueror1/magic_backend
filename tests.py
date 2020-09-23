# -*- coding: utf-8 -*-
import unittest
from utils import flatten_array


class TestCase(unittest.TestCase):
    """Functions unit tests"""

    # @unittest.skip('Already tested')
    def test_1_flatten_array(self):
        """ Test to verify first given input
        """
        arr = [[1, 2, [3]], 4]
        print("\n****************** Flatten Array - First Given Array *******************\n")
        flatten_result = flatten_array(arr)
        self.assertEqual(flatten_result, [1, 2, 3, 4])

    # @unittest.skip('Already tested')
    def test_2_flatten_array(self):
        """ Test to verify empty input
        """
        arr = []
        print("\n****************** Flatten Array - Empty Array *******************\n")
        flatten_result = flatten_array(arr)
        self.assertEqual(flatten_result, [])

    # @unittest.skip('Already tested')
    def test_3_flatten_array(self):
        """ Test to verify empty input
        """
        arr = [1, 2, 3, 4]
        print("\n****************** Flatten Array - Flat array *******************\n")
        flatten_result = flatten_array(arr)
        self.assertEqual(flatten_result, [1, 2, 3, 4])

    # @unittest.skip('Already tested')
    def test_4_flatten_array(self):
        """ Test to verify one-elemen input
        """
        arr = [1]
        print("\n****************** Flatten Array - One Element array *******************\n")
        flatten_result = flatten_array(arr)
        self.assertEqual(flatten_result, [1])


if __name__ == "__main__":
    unittest.main()