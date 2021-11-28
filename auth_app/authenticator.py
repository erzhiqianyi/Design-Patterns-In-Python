from auth_app.auth_exception import UsernameAlreadyExistsException
from auth_app.auth_exception import PasswordTooShortException
from auth_app.auth_exception import InvalidPasswordException
from auth_app.auth_exception import InvalidUsernameException

from auth_app.user import User


class Authenticator:
    def __init__(self):
        """ Construct  an authenticator to manage  users logging in and out. """
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExistsException(username)

        if len(password) < 6:
            raise PasswordTooShortException(username)

        self.users[username] = User(username, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsernameException(username)

        if not user.check_password(password):
            raise InvalidPasswordException(username, user)

        user.is_logged = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged
        return False


