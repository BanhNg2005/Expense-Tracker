from expense_tracker.venv.src.backend.expense import Expense
from expense_tracker.venv.src.backend.tracking import ExpenseTracker
from datetime import datetime

print("Welcome to SmartTrackers!")
def add_expense_from_user(tracker):
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                raise ValueError("Invalid amount")
            break
        except ValueError:
            print("Invalid amount! Please enter a valid number")
    while True:
        category = input("Enter the category (Food, Transport, Entertainment, Bills, Others): ").strip()
        if category not in ["Food", "Transport", "Entertainment", "Bills", "Others"]:
            print("Invalid category")
        else:
            break
    while True:
        date = input("Enter the date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format, should be YYYY-MM-DD")
    description = input("Enter the description: ").strip()
    expense = Expense(amount, category, date, description)
    tracker.add_expense(expense)
    print("=====================")
    print("The expense is added!")

def main() -> None:
    tracker = ExpenseTracker()
    while True:
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense_from_user(tracker)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            print("Thank you for using SmartTrackers!")
            break
        else:
            print("Invalid choice! Please enter a valid choice")

if __name__ == '__main__':
    main()