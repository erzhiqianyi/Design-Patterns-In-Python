import unittest

from estate_app.utils import get_valid_input


class GetValidInputTestCase(unittest.TestCase):

    def test_get_valid_input(self):
        furnished = get_valid_input("Is the property furnished? ", ("yes", "no"))
        self.assertTrue(furnished in ("yes", "no"))


if __name__ == '__main__':
    unittest.main()
