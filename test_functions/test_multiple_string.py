import unittest

from more_functions.string_functions import multiply_string


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(multiply_string('Paul', 3), 'PaulPaulPaul}')


if __name__ == '__main__':
    unittest.main()
