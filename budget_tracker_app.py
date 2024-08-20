# connecting to sql database
import sqlite3

conn = sqlite3.connect("budget_tracker.db")
cursor = conn.cursor()

# Creating tables for expenses, income, budget and financial goals
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        description TEXT,       
        date DATE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS income (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL,
        description TEXT,       
        date DATE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS budget (
        id INTEGER PRIMARY KEY,
        category TEXT,
        amount REAL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS financial_goals (
        id INTEGER PRIMARY KEY,
        income REAL,
        expenses REAL,
        savings REAL,
        date Date
    )
""")
conn.commit()

# Function adding expenses into programme
def add_expense(category, amount, description, date):
    cursor.execute("INSERT INTO expenses (category, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (category, amount, description, date))
    conn.commit()

# Function that view the expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(f"Category: {expense[1]}, Amount: {expense[2]}, Description: {expense[3]}, Date: {expense[4]}")

# Function to view expense by category
def view_expenses_by_category():
    category = input("Please enter expense category: ")
    cursor.execute('SELECT * FROM expenses WHERE category = ?', (category,))
    expens = cursor.fetchall()
    if not expens:
        print("The category does not exist, Try again!")
    else:
        for expense in expens:
            print(f"Category: {expense[1]}, Amount: {expense[2]}, Description: {expense[3]}, Date: {expense[4]}")

# Fuction adding income to programme
def add_income(category, amount, description, date):
    cursor.execute("INSERT INTO income (category, amount, description, date) VALUES (?, ?, ?, ?)", 
                   (category, amount, description, date))
    conn.commit()

# Function to view income
def view_income():
    cursor.execute("SELECT * FROM income")
    income = cursor.fetchall()
    for i in income:
        print(f"Category: {i[1]}, Amount: {i[2]}, Description: {i[3]}, Date:  {i[4]}")

# Function to view income by category
def view_income_by_category():
    category = input("Please enter income category: ")
    cursor.execute('SELECT * FROM income WHERE category = ?', (category,))
    income = cursor.fetchall()
    if not income:
        print("The category does not exist, Try again!")
    else:
        for i in income:
            print(f"Category: {i[1]}, Amount: {i[2]}, Description: {i[3]}, Date: {i[4]}")

# Function that sets a budget
def set_budget(category, amount):
    cursor.execute("INSERT INTO budget (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()

# Function to view budget by category
def view_budget():
    category = input("Please enter budget category: ")
    cursor.execute("SELECT * FROM budget WHERE category = ?", (category,))
    budget = cursor.fetchall()
    if not budget:
        print("The category does not exist,Try again!")
    else:
        for budgets in budget:
            print(f"Category: {budgets[1]}, Amount: {budgets[2]}")

def set_financial_goals(income, expenses, savings, date):
    cursor.execute("INSERT INTO financial_goals (income, expenses, savings, date) VALUES (?, ?, ?, ?)", 
                   (income, expenses, savings, date))
    conn.commit()

def view_financial_goal():
    cursor.execute("SELECT * FROM financial_goals")
    financial_goals = cursor.fetchall()
    for finance in financial_goals:
        print(f"Income: {finance[1]}, Expenses: {finance[2]}, Savings: {finance[3]}, Date: {finance[4]}")

''' The budget tracker menu,user will select option in menu.
    The functions above will assist with the output of the menu options
'''
while True:
    print(" Welcome to the Budget Tracker:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View expenses by category")
    print("4. Add income")
    print("5. View income")
    print("6. View income by category")
    print("7. Set budget for a category")
    print("8. View budget for a category")
    print("9. Set financial goals")
    print("10. View progress towards financial goals")
    print("11. Quit")

    choice = input("Enter your choice: ")

# Adding expense to table 
    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        description = input("Reason for expense: ")
        date = input("Enter date (YYYY-MM-DD): ")
        add_expense(category, amount, description, date)
        print("Your expense has been added.\n")

# viewing expense in app, it will show the in list format  
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        view_expenses_by_category()

    elif choice == "4":
        category = input("Enter income category: ")
        amount = float(input("Enter income amount: "))
        description = input("Reason for income: ")
        date = input("Enter date (YYYY-MM-DD): ")
        add_income(category, amount, description, date)
        print("Your income has been added.")

    elif choice == "5":
        view_income()

    elif choice == "6":
        view_income_by_category()

    elif choice == "7":
        category = input("Enter the category for the budget: ")
        amount = float(input("Enter the amount: "))
        set_budget(category, amount)

    elif choice == "8":
        category = input("Please enter income category to be viewed: ")
        view_budget()

    elif choice == "9":
        income = float(input("Enter Income goal: "))
        expenses = float(input("Enter expense goal amount: "))
        savings = float(input("Enter your savings goal: "))
        date = input("Enter date you want to achieve goal(YYYY-MM-DD): ")
        set_financial_goals(income, expenses, savings, date)
        print("Your financial goal has been added")
    
    elif choice == "10":
        view_financial_goal()

    elif choice == "11":
        print("Programme Exit, Thank You for using the budget app.")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()