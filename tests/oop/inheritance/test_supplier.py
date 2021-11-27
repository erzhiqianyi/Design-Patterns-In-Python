import unittest
from oop.inheritance.supplier import Supplier


class OrderTestCase(unittest.TestCase):
    def test_order(self):
        s = Supplier('Supplier', 'Supplier@example.net')
        s.order("I need pliers")


if __name__ == '__main__':
    unittest.main()
