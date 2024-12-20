"""
            JAY BHAVANI

        1) product manager
        2) customer

        # section for product manager(if user use 1)
        ---> add product
        ---> view
        ---> remove or del any product(del function)


            product name: vadapav
            qty: 20
            price :30

            product name: dabeli
            qty: 30
            price :40

        # section for customer (if user use 2)
        --> at first directly show the items  in stock( view section from product manager)
        --> ask user what would you like to order, (product name, and quantity of that product)
        --> print bill( with total price{ price * qty of product})
        --> again  ask user if she like to coninue, again repeat the same process
        
# for me
diction should be viewed like this
product = {vadapav{"qty":20,"price":30} , dabeli{"qty":30,"price":40} , ...}
# hello priyanshi, you can use keyword argument, (if all string are keys).....
e.g.: 
product = dict(vadapav=dict(qty=20,price=30),dabeli=dict(qty=30,price=40))

"""
start = True
product = {}
while start:

    menu = """
                    JAY BHAVANI 
            1)  Product Manager
            2)  Customer
            3)  exit
    """
    print(menu)

    choice_for_menu = int(input("Enter your choice: "))
    if choice_for_menu == 1:
        print("*" * 10 +"Welcome to Product Manager"+ "*" * 10 )
        your_choice = int(input("What would you like choose \n 1) add product\n 2) view\n 3)remove product from stock\n-->"))
        # product_qty_price= {}
        if your_choice == 1:
            input("Press enter to add product ")
            start_2 =True
            while start_2:  
                food_product = input("Enter your product: ")
                qty = int(input("Enter your quantity: "))
                price = int(input("Enter your price: "))
                product_qty_price= {} #reseting it will help to store new value each time...

                product_qty_price["qty"] = qty
                product_qty_price["price"] = price

                #or this way can be possible
                # product_qty_price = {"qty":qty,"price":price}

                # product_qty_price[qty] = price
                # print(product_qty_price)
                product[food_product] = product_qty_price
                print("Your product is:",end=" ")
                print(product)
                 #some of the try and error methods
                # product_qty_price[product] = [qty][price]
                # product=product_qty_price
                # print(product)

                choice_for_product = input("do you like to continue product adding 'y' for yes or 'n' for no:").lower()
                if choice_for_product == 'n' or choice_for_product == 'no':
                    start_2 = False

        elif your_choice == 2:
            print("product     qty     price  ")
            for k,v in product.items():
                print(f"{k}    |   {v['qty']}   |   {v['price']}")
                # print(f"{k}     {v["qty"]}    {v["price"]}")#this will show an conflict in "" and ''
                # print(product[product_qty_price])
            # print(f" {food_product} | qty: {qty} | price: {price} ")
        else:
            del_product = input("Enter the product you want to delete: ")
            if del_product == food_product:
                del product[food_product]

            print("Your remaining products are: ")
            print(product)

    elif choice_for_menu == 2:
        print("*" * 10 +"Welcome to Customer"+ "*" * 10 )
        start_3 = True
        while start_3:
            print("menu of stock items:-\n")
            if len(product) > 0:
                print("product     qty     price  ")
                for k,v in product.items():
                    #error is occuring when qty is becoming 0, after its update in purchase, so to handle this issue, 
                    # we have to put a condition that
                    if product[k]['qty']>0:
                        print(f"{k}    |   {product[k]["qty"]}   |   {product[k]["price"]}")
                    # print("=====================================")
                    # print(product)
                    # print(product.items())
                    # print(k)
                    # print(v)
                print()

                purchase_user = input("What would you like to order :")
        
                # if purchase_user in product.items():
                if purchase_user in product:
                    user_qty = int(input("Enter the number of quantity you like  to order :"))
                    # if user_qty<= product[food_product]["qty"]: # this food_product will take the last product in dictionary, 
                    # so to cure this we have to user purchase_user to get the accurate result, as per product. 
                    if user_qty<=product[purchase_user]["qty"]:
                        print(f"Your bill is :{user_qty * product[purchase_user]["price"]} ")
                    # both way it is possible
                    # if user_qty<= product[purchase_user]["qty"]:
                    # print(f"Your bill is :{user_qty * product[purchase_user]["price"]} ")
                        product[purchase_user]["qty"] = product[purchase_user]["qty"] - user_qty # updating the qunatity after purchase
                        # product[food_product]["qty"] -= user_qty
                        if product[purchase_user]["qty"]==0:
                            del product[purchase_user]
                    else:
                        print(f"Quantity of product left are: {product[purchase_user]["qty"]}, not sufficient for purchase")
                else:
                    print("Invalid product, please select it from menu!!")

                choice_for_user = input("do you like to continue product adding 'y' for yes or 'n' for no:").lower()
                if choice_for_user == 'n' or choice_for_user == "no":
                    start_3 = False
            else:
                print("All stock are clear!!")
                start_3 = False
    else:
        print("*" * 10 +"Thank you for visiting"+"*" * 10 )
        start = False