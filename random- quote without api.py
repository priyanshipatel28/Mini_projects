import random

# List of predefined quotes
quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]

# Function to generate a random quote
def random_quote():
    return random.choice(quotes)

# Main program
start = True
while start:
    print("\n" + "*" * 10 + " Random Quote Generator " + "*" * 10)
    print("1. Get a Random Quote")
    print("2. Exit")
    
    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        print("\nHere's a random quote for you:\n")
        print(random_quote())
    elif choice == "2":
        print("\nThank you for using the Random Quote Generator. Goodbye!\n")
        start = False
    else:
        print("\nInvalid choice. Please try again.\n")