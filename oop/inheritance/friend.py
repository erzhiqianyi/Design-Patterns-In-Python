from oop.inheritance.contact import Contact
from oop.inheritance.address_holder import AddressHolder


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class CloseFriend(Contact, AddressHolder):

    def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
