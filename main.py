from model.player import Player
from model.game import Game
from model.property import Property
from model._init_ import _init_

if __name__ == "__main__":
    num_of_player = input("Please type the number of players:(2-6) ")
    while (num_of_player<2 or num_of_player>6):
        print("Please enter a valid number of players.(2-6)")
        num_of_player = input("Please type the number of players:(2-6) ")
    player_name = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6"]
    player_names = []
    for x in range(num_of_player):
        player_names[x] = player_name[x]
    players = [Player(name) for name in player_names]
    game = Game(players)

 # Game loop (simplified)
while not game.check_game_over():
    game.play_turn()

    # Print the winner
winners = game.determine_winner()
if winners:
    winner_names = ", ".join(winner.name for winner in winners)
    max_money = winners[0].money  # All winners have the same amount
    print(f"The winner(s): {winner_names} with HKD {max_money}.")
else:
    print("No winners, the game ended without any remaining players.")

    # Print the final player status
for player in game.players:
    print(f"{player.name} has HKD {player.money}.")