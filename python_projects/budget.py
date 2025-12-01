class BudgetPlan:
    def __init__(self, salary=25000):
        self.salary = salary
        self.grocery_amt = 0
        self.rent_amt = 0
        self.electricity_amt = 0

    def grocery(self, grocery=5000):
        self.grocery_amt = grocery
        return f"The grocery expense: {self.grocery_amt}"

    def rent(self, rent=6000):
        self.rent_amt = rent
        return f"Your rent is: {self.rent_amt}"

    def electricity(self, bill=500):
        self.electricity_amt = bill
        return f"Your electricity bill is: {self.electricity_amt}"

    def total_expenses(self):
        total = self.grocery_amt + self.rent_amt + self.electricity_amt
        return f"Total expenses: {total}"

    def remain_balance(self):
        remain = self.salary - (self.grocery_amt + self.rent_amt + self.electricity_amt)
        return f"Remaining balance: {remain}"


# Create an instance of BudgetPlan
budget = BudgetPlan()

while True:
    print("\n=== Budget Plan ===")
    print("1. Grocery")
    print("2. Rent")
    print("3. Electricity")
    print("4. Total Expenses")
    print("5. Remaining Balance")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = int(input("Enter grocery amount: "))
        print(budget.grocery(amount))
    elif choice == '2':
        amount = int(input("Enter rent amount: "))
        print(budget.rent(amount))
    elif choice == '3':
        amount = int(input("Enter electricity bill: "))
        print(budget.electricity(amount))
    elif choice == '4':
        print(budget.total_expenses())
    elif choice == '5':
        print(budget.remain_balance())
    elif choice == '6':
        print("Goodbye! This is your budget plan.")
        break
    else:
        print("Invalid option. Try again.")
