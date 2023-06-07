import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Amount: {self.amount}\nCategory: {self.category}\nDescription: {self.description}\nDate: {self.date}"


class ExpenseTracker:
    def __init__(self):
        self.users = []
        self.expenses = []
        self.logged_in = False
        self.current_user = None

    def register_user(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        user = User(username, password)
        self.users.append(user)
        print("User registered successfully.")

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_in = True
                self.current_user = user
                print("Login successful.")
                return

        print("Invalid username or password.")

    def logout(self):
        self.logged_in = False
        self.current_user = None
        print("Logged out successfully.")

    def add_expense(self):
        if not self.logged_in:
            print("Please log in to add an expense.")
            return

        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        description = input("Enter expense description: ")

        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(self.expenses, start=1):
                print(f"\nExpense {i}")
                print(expense)

    def run(self):
        while True:
            print("\n===== Expense Tracker Menu =====")
[O            print("1. Register user")
            print("2. Login")
            print("3. Logout")
            print("4. Add expense")
            print("5. View expenses")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                self.login()
            elif choice == "3":
                self.logout()
            elif choice == "4":
                self.add_expense()
            elif choice == "5":
                self.view_expenses()
            elif choice == "6":
                print("Exiting the Expense Tracker.")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the app
app = ExpenseTracker()
app.run()

