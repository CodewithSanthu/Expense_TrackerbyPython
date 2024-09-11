import json
from datetime import datetime

def add_expense(expenses, amount, description, category):
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    for expense in expenses:
        print(f"{expense['date']} - {expense['category']}: {expense['description']} - ${expense['amount']}")

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, 'w') as file:
        json.dump(expenses, file)
    print(f"Expenses saved to {filename}")

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Save & Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            category = input("Enter category: ")
            add_expense(expenses, amount, description, category)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses)
            break
        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
