class Pub:
    def __init__(self, name, till, drinks_list):
        self.name = name
        self.till = till
        self.drinks_list = drinks_list

    def sell_drink(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness <100:
            self.till += drink.price