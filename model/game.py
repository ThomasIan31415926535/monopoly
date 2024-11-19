import random
from .property import Property
from .player import Player
import json

class Game:
    def __init__(self, players):
        self.players = players
        self.properties = self.initialize_properties()
        self.current_player_index = 0
        self.rounds = 0

    def initialize_properties(self):
        return [
            None,  # Square 0: Go
            Property("Central", 800, 90),
            Property("Wan Chai", 700, 65),
            None,  # Income Tax
            Property("Stanley", 600, 60),
            None, #In jail/Just Visiting
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
            None,  #Chance
            Property("Tai O", 600, 25)
        ]

    def next_player(self):
        return self.players[self.current_player_index]

    def play_turn(self):
        player = self.next_player()
        if player.in_jail:
           if player.jail_turns < 3:
              print(f"{player.name} is in jail. Turn {player.jail_turns + 1}.")
              if player.jail_turns >= 1:
                decision = input("Type 'pay' to pay the fine or 'roll' to roll the dice: ").strip().lower()
                if decision == 'pay':
                    if player.money >= 150:
                       player.money -= 150
                       player.in_jail = False
                       print(f"{player.name} paid HKD 150 to get out of jail.")
                    else:
                       print(f"{player.name} does not have enough money to pay the fine.")
                    return
                else:
                     roll1, roll2 = random.randint(1, 4), random.randint(1, 4)
                     roll = roll1 + roll2
                     if roll1 == roll2:
                      player.in_jail = False
                      player.position = (player.position + roll) % len(self.properties)
                      print(f"{player.name} rolled doubles! They move to {player.position}.")
                     else:
                      player.jail_turns += 1
                if player.jail_turns == 3:
                    print(f"{player.name} did not roll doubles in three turns and pays HKD 150 to get out of jail.")
                    player.money -= 150
                    player.in_jail = False
                    player.position = (player.position + roll) % len(self.properties)
                    print(f"{player.name} moves to {player.position}.")
                else:
                    print(f"{player.name} did not roll doubles. They remain in jail for another turn.")
                    return

        # If not in jail, roll the dice
        roll = sum(random.randint(1, 4) for _ in range(2))  # Roll 2 tetrahedral dice
        start_position = player.position
        player.move(roll)
        current_position = player.position
        # Move the player
        print(f"{player.name} rolls {roll} and moves from {start_position}th Square to {current_position}th Square ")
        self.handle_square_action(player)

        if player.money < 0:
            print(f"{player.name} is bankrupt and out of the game.")
            self.players.remove(player)

        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.rounds += 1

    def handle_square_action(self, player):
        
        if player.position < 0 or player.position >= len(self.properties):
           print(f"Resetting to GO e.g 0th square.")
           player.position = 0  # Reset to a valid position or handle as needed

        square = self.properties[player.position]
    
    
        if player.position in [8, 12, 18]:  # 9th, 13th, and 19th squares
            self.handle_chance(player)
            return  # Exit after handling chance
        
        if player.position == 15:  # Go to jail square 
            print(f"{player.name} landed on Go to Jail! They go directly to Jail.")
            player.position == 6  # Move to Jail (6th square)
            player.in_jail = True  # Set the player as in jail
            player.jail_turns = 0  # Reset jail turn counter
            self.handle_Go_to_Jail(player)
            return  # Exit after handling chance

        # Income tax square at position 3 (0-indexed)
        if player.position == 3:  # 4th square
            self.handle_income_tax(player)
            return  # Exit after handling tax
        
        if player.position == 10:  # 11th square
            print(f"{player.name} landed on Free Parking. No effect.")
            return  # Exit without any effect
        
        if player.position == 5:  # 6th square
            print(f"{player.name} landed on In Jail/Just Visiting. No effect.")
            return  # Exit without any effect


        if isinstance(square, Property):
            if square.owner is None:
                print(f"{player.name} landed on {square.name}. Do you want to buy it for HKD {square.price}?")
                 # Input handling for the player's decision
                decision = input().strip().lower()
                if decision == 'yes':
                    if player.money >= square.price:
                       player.money -= square.price  # Deduct the price from the player's money
                       square.owner = player  # Set the player as the owner of the square
                       print(f"{player.name} bought {square.name} for HKD {square.price}. Remaining money: HKD {player.money}.")
                    else:
                       print(f"{player.name} does not have enough money to buy {square.name}.")
                elif decision == 'no':
                    print(f"{player.name} decided not to buy {square.name}.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            else:
                player.money -= square.rent
                print(f"{player.name} landed on {square.name}, which is owned by {square.owner.name}. Pay rent of HKD {square.rent}.Remaining money: {player.money} HKD")
                
    def save_game(self, filename):
        with open(filename, 'w') as f:
            json.dump({
                'players': [{'name': p.name, 'money': p.money, 'position': p.position, 'in_jail': p.in_jail}
                            for p in self.players],
                'current_player_index': self.current_player_index,
                'rounds': self.rounds
            }, f)


    def handle_chance(self, player):
        # Chance logic: gain or lose a random amount
        amount = random.randint(1, 20) * 10  # Random amount between 10 and 200
        if random.choice([True, False]):  # Randomly decide to gain or lose
            player.money += amount
            print(f"{player.name} gained HKD {amount} from Chance! Current money: HKD {player.money}.")
        else:
            player.money -= amount
            print(f"{player.name} lost HKD {amount} from Chance! Current money: HKD {player.money}.")

    def handle_income_tax(self, player):
        tax_amount = (player.money // 10) * 10  # Round down to nearest multiple of 10
        player.money -= tax_amount
        print(f"{player.name} pays HKD {tax_amount} in income tax. Remaining money: HKD {player.money}.")

    
    def load_game(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.players = [Player(p['name']) for p in data['players']]
            for p, d in zip(self.players, data['players']):
                p.money = d['money']
                p.position = d['position']
                p.in_jail = d['in_jail']
            self.current_player_index = data['current_player_index']
            self.rounds = data['rounds']

    def check_game_over(self):
        # Check for players with money left
        active_players = [p for p in self.players if p.money > 0]
        
        if len(active_players) <= 1 or self.rounds >= 100:
            return True
        return False
    
    def determine_winner(self):
        max_money = max(player.money for player in self.players)
        winners = [player for player in self.players if player.money == max_money]
        return winners
    