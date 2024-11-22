from model.player import Player
from model.game import Game
from model.property import Property
from model.gameboard import Gameboard

def main():
    newgame = input("1. Start a new game?\n2. Load a saved game?\n")
    if newgame == "1":
        num_of_player = int(input("Please type the number of players:(2-6) "))
        while (num_of_player<2 or num_of_player>6):
            print("Please enter a valid number of players.(2-6)")
            num_of_player = int(input("Please type the number of players:(2-6) "))
        player_name = ["Player 1","Player 2","Player 3","Player 4","Player 5","Player 6"]
        player_names = []
        naming = input("Do you want to name your players?(y/n) ")
        while naming != "y" and naming != "n":
            naming = input("Please type 'y' or 'n': ")
        if naming == "y":
            for x in range(num_of_player):
                player_names.append(input("Please type the name of player "+str(x+1)+": "))
        else:
            for x in range(num_of_player):
                player_names.append(player_name[x])
        players = [Player(name) for name in player_names]
        game = Game(players)
    elif newgame == "2":
        game = Game([])
        game.load_game(input("Please type the name of the saved game: "))
        print("Game loaded successfully.")
    else:
        print("Please type 1 or 2.")
        main()

    
    GB = input("1. Use the default gameboard?\n2. Load a saved gameboard?\n3. Create a new gameboard?\n")
    while (GB != "1" and GB != "2"):
        print("Please type 1 or 2.")
        GB = input("1. Use the default gameboard?\n2. Load a saved gameboard?\n")
    if GB == "1":
        gameboard = Gameboard()
    elif GB == "2":
        game.load_gameboard(gameboard = input("Please type the name of the saved gameboard: "))
        print("Gameboard loaded successfully.")
    elif GB == "3":
        while True:
            gameboard.print_gameboard()
            choice = input("1.Add a property\n2.Remove a property\n3.print the gameboard\n4.Exit\n")
            if choice == "1":
                gameboard.add_property()
            elif choice == "2":
                gameboard.remove_property()
            elif choice == "3":
                gameboard.print_gameboard()
            elif choice == "4":
                return
            else:
                print("Please type 1, 2, 3 or 4.")

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

if __name__ == "__main__":
    main()