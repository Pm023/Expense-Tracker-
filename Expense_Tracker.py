import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# File to store data
FILE_NAME = "expenses.csv"

# If file does not exist, create empty dataset
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])
    df.to_csv(FILE_NAME, index=False)

# Load data
df = pd.read_csv(FILE_NAME)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Travel, Bills, Shopping, etc.): ")
    amount = float(input("Enter amount: "))
    notes = input("Enter note (optional): ")

    new_entry = pd.DataFrame([[date, category, amount, notes]],
                             columns=["Date", "Category", "Amount", "Notes"])
    
    global df
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)
    print("\n✅ Expense added successfully!\n")

def view_expenses():
    print("\n----- All Expenses -----\n")
    print(df)
    print("\n------------------------\n")

def monthly_spending():
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')
    
    month_summary = df.groupby('Month')['Amount'].sum()
    print("\n----- Monthly Spending -----\n")
    print(month_summary)
    print("\n----------------------------\n")

def category_spending():
    category_summary = df.groupby('Category')['Amount'].sum()
    print("\n----- Spending by Category -----\n")
    print(category_summary)
    print("\n-------------------------------\n")

    # Plot without specifying colors
    plt.figure()
    category_summary.plot(kind='bar')
    plt.xlabel("Category")
    plt.ylabel("Total Spent")
    plt.title("Spending by Category")
    plt.show()

def menu():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Show Monthly Spending Summary")
        print("4. Show Category-wise Spending Chart")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_spending()
        elif choice == "4":
            category_spending()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

menu()
