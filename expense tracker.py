# Expense Tracker in Python

# Global dictionary to store expenses
expenses = {}

# Function to add an expense
def add_expense():
    print("\n" + "*" * 10 + " Add Expense " + "*" * 10)
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    
    # Generate a unique ID for the expense
    expense_id = len(expenses) + 1
    
    # Add the expense to the dictionary
    expenses[expense_id] = {
        "amount": amount,
        "description": description,
        "date": date
    }
    
    print("\nExpense added successfully!")
    print(f"Your expense (ID: {expense_id}): {expenses[expense_id]}\n")

# Function to view all expenses
def view_expenses():
    print("\n" + "*" * 10 + " Expense History " + "*" * 10)
    if not expenses:
        print("No expenses recorded yet.\n")
    else:
        for expense_id, expense in expenses.items():
            print(f"{expense_id}. | {expense['date']} | ${expense['amount']:.2f} | {expense['description']}")
        print()

# Function to calculate total expenses
def total_expenses():
    print("\n" + "*" * 10 + " Total Expenses " + "*" * 10)
    total = sum(expense['amount'] for expense in expenses.values())
    print(f"Total expenses: ${total:.2f}\n")

# Function to delete an expense
def delete_expense():
    print("\n" + "*" * 10 + " Delete Expense " + "*" * 10)
    view_expenses()
    if expenses:
        expense_id = int(input("Enter the ID of the expense you want to delete: "))
        if expense_id in expenses:
            # deleted_expense = expenses.pop(expense_id)
            # print(f"\nExpense deleted: {deleted_expense}\n")
            del expenses[expense_id]
            print ("done")
        else:
            print("\nInvalid ID. Please try again.\n")
    else:
        print("No expenses to delete.\n")

# Main program
start = True
while start:
    menu = """
    --- Expense Tracker ---
    1. Add Expense
    2. View Expenses
    3. View Total Expenses
    4. Delete Expense
    5. Exit
    """
    print(menu)
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expenses()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        print("\nThank you for using the Expense Tracker. Goodbye!\n")
        start = False
    else:
        print("\nInvalid choice. Please try again.\n")