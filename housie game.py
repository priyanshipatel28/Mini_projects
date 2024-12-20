"""
player 1:

player 2:

					press '1' for play game and press '2' for exit
					
					1

					shuffle tickets

					(1-100 randomly 12 tickets generate)(it is back work in program, may be with for loop, or may be other...)

							tickets generated
					
				23  88  66  54  72  45  81  65  35  5  7  2

				player1 : 66  54  72  81  65  23
				
				player2:  88  45  5  7  2  35
					
					enter  (input())-->input function    
				

					lucky number is: 2
							enter
					(whatever number is generated in lucky number must be remove from player 1 or player 2 if it is present)
					(whoever (players) number will complete first then , it will be winner between(player1 ans player 2)


				player1: 66 54 72 81 65 23
				player2: 88 45 5 7 35
					
						(loop)
					lucky number is: 23
							enter
					(whatever number is generated in lucky number must be remove from player 1 or player 2 if it is present)
					(whoever (players) number will complete first then , it will be winner between(player1 ans player 2)


				player1: 66 54 72 81 65 
				player2: 88 45 5 7 35
						(loop, may be)
					lucky number is: 81
							enter
					(whatever number is generated in lucky number must be remove from player 1 or player 2 if it is present)
					(whoever (players) number will complete first then , it will be winner between(player1 ans player 2)


				player1: 66 54 72 65 23
				player2: 88 45 5 7 35

				(like these to all the numbers in player1 and player2, whoever first complete the number in list then it will be winner).....

"""
import random

menu = """
                WELCOME TO THE HOUSIE GAME

                THIS GAME IS PLAYED BY TWO PLAYERS
                PLAYER_1:
                PLAYER_2:

            Press '1' to play the game 

                    or

            Press '2' for exit
"""
tickets_generated = [] # a empty list to store ticket generated
player_1 = [] # a empty list for player_1
player_2 = [] # a empty list for player_2
flag = True

while flag:
    print(menu)
    result = int(input("--> "))
    if result == 2:
        flag = False
        break # to break the the game 
    else:
        print("GAME START !!")

    input("wait for some time, tell computer generate your tickets") # just to press enter, to take a pause, JUST FOR FUN :)
    print() # just to leave one line

    for i in range(12): # it is fixed to generate 12 tickets so, for loop
        shuffle_ticktes = random.randint(1,100) # it will generate random number 
        if shuffle_ticktes not in tickets_generated: # it will help me to not store the same number twice in a tickets_generated
            tickets_generated.append(shuffle_ticktes) # putting tickets in list
            
    print(f"{"-"*10} tickets_generated are: {"-"*10} ") # just for fun, to look better
    for i in tickets_generated:  # to print the number in list without brackets and comma
        print(i,end=" ")   
    
    # player_1 = [ tickets_generated[::2] for i in tickets_generated]

    # tickets to distributed in player_1

    player_1.extend(tickets_generated[::2]) # with the help of slicing 
    print() #to leave one line
    print("player_1 :",end=" ") # to print evenytime in one line, with number
    for i in player_1:
        print(i,end=" ") # this will print number in player_1

    # tickets to diatributed in player_2
    for i in tickets_generated: # i think this will work
        if i not in player_1: # this will check the number that are present in player_1
            player_2.append(i) # this will append the remaining number to player_2

    print() #to leave one line
    print("player_2 :",end=" ") # to print evenytime in one line, with number
    for j in player_2:
        print(j,end=" ") # this will print number in player_2

    print()
    input("press enter to get the lucky number")

    while tickets_generated != []:
        lucky_number = random.choice(tickets_generated)
        print("the lucky number genereted is: ",lucky_number) #it will print the lucky_number
        # if lucky_number == player_1 and lucky_number == player_2: # may be this work because if the lucky_number is repeacted then, it is not necessary..
        if lucky_number in player_1:# it will check the number present in player_1
            player_1.remove(lucky_number) # if yes then remove it
        elif lucky_number in player_2:# it will check the number present in player_2
            player_2.remove(lucky_number) # if yes then remove it

        tickets_generated.remove(lucky_number)# to remove the lucky number from ticket generated, so that it won't repeat the number again
        
        print()
        print("player_1 :",end=" ")
        for i in player_1:
            print(i,end=" ") # to print again the list of player_1

        print()
        print("player_2 :",end=" ")
        for i in player_2:
            print(i,end=" ") # to print again the list of player_2

        input()
        #who's ever list will be first empty then it will be winner 
        if player_1 == []: 
            print(f"player_1 win the game!")
            break # to break the loop
        
        if player_2 == []:
            print(f"player_2 win the game!")
            break #to brean the loop

    # to ask user to play the game , again if she wan't to play
    again = input("Do you like to play again:  'y' for yes or 'n' for no :").lower()
    if again == 'n' or again == 'no':
        flag = False
    else:
        flag = True

    
    