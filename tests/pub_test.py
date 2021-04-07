import unittest
from src.pub import Pub
from src.drink import Drink


class TestPub(unittest.TestCase):
    
    def setUp(self):
        drink_1 = Drink("old fashioned", 5.00)
        drink_2 = Drink("hophouse 13", 4.50)

        self.pub = Pub("The Prancing Pony", 100.00, [drink_1, drink_2])
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_drinks_list(self):
        self.assertEqual(list, type(self.pub.drinks_list))

    def test_sell_drink(self):
        self.pub.sell_drink(self.pub.drinks_list[0])
        self.assertEqual(105, self.pub.till)