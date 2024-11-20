import json
from .property import Property

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

    def save_gameboard(self, filename):
        """Saves the gameboard to a file."""
        with open(filename, 'w') as f:
            json.dump([{'name': p.name, 'price': p.price, 'rent': p.rent} if p else None for p in self.properties], f)

    def load_gameboard(self, filename):
        """Loads the gameboard from a file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.properties = [Property(d['name'], d['price'], d['rent']) if d else None for d in data]