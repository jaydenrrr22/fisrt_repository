from savings_account import SavingsAccount
from checking_account import CheckingAccount

savings1 = SavingsAccount("Jayden", 1000, 100, "ABC123", "DEF456", 0.4)
savings2 = SavingsAccount("Michelle", 500, 50, "GHI789", "JKL012", 0.4)

# testing savings account
savings1.print_customer_information()
print()
savings1.add_interest()
savings1.deposit(300)
savings1.withdraw(500)

print()

savings2.print_customer_information()
print()
savings2.add_interest()
savings2.deposit(400)
savings2.withdraw(200)

print()
checking1 = CheckingAccount("Cole", 800, 150, "ABC234", "DEF567", 500)
checking2 = CheckingAccount("Jean", 400, 100, "GHI123", "JKL456", 300)
# testing checking accounts

checking1.print_customer_information()
print()
checking1.transfer(400)
checking1.withdraw(200)
checking1.transfer(600)
checking1.transfer(400)

print()
checking2.print_customer_information()
print()
checking2.transfer(200)
checking2.withdraw(100)
checking2.transfer(500)
checking2.transfer(300)



