class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExistsException(AuthException):
    pass


class PasswordTooShortException(AuthException):
    pass


class InvalidUsernameException(AuthException):
    pass


class InvalidPasswordException(AuthException):
    pass


class NotLoggedInException(AuthException):
    pass


class NotPermittedException(AuthException):
    pass
