from oop.inheritance.contact import Contact


class Supplier(Contact):

    def order(self, order):
        print("If this were a real system we would send " + self.name + " the " + order)
