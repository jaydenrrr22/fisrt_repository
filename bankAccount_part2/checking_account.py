from backAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, customer_balance, minimum_balance, account_number, routing_number)
        self._transfer_limit = transfer_limit

    def transfer(self, amount):
        if amount <= 0:
            print("Transfer must be positive")
        elif amount > self._transfer_limit:
            print(f"Transfer exceeds limit of {self._transfer_limit}")
        elif self._customerBalance - amount < self._minBalance:
            print(f"Transfer exceeds minimum balance of {self._minBalance}")
        else:
            self._customerBalance = self._customerBalance - amount
            print(f"{self._customerName} transferred ${amount}. Current Balance: ${self._customerBalance}")

    # def set_transferLimit(self, amount):
    #     transfer_limit = amount
    #     if transfer_limit > self._customer_balance: