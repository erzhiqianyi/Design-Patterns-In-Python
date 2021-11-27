import unittest
from notebook.menu import Menu
from pynput.keyboard import Key, Controller


class MenuRunTestCase(unittest.TestCase):

    def setUp(self):
        self.menu = Menu()
        self.keyboard = Controller()

    def test_run(self):
        self.menu.display_menu()


if __name__ == '__main__':
    unittest.main()
