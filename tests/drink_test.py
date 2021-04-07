import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):

        self.drink_1 = Drink("Guinness", 4.75)

    # START OF TESTS

    def test_drink_has_name(self):
        self.assertEqual("Guinness", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.75, self.drink_1.price)