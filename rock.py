import random

print("Rock Paper Scissors")

# list of words
list_of_words = '''rock paper scissors'''
list_of_words = list_of_words.split(' ')

game_number = 0
computer_won = 0
player_one_won = 0
tie = 0

while game_number < 5:
    player_one = input("Enter rock, paper, or scissors: ")
    word = random.choice(list_of_words)

    if word == "rock":
        print(f"The computer chose {word}.")
        if player_one == "rock":
            print("We have a tie.")
            tie += 1
        elif player_one == "paper":
            print("Paper beats Rock.")
            player_one_won += 1
        else:
            print("Rock beats Scissors.")
            computer_won += 1
        print("\n")
    elif word == "paper":
        print(f"The computer chose {word}.")
        if player_one == "rock":
            print("Paper beats Rock.")
            computer_won += 1
        elif player_one == "paper":
            print("We have a tie.")
            tie += 1
        else:
            print("Rock beats Scissors.")
            player_one_won += 1
        print("\n")
    else:
        print("The computer chose scissors.")
        if player_one == "rock":
            print("Rock beats Scissors.")
            player_one_won += 1
        elif player_one == "paper":
            print("Scissors beats Paper.")
            computer_won += 1
        else:
            print("We have a tie.")
            tie += 1
        print("\n")
            
    game_number += 1
    print(f"Player One Score: {player_one_won}.")
    print(f"Computer Score: {computer_won}.")
    print(f"Number of ties: {tie}.\n")
    
if player_one_won > computer_won and player_one_won > tie:
    print("The winner is player one!")
elif computer_won > player_one_won and computer_won > tie:
    print("The winner is the computer!")
elif tie > computer_won and tie > player_one_won:
    print("Too many ties!")
else:
    print("I dont know what's going on")

