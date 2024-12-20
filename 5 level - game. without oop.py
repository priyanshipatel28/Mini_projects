# this is 5 level game in python
import random

total_scored = 0

level = True
while True:
    computer_guess = random.randint(1,50)
    # for 10 trials
    points = 10
    for i in range(1,11):
        user_guess = int(input("Enter your number :"))
       
        if computer_guess == user_guess:
            total_scored += points
            print(f"You Win The LEVEL=1, The number guess by computer is {computer_guess}")
            print(f"Now will move to next level and your score is : {total_scored}")
            break
        elif i==10 and computer_guess != user_guess:
            print("You are OUT! \n Try Again Next Time")
        else:
            if user_guess>computer_guess:
                print("Hint : Guess Lower Number.")
            elif user_guess<computer_guess:
                print("Hint : Guess Upper Number.")
    #   level 2          
    if total_scored == 10:
        print("You are now in level 2, Congratulations!")
        print("-------------------------------------------")
        computer_guess = random.randint(1,100)
        points = 10
    # for 10 trials
        for i in range(1,11):
            user_guess = int(input("Enter your number :"))
            if computer_guess == user_guess:
                total_scored += points
                print(f"You Win The LEVEL=2, The number guess by computer is {computer_guess}")
                print(f"Now will move to next leve3 and your score is : {total_scored}")
                break  #( second level start from here, else part) 
            elif i==10 and computer_guess != user_guess:
                print("You are OUT! \n Try Again Next Time")
            else:
                if user_guess>computer_guess:
                    print("Hint : Guess Lower Number.")
                elif user_guess<computer_guess:
                    print("Hint : Guess Upper Number.")
        # level 3
        if total_scored == 20:
            print("You are now in level 3, Congratulations!")
            print("-------------------------------------------")
            computer_guess = random.randint(1,150)
            points=10
    # for 10 trials
            for i in range(1,11):
                user_guess = int(input("Enter your number :"))
            
                if computer_guess == user_guess:
                    total_scored += points
                    print(f"You Win The LEVEL=3, The number guess by computer is {computer_guess}")
                    print(f"Now will move to next leve4 and your score is : {total_scored}")
                    break   
                elif i==10 and computer_guess != user_guess:
                    print("You are OUT! \n Try Again Next Time")
                else:
                    if user_guess>computer_guess:
                        print("Hint : Guess Lower Number.")
                    elif user_guess<computer_guess:
                        print("Hint : Guess Upper Number.")
            # LEVEL 4
            if total_scored == 30:
                print("You are now in level 4, Congratulations!")
                print("-------------------------------------------")
                computer_guess = random.randint(1,200)
                points=20
            # for 7 trials
                for i in range(1,8):
                    user_guess = int(input("Enter your number :"))
            
                    if computer_guess == user_guess:
                        total_scored += points
                        print(f"You Win The LEVEL=4, The number guess by computer is {computer_guess}")
                        print(f"Now will move to next level 5 and your score is : {total_scored}")
                        break   
                    elif i==7 and computer_guess != user_guess:
                        print("You are OUT! \n Try Again Next Time")
                    else:
                        if user_guess>computer_guess:
                            print("Hint : Guess Lower Number.")
                        elif user_guess<computer_guess:
                            print("Hint : Guess Upper Number.")
                    # level 5
                if total_scored == 50:
                        print("You are now in level 5, Congratulations!")
                        print("-------------------------------------------")
                        computer_guess = random.randint(1,200)
                        points=30
            # for 7 trials
                        for i in range(1,8):
                            user_guess = int(input("Enter your number :"))
            
                            if computer_guess == user_guess:
                                total_scored += points
                                print(f"You Win The LEVEL=5, The number guessed by the computer is {computer_guess}")
                                print(f"YEAH VICTORY !! You have completed all levels. Your total score is: {total_scored}")
                                level = False
                                break  
                            elif i==7 and computer_guess != user_guess:
                                print("You are OUT! \n Try Again Next Time")
                            else:
                                if user_guess>computer_guess:
                                    print("Hint : Guess Lower Number.")
                                elif user_guess<computer_guess:
                                    print("Hint : Guess Upper Number.")
                        



