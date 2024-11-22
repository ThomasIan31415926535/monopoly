# model/property.py
from .gameboard import Gameboard

class Property:
    def __init__(self, gameboard):
        self.name = gameboard.name
        self.price = gameboard.price
        self.rent = gameboard.rent
        self.owner = None
        self.ownedproperties = []
    
    def print_all_properties(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Rent: {self.rent}")
        print(f"Owner: {self.owner}")
        print("--------------------")