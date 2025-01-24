"""
Personal Expense Tracker - CLI program
"""

# imports
import json
import os
from datetime import datetime

# globals
totalExpense : float = 0.00
expenseList = [] # needs amount, category, timestamp

def main():
    """
    Main menu prompts also loads data from json file from load_data func
    """
    if load_data() == 1:
        print("Hello, welcome to this personal expense tracker\n")
    else:
        print("Welcome back to this personal expense tracker\n")
    
    while True:
        print("Would you like to view or add an expense?")
        try:
            choice = int(input("1. Add new expense\n2. View expenses\n3. View Spending Summary\n4. Exit\nChoice: "))
            if choice == 1:
                add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_spending_sum()
            elif choice == 4:
                print("See you next time.\n")
                quit()
            else:
                print("Please enter a number between 1-4.\n")
        except ValueError:
            print("Non-integer entered, enter a number between 1-4.\n")
            

def load_data():
    """
    Loads data from expensedata.json file into expenseList
    """
    global expenseList
    if os.path.exists("expensedata.json"):
        # load the data into the expense list
        f = open("expensedata.json", "r")
        expenseList = json.load(f) # this only works if there is one list of dict in the json
        f.close()
        return 0 # file exists
    else:
        f = open("expensedata.json", "x")
        f.write(json.dumps(expenseList))
        f.close()
        return 1 # new file

def save_data(list):
    """
    Saves list to json file
    """
    f = open("expensedata.json", "w")
    f.write(json.dumps(list))
    f.close()

def add_expense():
    """
    Lets user to add an expense to their list
    """
    global expenseList

    try:
        amount = float(input("\nPlease enter the amount: "))
        category = input("Please enter the category: ")
        timestamp = datetime.now()
        formatedTime = timestamp.strftime("%Y-%m-%d %H:%M:%S")

        expenseList.append({"amount" : amount, "category" : category, "timestamp" : formatedTime})

        save_data(expenseList)
        print() # acts as a \n
    except ValueError:
        print("Invalid entry. please try again.\n")


def view_expenses():
    """
    View all expenses
    """
    print() # acts as a \n
    
    if not expenseList:
        print("Expense list empty.\n")
    else:
        for expenses in expenseList:
            print(f"Amount: {expenses["amount"]}\nCategory: {expenses["category"]}\nTimestamp: {expenses["timestamp"]}\n")

def view_spending_sum():
    """
    Used to show total spending amount
    """
    global expenseList, totalExpense
    
    calc_total(expenseList)
    
    if totalExpense == 0.00:
        print("\nNo expenses.\n")
    else:
        print(f"\nTotal expense: ${totalExpense}\n")

def calc_total(expenses):
    """
    Calcs the total expenses in the expenseList
    """
    global totalExpense
    totalExpense = 0.00
    for amount in expenses:
        totalExpense += amount['amount']


if __name__ == "__main__":
    """
    Main guard
    """
    # This is used as a test case for calc total and what the expense file will hold
    # test = [
    # {
    #     "amount": 25.50,
    #     "category": "food",
    #     "timestamp": "2023-10-15 12:30:00"
    # },
    # {
    #     "amount": 10.00,
    #     "category": "transport",
    #     "timestamp": "2023-10-15 08:15:00"
    # }
    # ]
    # calc_total(test)
    main()