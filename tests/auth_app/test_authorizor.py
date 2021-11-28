import unittest
from auth_app.authorizor import Authorizor
from auth_app.authenticator import Authenticator
from auth_app.auth_exception import InvalidUsernameException
from auth_app.auth_exception import NotLoggedInException
from auth_app.auth_exception import NotPermittedException


class AddPermissionTestCase(unittest.TestCase):

    def setUp(self):
        authenticator = Authenticator()
        self.authorizor = Authorizor(authenticator)

    def test_add_permission(self):
        permission = 'view_all_users'
        self.authorizor.add_permission(permission)
        self.assertTrue(permission in self.authorizor.permission)

    def test_permission_exists(self):
        permission = 'view_all_users'
        self.authorizor.add_permission(permission)
        self.assertRaises(PermissionError, self.authorizor.add_permission, permission)


class PermitUserTestCase(unittest.TestCase):
    def setUp(self):
        authenticator = Authenticator()
        self.authorizor = Authorizor(authenticator)
        self.permission = 'view_all_users'
        self.authorizor.add_permission(self.permission)

    def test_permit_user(self):
        username = 'joe'
        password = 'password'
        self.authorizor.authenticator.add_user(username, password)
        self.authorizor.permit_user(self.permission, username)
        perm_set = self.authorizor.permission[self.permission]
        self.assertTrue(username in perm_set)

    def test_invalid_username(self):
        username = 'joe'
        self.assertRaises(InvalidUsernameException, self.authorizor.permit_user, self.permission, username)

    def test_permission_does_not_exist(self):
        username = 'joe'
        self.assertRaises(PermissionError, self.authorizor.permit_user, "wrong permission", username)


class CheckPermissionTestCase(unittest.TestCase):
    def setUp(self):
        authenticator = Authenticator()
        self.authorizor = Authorizor(authenticator)
        self.permission = 'view_all_users'
        self.authorizor.add_permission(self.permission)

    def test_check_permission(self):
        username = 'joe'
        password = 'password'
        self.authorizor.authenticator.add_user(username, password)
        self.authorizor.authenticator.login(username, password)
        self.authorizor.permit_user(self.permission, username)
        permitted = self.authorizor.check_permission(self.permission, username)
        self.assertTrue(permitted)

    def test_not_login(self):
        username = 'joe'
        password = 'password'
        self.authorizor.authenticator.add_user(username, password)
        self.assertRaises(NotLoggedInException, self.authorizor.check_permission, self.permission, username)

    def test_permission_does_not_exist(self):
        username = 'joe'
        password = 'password'
        self.authorizor.authenticator.add_user(username, password)
        self.authorizor.authenticator.login(username, password)
        self.assertRaises(PermissionError, self.authorizor.check_permission, "wrong permission", username)

    def test_not_permitted_exception(self):
        username = 'joe'
        password = 'password'
        self.authorizor.authenticator.add_user(username, password)
        self.authorizor.authenticator.login(username, password)
        self.assertRaises(NotPermittedException, self.authorizor.check_permission, self.permission, username)


if __name__ == '__main__':
    unittest.main()
