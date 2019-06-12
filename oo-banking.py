
# 1. Build a new class called `BankAccount`...
class BankAccount:
    pass # delete this line when you're ready to build the BankAccount class



#  ... and instantiate a new account for a user named "Kiran".
kiran_account = BankAccount("Kiran")

# i. Confirm that Kiran's new account is of the type `BankAccount`.
print(type(kiran_account))

# ii. Confirm that the name on Kiran's account is "Kiran".
print(kiran_account.name)

# iii. Confirm that Kiran's account has a balance of $1000.
print(kiran_account.balance)

# iv. Confirm that Kiran's account is `open`.
print(kiran_account.status)

# v. Set Kiran's balance to $2000. Confirm his new account balance.
kiran_account.balance = 2000
print(kiran_account.balance)

# Now you're on your own to write tests for the rest...


class Transfer:
    pass # delete this line when you're ready to build the Transfer class

