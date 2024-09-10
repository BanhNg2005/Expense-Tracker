from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    # Getter
    @property 
    def category(self):
        return self._category
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def date(self):
        return self._date
    
    @property
    def description(self):
        return self._description
    
    # Setter
    @category.setter
    def category(self, category):
        if category not in ["Food", "Transport", "Entertainment", "Bills", "Others"]:
            raise ValueError("Invalid category")
        self._category = category

    @amount.setter
    def amount(self, amount):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Invalid amount")
        self._amount = amount

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            try:
                datetime.strptime(date, "%Y-%m-%d")
                self._date = date
            except ValueError:
                raise ValueError("Invalid date format, should be YYYY-MM-DD")
        else:
            raise TypeError("date must be a string in the format YYYY-MM-DD")


    @description.setter
    def description(self, description):
        if not description:
            raise ValueError("Missing description")
        self._description = description
