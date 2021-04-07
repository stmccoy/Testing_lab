import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("old fashioned", 5.00, 40)
        self.drink_2 = Drink("hophouse 13", 4.50, 5)
        self.customer_1 = Customer("Fred", 50, 40)
        self.customer_2 = Customer("Jon", 20, 13)
        self.pub = Pub("The Prancing Pony", 100.00, [self.drink_1, self.drink_2])
    
    # START OF TESTS

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_drinks_list(self):
        self.assertEqual([self.drink_1, self.drink_2], self.pub.drinks_list)

    def test_sell_drink_overage(self):
        self.pub.sell_drink(self.drink_1, self.customer_1)
        self.assertEqual(105, self.pub.till)

    def test_sell_drink_underrage(self):
        self.pub.sell_drink(self.drink_1, self.customer_2)
        self.assertEqual(100, self.pub.till)
   
    def test_sell_drink_too_drunk(self):
        for _ in range(4):
            self.customer_1.buy_drink(self.drink_1, self.pub)
    
        self.assertEqual(115, self.pub.till)

    