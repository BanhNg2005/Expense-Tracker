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
        category = input("Enter the category (Food, Transport, Entertainment, Bills, Others): ").strip().lower()
        if category not in ["food", "transport", "entertainment", "bills", "others"]:
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
    
    # Create an Expense object, which will validate the inputs
    expense = Expense(amount, category, date, description)
    tracker.add_expense(expense)  # Add the expense to the tracker
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
            print("Choose the option to view expenses: ")
            print("1. View all expenses")
            print("2. View expenses by category")
            print("3. View total expenses")
            print("4. View total expenses by category")
            print("5. View total expenses by date")
            view_choice = input("Enter your choice: ")
            if view_choice == "1":
                tracker.view_expenses()
            elif view_choice == "2":
                category = input("Enter the category: ")
                print(tracker.total_expense_by_category(category))
            elif view_choice == "3":
                print(tracker.total_expense())
            elif view_choice == "4":
                category = input("Enter the category (Food, Transport, Entertainment, Bills, Others): ")
                print(tracker.total_expense_by_category(category))
            elif view_choice == "5":
                date = input("Enter the date (YYYY-MM-DD): ")
                print(tracker.total_expense_by_date(date))
            else:
                print("Invalid choice! Please enter a valid choice")
        elif choice == "3":
            print("Thank you for using SmartTrackers!")
            break
        else:
            print("Invalid choice! Please enter a valid choice")

if __name__ == '__main__':
    main()