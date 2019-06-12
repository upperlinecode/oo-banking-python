
# 1. Build a new class called `BankAccount`...
class BankAccount:
    pass # delete this line when you're ready to build the BankAccount class



#  ... and instantiate a new account for a user named "Avi".
avi = BankAccount("Avi")

# i. Confirm that Avi's new account is of the type `BankAccount`.
print(type(avi))

# ii. Confirm that the name on Avi's account is "Avi".
print(avi.name)

# iii. Confirm that Avi's account has a balance of $1000.
print(avi.balance)

# iv. Confirm that Avi's account is `open`.
print(avi.status)

# v. Set Avi's balance to $2000. Confirm his new account balance.
avi.balance = 2000
print(avi.balance)

# Now you're on your own for the rest...


class Transfer:
    pass # delete this line when you're ready to build the Transfer class

