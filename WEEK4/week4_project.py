# ---------------------------------------------------------
# WEEK 4 PROJECT: PERSONAL FINANCE TRACKER
# Developer's Arena Internship
# ---------------------------------------------------------
import csv
from datetime import datetime

# File to store expense data
FILENAME = "expenses.csv"

# Function to load existing expenses from file
def load_expenses():
    expenses = []
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        # Create file if not found
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Description", "Category", "Amount"])
    return expenses

# Function to save expenses to file
def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ["Date", "Description", "Category", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

# Function to add a new expense
def add_expense(expenses):
    print("\n--- Add New Expense ---")
    description = input("Enter description: ")
    category = input("Enter category (e.g., Food, Travel, Bills): ")
    amount = float(input("Enter amount: ₹"))
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {"Date": date, "Description": description, "Category": category, "Amount": f"{amount:.2f}"}
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

# Function to view all expenses
def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses found.")
        return

    total = 0
    for exp in expenses:
        print(f"{exp['Date']} | {exp['Category']:<10} | {exp['Description']:<15} | ₹{exp['Amount']}")
        total += float(exp["Amount"])
    print(f"\nTotal Spent: ₹{total:.2f}")

# Function to generate category-wise summary
def summary_report(expenses):
    print("\n--- Monthly Summary Report ---")
    summary = {}
    total = 0

    for exp in expenses:
        category = exp["Category"]
        amount = float(exp["Amount"])
        summary[category] = summary.get(category, 0) + amount
        total += amount

    for category, amount in summary.items():
        print(f"{category:<10} : ₹{amount:.2f}")

    print(f"\nOverall Spending: ₹{total:.2f}")

# Main program loop
def main():
    expenses = load_expenses()

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_report(expenses)
        elif choice == "4":
            print("💰 Exiting... Have a financially smart day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

