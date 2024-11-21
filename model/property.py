# model/property.py
class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None
        self.ownedproperties = []
    
    def print_all_properties(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Rent: {self.rent}")
        print(f"Owner: {self.owner}")
        print("--------------------")