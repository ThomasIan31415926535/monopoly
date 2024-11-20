class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0
        self.in_jail = False
        self.jail_turns = 0

    def move(self, spaces):
        self.position = (self.position + spaces) % 20
        if self.position == 0:
            self.money += 1500  # Salary for passing Go
            print(f"{self.name} passed Go and received HKD 1500.")
