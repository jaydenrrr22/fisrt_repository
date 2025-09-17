class BankAccount:
    bank_title = "Chase Bank"

    def __init__(self, customer_name, customer_balance, minimum_balance):
        self.customerName = customer_name
        self.customerBalance = customer_balance
        self.minBalance = minimum_balance

    def deposit(self, amount):
        if amount > 0:
            self.customerBalance += amount
            print(f"{self.customerName} deposited {amount}. Current balance: {self.customerBalance}")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be positive")
        if self.customerBalance - amount < self.minBalance:
            print("Withdraw cannot be less than minimum balance")
        else:
            self.customerBalance -= amount
            print(f"{self.customerName} withdrawed {amount}. Current balance: {self.customerBalance}")

    def print_customer_information(self):
        print(f"Bank Name: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customerName}")
        print(f"Customer Balance: {self.customerBalance}")
        print(f"Minimum Balance: {self.minBalance}")


print()
account1 = BankAccount("Jayden", 1000, 100)
account1.print_customer_information()
account1.deposit(2000)
account1.deposit(-500)
account1.withdraw(1500)
account1.withdraw(5000)
print()

account2 = BankAccount("Cole", 500, 200)
account2.print_customer_information()
account2.deposit(300)
account2.deposit(-500)
account2.withdraw(800)
account2.withdraw(200)