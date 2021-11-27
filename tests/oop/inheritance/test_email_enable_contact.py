import unittest

from oop.inheritance.email_enable_contact import EmailEnableContact
from oop.inheritance.contact import Contact


class SendEmailTestCase(unittest.TestCase):
    def test_send_email(self):
        e = EmailEnableContact('John Smith', 'jsmith@example.net')
        e.send_mail("Hello,test e-mail here")
        self.assertEqual(len(Contact.all_contacts), 1)


if __name__ == '__main__':
    unittest.main()
