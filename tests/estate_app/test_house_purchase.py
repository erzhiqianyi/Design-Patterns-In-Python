import unittest
from estate_app.house_purchase import HousePurchase


class HousePurchaseTestCase(unittest.TestCase):
    def test_house_purchase_prompt_init(self):
        init = HousePurchase.prompt_init()
        self.assertIsNotNone(init['square_feet'])
        self.assertIsNotNone(init['beds'])
        self.assertIsNotNone(init['baths'])
        self.assertTrue(init['fenced'] in ("yes", "no"))
        self.assertTrue(init['garage'] in ("attached", "detached", "none"))
        self.assertIsNotNone(init['num_stories'])
        self.assertIsNotNone(init['price'])
        self.assertIsNotNone(init['taxes'])

    def test_purchase_house(self):
        init = HousePurchase.prompt_init()
        house = HousePurchase(**init)
        house.display()


if __name__ == '__main__':
    unittest.main()
