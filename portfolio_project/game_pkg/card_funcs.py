import random

# the following values are assigned 10 and listed as items within the deck.
J = 10
K = 10
Q = 10
A = 11  # 2 aces will be worth 11
a = 1  # 2 aces will be worth 1

deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7,
        7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, J, J, J, J, Q, Q, Q, Q, K, K, K, K, A, A, a, a]
# the conventional 52 card deck is converted to a string.

player_hand = []
cpu_hand = []
# the cpu hand and the player hand are both empty strings for now.


def reset_deck():
    deck.extend(player_hand)
    deck.extend(cpu_hand)
    player_hand.clear()
    cpu_hand.clear()
    shuffle_deck()
# a function to provide a clean deck and clear out each hand.


def shuffle_deck():
    random.shuffle(deck)
# shuffle deck function.


def player_choice():
    choice = input(
        "\nPress D to draw another card. \nPress F to fold. \nPress H to hold. ")
    player_total = sum(player_hand)
    if choice in ("D", "d"):
        print("You are dealt another card.")
        player_draw_card()
        if player_total == 21:
            print("You win!")
        elif player_total > 21:
            print("You broke! Better luck next time.")
    if choice in ("F", "f"):
        print("Sorry to see you go. Better luck next time.")
    if choice in ("H", "h"):
        print("You chose to hold. It is now the Dealer's turn.\n")
        cpu_deal()
# function to provide a choice for the player and the outcome of that choice.


def player_total_ops():
    player_total = sum(player_hand)
    if player_total > 21:
        print("You broke! Better luck next time.")
    elif player_total == 21:
        print("You win!")
    else:
        player_choice()
# function to add the total of the hand and base it off conditions to meet, otherwise, calling on the player_choice func.


def deal():
    print("\nLet's play!")
    print("\n The Dealer is shuffling the cards.")
    print("\nYou're dealt two cards.")
    random.shuffle(deck)
    new_card = random.choice(deck)
    deck.remove(new_card)
    player_hand.append(new_card)
    new_card = random.choice(deck)
    deck.remove(new_card)
    player_hand.append(new_card)
    print("\nYour hand:")
    print(*player_hand, sep=", ")
    player_total = sum(player_hand)
    print("\nThe sum of your cards is:", player_total)
    player_total_ops()
# func to deal the first two cards to the player and provide the details of what's in the player's hand.


def player_draw_card():
    random.shuffle(deck)
    # for item in deck:
    new_card = random.choice(deck)
    deck.remove(new_card)
    player_hand.append(new_card)
    print("\nYour hand:")
    print(*player_hand, sep=", ")
    player_total = sum(player_hand)
    print("The sum of your cards is:", player_total)
    player_total_ops()
# func to deal another card and provide the details of what's in the player's hand.


def cpu_deal():
    random.shuffle(deck)
    new_card = random.choice(deck)
    deck.remove(new_card)
    cpu_hand.append(new_card)
    new_card = random.choice(deck)
    deck.remove(new_card)
    cpu_hand.append(new_card)
    cpu_total = sum(cpu_hand)
    print("\nThe Dealer draws two cards.\n")
    print("The sum of the Dealer's cards is:", cpu_total)
    player_cpu_totals()
# func to deal two cards to the cpu and provide the player details of the sum.


def cpu_draw_card():
    random.shuffle(deck)
    new_card = random.choice(deck)
    deck.remove(new_card)
    cpu_hand.append(new_card)
    cpu_total = sum(cpu_hand)
    print("The sum of the Dealer's cards is:", cpu_total)
    player_cpu_totals()
# func to deal another card to the cpu and provide the player details of the sum.


def player_cpu_totals():
    player_total = sum(player_hand)
    cpu_total = sum(cpu_hand)
    if cpu_total < 14:
        print("\nThe Dealer is drawing another card.")
        cpu_draw_card()
    elif cpu_total == 21:
        print("The Dealer won!")
    elif cpu_total > 21:
        print("The Dealer broke! You won the game.")
    elif cpu_total == player_total:
        print("It's a draw!")
    elif cpu_total > player_total:
        print("The Dealer's hand beat your hand. You lost.")
    elif cpu_total < player_total:
        print("Your hand beat the Dealers hand. You won!")
# func to add the two hands up and compare them to see who won and who lost.
