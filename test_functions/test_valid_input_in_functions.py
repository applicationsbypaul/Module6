"""
Program: test_valid_input_in_functions.py
Author: Paul Ford
Last date modified: 06/17/2020
Purpose: test score input function
"""
import unittest

from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input('Paul'), 'Paul: 0')

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input('Paul', 78), 'Paul: 78')

    def test_score_input_test_score_below_range(self):
        with self.assertRaises(ValueError):
            score_input('Paul', -32)

    def test_score_input_test_score_above_range(self):
        with self.assertRaises(ValueError):
            score_input('Paul', 101)

    def test_test_score_non_numeric(self):
        with self.assertRaises(ValueError):
            score_input('Paul', 'a')

    def test_score_input_invalid_message(self):
        with self.assertRaises(ValueError):
            score_input('Paul', 'a', 'Test new message')


if __name__ == '__main__':
    unittest.main()
