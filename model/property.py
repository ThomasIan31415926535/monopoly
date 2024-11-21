# model/property.py
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

    def buy(self, player):
        """Allows a player to buy the property if it's not already owned."""
        if self.owner is None:
            if player.money >= self.price:
                self.owner = player
                player.money -= self.price
                print(f"{player.name} bought {self.name} for HKD {self.price}.")
            else:
                print(f"{player.name} does not have enough money to buy {self.name}.")
        else:
            print(f"{self.name} is already owned by {self.owner.name}.")