from auth_app.auth_exception import InvalidUsernameException
from auth_app.auth_exception import NotLoggedInException
from auth_app.auth_exception import NotPermittedException


class Authorizor:
    def __init__(self, authenticator):
        self.authenticator = authenticator
        self.permission = {}

    def add_permission(self, perm_name):
        """ Create  a new permission that users can be added to """
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            self.permission[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """ Grant the given permission to the user """
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsernameException(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInException(username)
        try:
            perm_set = self.permission[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedException(username)
            else:
                return True


