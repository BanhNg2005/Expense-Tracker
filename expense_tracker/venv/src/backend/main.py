from expense_tracker.venv.src.backend.expense import Expense, ExpenseTracker
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
tracker = ExpenseTracker()

print(f"Total expenses: {tracker.total_expense()}CAD")
print(f"Expenses by category: {tracker.expenses_by_category()}")
print(f"Total expense for Food: {tracker.total_expense_by_category('Food')}CAD")
print(f"Total expense for Transport: {tracker.total_expense_by_category('Transport')}CAD")
print(f"Total expense for Entertainment: {tracker.total_expense_by_category('Entertainment')}CAD")
print(f"Total expense for Bills: {tracker.total_expense_by_category('Bills')}CAD")


# Extract and print the date for the Food category
food_expenses = [expense for expense in tracker.expenses if expense.category == 'Food']
if food_expenses:
    date = food_expenses[0].date
    print(f"Total expense for Food: {tracker.total_expense_by_category('Food')}CAD on {date}")
else:
    print("No Food expenses found.")

def main() -> None:
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