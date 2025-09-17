class BankAccount:
    bank_title = "Chase Bank"

    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number):
        self._customerName = customer_name
        self._customerBalance = customer_balance
        self._minBalance = minimum_balance
        self.__account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        if amount > 0:
            self._customerBalance += amount
            print(f"{self._customerName} deposited {amount}. Current balance: {self._customerBalance}")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be positive")
        if self._customerBalance - amount < self._minBalance:
            print("Withdraw cannot be less than minimum balance")
        else:
            self._customerBalance -= amount
            print(f"{self._customerName} withdrawed {amount}. Current balance: {self._customerBalance}")

    def print_customer_information(self):
        print(f"Bank Name: {BankAccount.bank_title}")
        print(f"Customer Name: {self._customerName}")
        print(f"Customer Balance: {self._customerBalance}")
        print(f"Minimum Balance: {self._minBalance}")

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