class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def buy_drink(self, drink, pub):
        if self.wallet >= drink.price:
            pub.sell_drink(drink, self)
            self.wallet -= drink.price
            self.increase_drunkenness(drink)

    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level
        



