import json
from datetime import datetime

# Initialize the list to store expense records
expense_records = []


# Function to add a new expense
def record_expense():
    try:
        expense_amount = float(input("Enter the expense amount: "))
        expense_note = input("Enter a brief description of the expense: ")
        expense_category = input("Enter the expense category (e.g., food, transport, entertainment): ")
        expense_date = datetime.now().strftime("%Y-%m-%d")

        new_expense = {
            "amount": expense_amount,
            "note": expense_note,
            "category": expense_category,
            "date": expense_date
        }

        expense_records.append(new_expense)
        print("Expense recorded successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number for the amount.")


# Function to save expenses to a file
def save_expense_records():
    with open("expense_data.json", "w") as expense_file:
        json.dump(expense_records, expense_file)
    print("Expenses have been saved to file.")


# Function to load expenses from a file
def load_expense_records():
    global expense_records
    try:
        with open("expense_data.json", "r") as expense_file:
            expense_records = json.load(expense_file)
        print("Expenses loaded from file.")
    except FileNotFoundError:
        print("No saved expense records found.")


# Function to display a summary of all expenses
def display_expense_summary():
    total_expenses = sum(item['amount'] for item in expense_records)
    print(f"Total expenses: {total_expenses}")

    expense_categories = {}
    for record in expense_records:
        category_name = record['category']
        if category_name not in expense_categories:
            expense_categories[category_name] = 0
        expense_categories[category_name] += record['amount']

    print("Expenses by category:")
    for category, total in expense_categories.items():
        print(f"{category}: {total}")


# Main function to execute the application
def run_expense_tracker():
    load_expense_records()

    while True:
        print("\nExpense Tracker")
        print("1. Record a New Expense")
        print("2. Display Expense Summary")
        print("3. Save Expenses")
        print("4. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            record_expense()
        elif user_choice == '2':
            display_expense_summary()
        elif user_choice == '3':
            save_expense_records()
        elif user_choice == '4':
            print("Exiting the Expense Tracker...")
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    run_expense_tracker()
