from oop.inheritance.contact import Contact
from oop.inheritance.mail_sender import MailSender


class EmailEnableContact(Contact, MailSender):
    pass

