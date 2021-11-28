import unittest
from auth_app.user import User


class UserTestCase(unittest.TestCase):
    def test_create_user(self):
        username = 'username'
        password = 'password'
        user = User(username, password)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)
        self.assertNotEqual(user.password, password)
        self.assertTrue(user.check_password(password))


if __name__ == '__main__':
    unittest.main()
