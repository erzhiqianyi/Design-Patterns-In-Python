import unittest
from error.EvenOnly import EvenOnly


class ExceptionTestCase(unittest.TestCase):

    def setUp(self):
        self.even = EvenOnly()

    def test_type_error(self):
        self.assertRaises(TypeError, self.even.append("2"))

    def test_value_error(self):
        self.assertRaises(TypeError, self.even.append(3))

    def test_append(self):
        self.even.append(2)

if __name__ == '__main__':
    unittest.main()
