import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Stella", 3.00, 5)
        self.customer_1 = Customer("Bob", 100.00, 18)

    # START OF TESTS

    def test_customer_has_name(self):
        self.assertEqual("Bob", self.customer_1.name)

    def test_buy_drink(self):
        self.customer_1.buy_drink(self.drink_1)
        self.assertEqual(97, self.customer_1.wallet)

    def test_customer_has_age(self):
        self.assertEqual(18, self.customer_1.age)