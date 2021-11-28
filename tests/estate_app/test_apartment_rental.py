import unittest
from estate_app.aprtment_rental import ApartmentRental


class HouseRentalTestCase(unittest.TestCase):
    def test_house_rental_prompt_init(self):
        init = ApartmentRental.prompt_init()
        self.assertIsNotNone(init['square_feet'])
        self.assertIsNotNone(init['beds'])
        self.assertIsNotNone(init['baths'])
        self.assertTrue(init['laundry'] in ("coin", "ensuite", "none"))
        self.assertTrue(init['balcony'] in ("yes", "no", "solarium"))
        self.assertIsNotNone(init['rent'])
        self.assertIsNotNone(init['utilities'])
        self.assertTrue(init['furnished'] in ("yes", "noe"))

    def test_rent_house(self):
        init = ApartmentRental.prompt_init()
        house = ApartmentRental(**init)
        house.display()


if __name__ == '__main__':
    unittest.main()
