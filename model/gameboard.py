import json


class Property:
    def __init__(self, gameboard):
        self.name = gameboard.name
        self.price = gameboard.price
        self.rent = gameboard.rent
        self.owner = None
    
    def print_all_properties(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Rent: {self.rent}")
        print(f"Owner: {self.owner}")
        print("--------------------")

class Gameboard:
    def __init__(self):
        self.properties = []

    

    def create_gameboard(self):
        """Creates a new gameboard with properties."""
        self.properties = [
            None,  # Square 0: Go
            Property("Central", 800, 90),
            Property("Wan Chai", 700, 65),
            None,  # Income Tax
            Property("Stanley", 600, 60),
            None,  # In jail/Just Visiting
            Property("Shek O", 400, 10),
            Property("Mong Kok", 500, 40),
            None,  # Chance
            Property("Tsing Yi", 400, 15),
            None,  # Free Parking
            Property("Shatin", 700, 75),
            None,  # Chance
            Property("Tuen Mun", 400, 20),
            Property("Tai Po", 500, 25),
            None,  # Go to Jail
            Property("Sai Kung", 400, 10),
            Property("Yuen Long", 400, 25),
            None,  # Chance
            Property("Tai O", 600, 25)
        ]

    def edit_gameboard(self):
        """Allows the user to modify the gameboard properties."""
        for i, property in enumerate(self.properties):
            if property:
                print(f"Square {i}: {property.name} (Price: {property.price}, Rent: {property.rent}, Owner: {property.owner})")
                modify = input("Do you want to modify this property? (y/n) ")
                if modify == "y":
                    new_name = input("Enter the new name: ")
                    new_price = input("Enter the new price: ")
                    new_rent = input("Enter the new rent: ")
                    property.name = new_name
                    property.price = int(new_price)
                    property.rent = int(new_rent)
            else:
                print(f"Square {i}: Empty")
                add = input("Do you want to add a property to this square? (y/n) ")
                if add == "y":
                    new_name = input("Enter the new name: ")
                    new_price = input("Enter the new price: ")
                    new_rent = input("Enter the new rent: ")
                    self.properties[i] = Property(new_name, new_price, new_rent)

    def add_property(self, name, price, rent):
        """Adds a new property to the gameboard."""
        self.properties.append(Property(name, price, rent))

    def remove_property(self, index):
        """Removes a property from the gameboard."""
        self.properties.pop(index)

    def print_gameboard(self):
        """Prints the gameboard."""
        for i, property in enumerate(self.properties):
            if property:
                print(f"Square {i}: {property.name} (Price: {property.price}, Rent: {property.rent}, Owner: {property.owner})")
            else:
                print(f"Square {i}: Empty")

    def save_gameboard(self, filename):
        """Saves the gameboard to a file."""
        with open("GB_"+filename, 'w') as f:
            json.dump([{'name': p.name, 'price': p.price, 'rent': p.rent} if p else None for p in self.properties], f)

    def load_gameboard(self, filename):
        """Loads the gameboard from a file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.properties = [Property(d['name'], d['price'], d['rent']) if d else None for d in data]

    def create_game(self):
        """Creates a new game."""
        self.create_gameboard()
        self.load_gameboard('gameboard.json')