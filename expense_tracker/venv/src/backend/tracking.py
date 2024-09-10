class ExpenseTracker:
    def __init__(self):
        # create an empty list to store expenses
        self.expenses = []

    def add_expense(self, expense):
        # add an expense to the list of expenses
        self.expenses.append(expense)

    def expenses_by_category(self):
        categories = {}
        for expense in self.expenses:
            if expense.category not in categories:
                categories[expense.category] = 0
            categories[expense.category] += expense.amount
        return categories
    
    def total_expense_by_category(self, category):
        # return the sum of all the expenses in a particular category
        return sum(expense.amount for expense in self.expenses if expense.category == category)
    
    def total_expense(self):
        # return the sum of all the expenses
        return sum(expense.amount for expense in self.expenses)
    
    def total_expense_by_date(self, date):
        # return the sum of all the expenses on a particular date
        return sum(expense.amount for expense in self.expenses if expense.date == date)
    def view_expenses(self):
        # print all the expenses
        for expense in self.expenses:
            print(f"Amount: {expense.amount}CAD")
            print(f"Category: {expense.category}")
            print(f"Date: {expense.date}")
            print(f"Description: {expense.description}")
            print()