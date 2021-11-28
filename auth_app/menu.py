from auth_app.authorizor import Authorizor
from auth_app.authenticator import Authenticator
from auth_app.auth_exception import InvalidUsernameException
from auth_app.auth_exception import InvalidPasswordException
from auth_app.auth_exception import NotLoggedInException
from auth_app.auth_exception import NotPermittedException

# set up a test user and permission
authenticator = Authenticator()
authorizor = Authorizor(authenticator)

authenticator.add_user('joe', 'joepassword')
authorizor.add_permission('test program')
authorizor.add_permission('change program')
authorizor.permit_user('test program', 'joe')


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            'login': self.login,
            'test': self.test,
            'change': self.change,
            'quit': self.quit
        }

    def login(self):
        logged_in = False
        while not logged_in:
            username = input('username: ')
            password = input('password: ')
            try:
                logged_in = authenticator.login(username, password)
            except InvalidUsernameException:
                print("Sorry ,that username does not exist")
            except InvalidPasswordException:
                print("Sorry, incorrect password")
            else:
                self.username = username

    def is_permitted(self, permission):
        try:
            authorizor.check_permission(permission, self.username)
        except NotLoggedInException as e:
            print("{} is not logged in".format(e.username))
            return False
        except NotPermittedException as e:
            print("{} can not {}".format(e.username, permission))
            return False
        else:
            return True

    def test(self):
        if self.is_permitted('test program'):
            print("Testing program now")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now")

    def quit(self):
        raise SystemExit()

    def menu(self):
        try:
            answer = ''
            while True:
                print("""Please enter a command:
                login Login
                test Test the Program
                change change the program
                quit Quit""")
                answer = input('enter a command: ').lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the program")


if __name__ == '__main__':
    editor = Editor()
    editor.menu()
