from backAccount import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self._interest_rate = interest_rate
        # self._account_number = account_number
        # self._routing_number = routing_number

    def add_interest(self):
        interest = self._customerBalance * self._interest_rate / 100
        self._customerBalance += interest
        print(f"{self._customerName} earned {interest:.2f} interest in your savings account. New balance: {self._customerBalance:.2f} ")

