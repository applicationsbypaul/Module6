import unittest

from more_functions.validate_input_in_functions import score_input


class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        self.assertEqual(score_input('Paul'), 'Paul: 0')

    # def test_score_input_test_score_valid(self):
    #    self.assertEqual(score_input('Paul', 78), False)

    # def test_score_input_test_score_below_range(self):
    #    self.assertEqual(score_input('Paul', -13), False)

    # def test_score_input_test_score_above_range(self):
    #    self.assertEqual(score_input('Paul', 101), False)

    # def test_test_score_non_numeric(self):
    #    self.assertEqual(score_input('Paul', 'a'), False)
    #    with self.assertRaises(ValueError):
    #        score_input('Paul', 'a')


if __name__ == '__main__':
    unittest.main()
