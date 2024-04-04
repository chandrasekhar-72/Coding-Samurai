import datetime

class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        if date is None:
            self.date = datetime.datetime.now()
        else:
            self.date = date

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        self.expenses.append(Expense(amount, category, description))

    def list_expenses(self):
        for expense in self.expenses:
            print(f"Date: {expense.date.strftime('%Y-%m-%d %H:%M:%S')}, Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}")

    def calculate_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def generate_monthly_report(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if expense.date.month == month and expense.date.year == year]
        category_totals = {}
        for expense in monthly_expenses:
            if expense.category in category_totals:
                category_totals[expense.category] += expense.amount
            else:
                category_totals[expense.category] = expense.amount
        
        print(f"Monthly Report for {month}/{year}:")
        for category, total in category_totals.items():
            print(f"{category}: {total}")

    def save_expenses(self, filename):
        with open(filename, 'w') as file:
            for expense in self.expenses:
                file.write(f"{expense.date},{expense.amount},{expense.category},{expense.description}\n")

    def load_expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    date_str, amount, category, description = line.strip().split(',')
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                    self.expenses.append(Expense(float(amount), category, description, date))
        except FileNotFoundError:
            print(f"File '{filename}' not found. No expenses loaded.")

    def delete_all_expenses(self):
        self.expenses = []
        print("All expenses deleted successfully.")



tracker = ExpenseTracker()
tracker.load_expenses("expenses.txt")

while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Calculate Total Expenses")
    print("4. Generate Monthly Report")
    print("5. Save Expenses")
    print("6. Delete All Expenses")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")
        tracker.add_expense(amount, category, description)
    elif choice == '2':
        tracker.list_expenses()
    elif choice == '3':
        print("Total Expenses:", tracker.calculate_total_expenses())
    elif choice == '4':
        month = int(input("Enter month (1-12): "))
        year = int(input("Enter year: "))
        tracker.generate_monthly_report(month, year)
    elif choice == '5':
        tracker.save_expenses("expenses.txt")
        print("Expenses saved successfully.")
    elif choice == '6':
        tracker.delete_all_expenses()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
