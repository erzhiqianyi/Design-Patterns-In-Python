import unittest
from auth_app.authenticator import Authenticator

from auth_app.auth_exception import UsernameAlreadyExistsException
from auth_app.auth_exception import PasswordTooShortException
from auth_app.auth_exception import InvalidUsernameException
from auth_app.auth_exception import InvalidPasswordException


class AddUserTestCase(unittest.TestCase):
    def setUp(self):
        self.authenticator = Authenticator()

    def test_add_user(self):
        username = 'test_user'
        password = 'test_password'
        self.authenticator.add_user(username, password)
        user = self.authenticator.users[username]
        self.assertIsNotNone(user)

    def test_user_already_exists(self):
        username = 'test_user'
        password = 'test_password'
        self.authenticator.add_user(username, password)
        self.assertRaises(UsernameAlreadyExistsException, self.authenticator.add_user, username, password)

    def test_password_too_short(self):
        username = 'test_user'
        password = 'test'
        self.assertRaises(PasswordTooShortException, self.authenticator.add_user, username, password)


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.authenticator = Authenticator()
        self.username = "test_user"
        self.password = "test_password"
        self.authenticator.add_user(self.username, self.password)

    def test_login(self):
        self.authenticator.login(self.username, self.password)
        is_logged_in = self.authenticator.is_logged_in(self.username)
        self.assertTrue(is_logged_in)

    def test_invalid_username(self):
        self.assertRaises(InvalidUsernameException, self.authenticator.login, 'test', self.password)

    def test_invalid_password(self):
        self.assertRaises(InvalidPasswordException, self.authenticator.login, self.username, 'test')


class IsLoginTestCase(unittest.TestCase):
    def setUp(self):
        self.authenticator = Authenticator()
        self.username = "test_user"
        self.password = "test_password"
        self.authenticator.add_user(self.username, self.password)

    def test_is_login(self):
        self.authenticator.login(self.username, self.password)
        is_login = self.authenticator.is_logged_in(self.username)
        self.assertTrue(is_login)

    def test_is_not_login(self):
        is_login = self.authenticator.is_logged_in(self.username)
        self.assertFalse(is_login)


if __name__ == '__main__':
    unittest.main()
