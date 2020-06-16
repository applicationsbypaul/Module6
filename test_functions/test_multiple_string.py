"""
Program: test_multiple_string.py
Author: Paul Ford
Last date modified: 06/16/2020
Purpose: test multiple_string function.
"""
import unittest

from more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(multiply_string('Paul', 3), 'PaulPaulPaul')

    def test_multiple_string1(self):
        self.assertEqual(multiply_string('Amy', 8), 'AmyAmyAmyAmyAmyAmyAmyAmy')

    def test_multiple_string2(self):
        self.assertEqual(multiply_string('Trevor', 2), 'TrevorTrevor')


if __name__ == '__main__':
    unittest.main()
