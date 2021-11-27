import unittest
from oop.inheritance.contact import Contact


class SearchContactTestCase(unittest.TestCase):
    def test_search(self):
        c1 = Contact('John A', 'Johna@example.net')
        c2 = Contact('John B', 'Johnb@example.net')
        c3 = Contact('Jenna C', 'Johnc@exmpale.net')
        john_contacts_name = ['John A', 'John B']
        search_john_result = [c.name for c in Contact.all_contacts.search('John')]
        self.assertEqual(john_contacts_name, search_john_result)


if __name__ == '__main__':
    unittest.main()
