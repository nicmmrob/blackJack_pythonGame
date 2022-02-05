from game_pkg import card_funcs
# importing the functions to the app


class User:
    def __init__(self, name):
        self.name = name
# created a class for the user name for my own practice using classes, though I know there's much simpler ways to go about Player Name.


while True:
    # this will reset the deck every time the loop is run.
    card_funcs.reset_deck()
    print("\n-------------  BLACK JACK  -------------      ")
    print("  1.  Play Game         2.  Quit Game       \n")
    menu = input("Press 1 to play or press any other key to quit: ")
    if menu == "1":
        user_name = input("Please enter your player name: ")
        player1 = User(user_name)
        # welcome message calling on the player1 object with User class.
        print(f"\nWelcome, {player1.name}!")
    else:
        print("\nGoodbye.")
        break

    card_funcs.deal()  # initiates the game play.
