from model import Player, Game

if __name__ == "__main__":
    print("Please type the number of players: ")
    player_names = ["Alice", "Bob", "Charlie"]
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

