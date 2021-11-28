import unittest
from estate_app.house_rental import HouseRental


class HouseRentalTestCase(unittest.TestCase):
    def test_house_rental_prompt_init(self):
        init = HouseRental.prompt_init()
        self.assertIsNotNone(init['square_feet'])
        self.assertIsNotNone(init['beds'])
        self.assertIsNotNone(init['baths'])
        self.assertTrue(init['fenced'] in ("yes", "no"))
        self.assertTrue(init['garage'] in ("attached", "detached", "none"))
        self.assertIsNotNone(init['num_stories'])
        self.assertIsNotNone(init['rent'])
        self.assertIsNotNone(init['utilities'])
        self.assertTrue(init['furnished'] in ("yes", "noe"))

    def test_rent_house(self):
        init = HouseRental.prompt_init()
        house = HouseRental(**init)
        house.display()


if __name__ == '__main__':
    unittest.main()
