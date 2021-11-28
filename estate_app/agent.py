from estate_app.utils import get_valid_input
from estate_app.aprtment_purchase import ApartmentPurchase
from estate_app.aprtment_rental import ApartmentRental
from estate_app.house_purchase import HousePurchase
from estate_app.house_rental import HouseRental


class Agent:

    def __init__(self):
        self.property_list = []
        self.type_map = {
            ('house', 'purchase'): HousePurchase,
            ('house', 'rental'): HouseRental,
            ('apartment', 'purchase'): ApartmentPurchase,
            ('apartment', 'rental'): ApartmentRental
        }

    def display_properties(self):
        for property in self.property_list:
            print(property)

    def add_property(self):
        property_type = get_valid_input("What type of property? ", ("house", "apartment")).lower()
        payment_type = get_valid_input("What payment type? ", ("purchase", "rental")).lower()
        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
