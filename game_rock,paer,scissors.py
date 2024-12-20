import random

game_list = ['rock','paper','scissors']

menu = """
                WELCOME TO ROCK PAPER SCISSOR GAME
                
                PRINT ROCK 
                PRINT PAPER
                PRINT SCISSORS
"""

status = True
while status:
    print(menu)
    computer = random.choice(game_list)
    user_choice = input("Enter your choice: ").lower()

    print("computer choice: ",computer)
    print("user choice is:",user_choice)
    print()

    if computer == 'paper' and user_choice == 'rock' or computer == 'scissors' and user_choice == 'paper' or computer == 'rock' and user_choice == 'scissors':
        print("computer won the game!")
    elif user_choice == 'paper' and computer == 'rock' or user_choice == 'scissors' and computer == 'paper' or user_choice == 'rock' and computer == 'scissors':
        print("user won the game !!")
    else:
        print("tie!")

    choice = input("Do you like to continue 'y for yes and 'n' for no :").lower()
    if choice == 'n' or choice == 'no':
        status = False