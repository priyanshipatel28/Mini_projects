
count_coke=0
count_brus = 0
count_ice_cream = 0
payment_from_pizza = []
payment_from_pasta = []
amount_of_the_day=[]
no_pizza_and_pasta = []
# --------------------------------pizza---------------------------
class pizza():
    global payment_from_pizza
    pizza = 10.99

    def __init__(self):
        self.order_pizza = 0 

    def pizza_menu(self):
        print("1 large pizza = 10.99 AUD \n2 large pizzas = 21.98 AUD \n3 large pizzas = 32.97 AUD \n" +
              "*" * 3 + "Buy 4 or more pizzas and get 1.5lt of soft drink free" + "*" * 3)

    def offer_for_pizza(self):
        print("*" * 3 + "Congratulations !! 1.5lt softdrink free " + "*" * 3)

    def pizza_order(self):
        global count_coke
        global no_pizza_and_pasta
        self.order_pizza = int(input("Enter number of pizzas you want to order: "))
        profit_pizza = self.pizza * self.order_pizza
        no_pizza_and_pasta.append(self.order_pizza)
        if self.order_pizza >= 4:
            self.offer_for_pizza()
            count_coke += 1
        print("Your pizza order amount is: ", profit_pizza)
        payment_from_pizza.append(profit_pizza)

# ---------------------------------------End-------------------------------------------

# --------------------------------pasta---------------------------
class pasts():
    global payment_from_pasta
    pasta = 9.5

    def __init__(self):
        self.order_pasta = 0

    def pasta_menu(self):
        print("\n1 large pasta = 9.5 AUD \n2 large pastas = 19.00 AUD \n3 large pastas = 28.5 AUD \n" +
              "*" * 3 + "Buy 4 or more pastas and get 2 bruschetta free" + "*" * 3 +
              "\n" + "*" * 3 + "Buy 2 or more pizzas and pastas and get 2 choco brownies ice cream free" + "*" * 3)

    def offer_for_pasta(self):
        print("*" * 3 + "Congratulations !! Get 2 bruschetta free " + "*" * 3)

    def pasta_offer(self):
        global count_brus
        global no_pizza_and_pasta
        self.order_pasta = int(input("Enter number of pastas you want to order: "))
        profit_pasta = self.pasta * self.order_pasta
        no_pizza_and_pasta.append(self.order_pasta)
        if self.order_pasta >= 4:
            self.offer_for_pasta()
            count_brus += 1
        print("Your pasta order amount is: ", profit_pasta)
        payment_from_pasta.append(profit_pasta)

# ---------------------------------------End-------------------------------------------

# ------------------------------main menu----------------------------------
class Menu(pizza, pasts):
    global count_brus
    global count_coke

    def __init__(self):
        super().__init__()
        print(" " * 10 + "Welcome to Amazing Pizza and Pasta Pizzeria" + " " * 10)
        print("Press 1 : Order menu \nPress 2 : Exit")

    def user_order(self):
        user = input("Enter your name: ")
        print(f"Welcome, {user}!")

    def offer_for_both(self):
        print("*" * 3 + "Congratulations !! Get 2 choco brownies ice cream free" + "*" * 3)

    def no_pizza_pasta(self):
        global no_pizza_and_pasta
        total_sum = 0
        for i in no_pizza_and_pasta:
            total_sum +=i
        return total_sum


    def more_than_4(self, order_pizza, order_pasta):
        global payment_from_pasta
        global payment_from_pizza
        global count_ice_cream
        if order_pizza >= 4 or order_pasta >= 4:
            self.offer_for_both()
            count_ice_cream += 1
        total_order = sum(payment_from_pasta) + sum(payment_from_pizza)
        print("Your total order is: ", total_order)
        amount_of_the_day.append(total_order)
        print("----> Your net order amount of the day is: ", sum(amount_of_the_day))

    def Pizza_and_pasta_bill(self):
        print("-" * 20 + "Pizza_and_pasta_bill" + "-" * 20)
        print("\nPayment received from pizza: ", int(sum(payment_from_pizza)))
        print("\nPayment received from pasta: ", int(sum(payment_from_pasta)))
        print("\nYour net order amount of the day is: ", int(sum(amount_of_the_day)))
        print("\nNumber of pizzas and pastas sold in one shift: ",int(self.no_pizza_pasta()))
        print("\nNumber of 1.5lt soft drink bottles given: ", count_coke)
        print("\nNumber of bruschetta given to customers: ", count_brus)
        print("\nNumber of choco brownies ice cream given to customers: ", count_ice_cream)

    def ASking_choice(self):
        status = True
        while status:
            user = int(input("Enter your choice: "))
            if user == 2:
                print("Thank you!")
                break
            else:
                self.pizza_menu()
                self.pasta_menu()
                while True:
                    self.user_order()
                    self.pizza_order()
                    self.pasta_offer()
                    self.more_than_4(self.order_pizza, self.order_pasta)
                    choice = input("Want to enter order for another customer (Y/N): ").lower()
                    if choice == 'n':
                        status = False
                        self.Pizza_and_pasta_bill()
                        break
# ---------------------------------------End-------------------------------------------

# -------------------------object to call the instance of the class--------------------
Menu = Menu()
Menu.ASking_choice()
# ---------------------------------------End-------------------------------------------