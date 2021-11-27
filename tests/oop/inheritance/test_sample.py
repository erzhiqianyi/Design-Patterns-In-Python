import unittest

from oop.inheritance.sample import SubClass


class SubClassCallTestCase(unittest.TestCase):

    def test_sub_class_call(self):
        s = SubClass()
        s.call_me()
        self.assertEqual(s.num_sub_calls, 1)
        self.assertEqual(s.num_left_calls, 1)
        self.assertEqual(s.num_right_calls, 1)
        self.assertEqual(s.num_base_calls, 2)


if __name__ == '__main__':
    unittest.main()
