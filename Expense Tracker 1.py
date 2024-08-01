import csv
import os
from datetime import datetime

EXPENSE_FILE = 'expenses.csv'

def initialize_file():
    if not os.path.isfile(EXPENSE_FILE):
        with open(EXPENSE_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Description'])


def add_expense():
    try:
        amount = float(input("Enter the amount spent: "))
        category = input("Enter the expense category (e.g., food, transportation, entertainment): ")
        description = input("Enter a brief description of the expense: ")
      
        with open(EXPENSE_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime('%Y-%m-%d'), amount, category, description])
        
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the amount.")


def view_monthly_expenses():
    month = input("Enter the month (YYYY-MM): ")
    try:
        total = 0
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Date'].startswith(month):
                    total += float(row['Amount'])
        print(f"Total expenses for {month}: ${total:.2f}")
    except Exception as e:
        print(f"Error reading file: {e}")


def view_category_expenses():
    category = input("Enter the expense category: ")
    try:
        total = 0
        with open(EXPENSE_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Category'].lower() == category.lower():
                    total += float(row['Amount'])
        print(f"Total expenses for category '{category}': ${total:.2f}")
    except Exception as e:
        print(f"Error reading file: {e}")


def display_menu():
    print("\nExpense Tracker Menu")
    print("1. Add New Expense")
    print("2. View Monthly Expenses")
    print("3. View Expenses by Category")
    print("4. Exit")


def main():
    initialize_file()
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_expenses()
        elif choice == '3':
            view_category_expenses()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
