import unittest
from mail_list.mail_sender import send_email


class HtmlLinkCollectorTestCase(unittest.TestCase):

    def test_send_mail(self):
        subject = 'A model subject'
        message = 'The message contents'
        from_address = 'from@example.com'
        to_address = 'to@exmaple.com'
        send_email(subject,message,from_address,to_address)


if __name__ == '__main__':
    unittest.main()
