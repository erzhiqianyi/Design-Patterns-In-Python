import unittest
from mail_list.mailing_list import MailingList


class SendMailTestCase(unittest.TestCase):

    def setUp(self):
        self.m = MailingList()
        self.m.add_to_group('friend1@example.com', 'friend')
        self.m.add_to_group('friend2@example.com', 'friend')
        self.m.add_to_group('family@example.com', 'family')
        self.m.add_to_group('prol@example.com', 'professional')

    def test_send_mailings(self):
        subject = 'A Party'
        message = 'Friends and family only: A Party'
        from_address = 'me@example.com'
        self.m.send_mailings(subject, message, from_address
                             , 'friend', 'family',
                             headers={"reply-to": "me@example.com"})


if __name__ == '__main__':
    unittest.main()
