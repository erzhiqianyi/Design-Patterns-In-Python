import unittest

from oop.inheritance.friend import Friend
from oop.inheritance.friend import CloseFriend


class CreateFriendTestCase(unittest.TestCase):
    def test_create_friend(self):
        phone = '123543343'
        f = Friend('John', 'john@example.net', phone)
        self.assertEqual(phone, f.phone)


class CreateCloseFriendTestCase(unittest.TestCase):

    def test_create_close_friend(self):
        name = 'John'
        email = 'john@example.net'
        phone = '123543343'
        street = 'street'
        city = 'city'
        state = 'state'
        code = 'code'
        f = CloseFriend(name, email, phone, street, city, state, code)
        self.assertEqual(f.name, name)
        self.assertEqual(f.email, email)
        self.assertEqual(f.street, street)
        self.assertEqual(f.city, city)
        self.assertEqual(f.state, state)
        self.assertEqual(f.code, code)


if __name__ == '__main__':
    unittest.main()
