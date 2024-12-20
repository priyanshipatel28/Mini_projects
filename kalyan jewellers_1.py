"""
Kalyan Jewellry

billing system

M 
>  65
purchase > 2lk - 3lk    20% 
purchase > 3lk - 5lk 	30% 
purchase > 5lk  	35% 


<65
purchase > 2lk - 3lk    10% 
purchase > 3lk - 5lk 	20% 
purchase > 5lk  	25% 



F
>  65
purchase > 2lk - 3lk    25% 
purchase > 3lk - 5lk 	35% 
purchase > 5lk  	40% 


<65
purchase > 2lk - 3lk    15% 
purchase > 3lk - 5lk 	25% 
purchase > 5lk  	30% 


------------------------------------------------------------
Enter your name : 
Enter gender : 
Enter age : 

Enter product : Ring 
Enter product gram : 20  
current gold price (1 grm) : 5752

-------------------------------------
TOTAL GOLD RATE :  XXXXX 


Making charges (1 gram)  : 845
Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 

---------------------------------------
TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG



DISCOUNT :   25 (AUTOMATIC) 
DIS- AMOUNT :  
-----------------------------------------
total net amount 
"""

print(F"WELCOME TO KALYAN JEWELLERS \n THIS A BILLING SYSTEM \n the product are : \n1) Ring \n2) Braclet \n3)Pendant")


user = input("Enter your name :")
age = int(input("Enter your age: "))
gender = input("Enter your gender(don't write it in aggregation form): ")
product = input("Enter the product you want to buy(from the giving product name): ")

print("The gold rate for 1 gram is : 7543")
print("The making charger for 1 gram is :700")
gram_1, marking_chargers = 7543,700
gram = int(input("Enter the amount of gram (gold) you want to purchase: "))

marking_charges_on_gram = marking_chargers * gram
gram_1_on_gram = gram_1 * gram
purchase = marking_charges_on_gram+gram_1_on_gram
print(f"Your total purchase is : {purchase}")
#for condition on purchase and absed on gender
# for male
if gender == "male" or "Male":
    if age >= 65:
        if 200000<=purchase<=300000:
            print("The discount applied is: 20%")
            discount = 20
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (20%), the product price is :{discount_price}")

        elif 300000<=purchase<=500000:
            print("The discount applied is: 30%")
            discount = 30
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (30%), the product price is :{discount_price}")

        elif purchase>500000:
            print("The discount applied is: 35%")
            discount = 35
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (35%), the product price is :{discount_price}")
        else:
            discount_price = purchase
            discount = 0
            discount_amount = 0
            print(f"There is no discount applied , your ourchase amount is :{discount_price}")
    else:
        if 200000<=purchase<=300000:
            print("The discount applied is: 10%")
            discount = 10
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (10%), the product price is :{discount_price}")

        elif 300000<=purchase<=500000:
            print("The discount applied is: 20%")
            discount = 20
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (20%), the product price is :{discount_price}")

        elif purchase>500000:
            print("The discount applied is: 25%")
            discount = 25
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (25%), the product price is :{discount_price}")
        else:
            discount_price = purchase
            discount = 0
            discount_amount = 0
            print(f"There is no discount applied , your ourchase amount is :{discount_price}")

if gender == "female" or "Female":
    if age >= 65:
        if 200000<=purchase<=300000:
            print("The discount applied is: 25%")
            discount = 25
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (25%), the product price is :{discount_price}")

        elif 300000<=purchase<=500000:
            print("The discount applied is: 35%")
            discount = 35
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (35%), the product price is :{discount_price}")

        elif purchase>500000:
            print("The discount applied is: 40%")
            discount = 40
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (40%), the product price is :{discount_price}")
        else:
            discount_price = purchase
            discount = 0
            discount_amount = 0
            print(f"There is no discount applied , your ourchase amount is :{discount_price}")
        
    else:
        if 200000<=purchase<=300000:
            print("The discount applied is: 25%")
            discount = 25
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (25%), the product price is :{discount_price}")

        elif 300000<=purchase<=500000:
            print("The discount applied is: 35%")
            discount = 35
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (35%), the product price is :{discount_price}")

        elif purchase>500000:
            print("The discount applied is: 40%")
            discount = 40
            discount_amount = (purchase*discount) // 100
            print(f"the discount amount is : {discount_amount}")
            discount_price = purchase-discount_amount        
            print(f"After discount of (40%), the product price is :{discount_price}")
        else:
            discount_price = purchase
            discount = 0
            discount_amount = 0
            print(f"There is no discount applied , your ourchase amount is :{discount_price}")
print("-"*80)
print("BILL BOARD")

print("Name : ",user)
print("gender :",gender)
print("age:",age)
print("Product :",product)
print("Product Gram: ",gram)
print("Current gold price(1 grm):",gram_1)
print("-"*50)
print("TOTAL GOLD RATE :",gram_1_on_gram)
print("Making charges (1 gram):",marking_chargers)
print("Total making charges :",marking_charges_on_gram)
print("-"*50)
print("TOTAL AMOUNT : ",purchase)
print(f"DISCOUNT:{discount}%")
print("DIS-AMOUNT: ",discount_amount)
print("-"*50)
print("TOTAL NET AMOUNT:",discount_price)






       
 