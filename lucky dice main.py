import random

max_score = 50
score_player1 = 0
score_player2 = 0
count = 0
count1 = 0
print(f"WElCOME TO THE LUCKY DICE GAME !! \n RULES: \n 1. Game will start when one of the player get 6 number in her dice \n 2. Game will stop when your number score of dice will become 50, \n IT means the number you get in lucky dice will be adding in your score_card.")
print("-"*70)

while True:
    print()
    input("Press enter for player_1:")
    player_1 = random.randint(1,6)
    print(f"The lucky number player_1 get is : {player_1}")

    input("Press enter for player_2:")
    player_2 = random.randint(1,6)
    print(f"The lucky number player_2 get is : {player_2}")

    if player_1 == 6:
        count += 1
    if count!=0:
        score_player1 += player_1
        print(f"player1 score is :{score_player1}")

    if player_2 ==6:
        count1 += 1
    if count1!=0:
        score_player2 += player_2
        print(f"player2 score is :{score_player2}")
    if score_player1 >=max_score:
        print("Player1 is  winer......")
        print(f"Your final scorr is : {score_player1}")
        break
    if score_player2 >=max_score:
        print("player2 is winer......")
        print(f"Your final scorr is : {score_player2}")
        break
