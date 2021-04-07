import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Stella", 3.00, 5)
        self.customer_1 = Customer("Bob", 100.00, 18)
        self.customer_2 = Customer("Skint_Bob", 0.01, 20)
        self.pub = Pub("The Queen's Arms", 1000.00, [self.drink_1])

    # START OF TESTS

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.customer_1.name)

    def test_buy_drink_enough_money(self):
        self.customer_1.buy_drink(self.drink_1, self.pub)
        self.assertEqual(97, self.customer_1.wallet)

    def test_buy_drink_not_enough_money(self):
        self.customer_1.buy_drink(self.drink_1, self.pub)
        self.assertEqual(0.01, self.customer_2.wallet)

    def test_customer_has_age(self):
        self.assertEqual(18, self.customer_1.age)

    def test_increase_drunkenness(self):
        self.customer_1.increase_drunkenness(self.drink_1)
        self.assertEqual(5, self.customer_1.drunkenness)