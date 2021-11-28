import unittest
from estate_app.aprtment_purchase import ApartmentPurchase


class HousePurchaseTestCase(unittest.TestCase):
    def test_house_purchase_prompt_init(self):
        init = ApartmentPurchase.prompt_init()
        self.assertIsNotNone(init['square_feet'])
        self.assertIsNotNone(init['beds'])
        self.assertIsNotNone(init['baths'])
        self.assertTrue(init['laundry'] in ("coin", "ensuite", "none"))
        self.assertTrue(init['balcony'] in ("yes", "no", "solarium"))
        self.assertIsNotNone(init['price'])
        self.assertIsNotNone(init['taxes'])

    def test_purchase_house(self):
        init = ApartmentPurchase.prompt_init()
        house = ApartmentPurchase(**init)
        house.display()


if __name__ == '__main__':
    unittest.main()