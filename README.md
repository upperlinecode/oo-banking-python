## Objective

<img src="https://after-school-assets.s3.amazonaws.com/jerry-mcguire.gif" width="300px" align="right" hspace="10"> We're going to build a `BankAccount` class where two instances of the class can transfer money to each other through a `Transfer` class.

You can't just transfer money to another account without the bank running checks first, and the `Transfer` class acts as a space to check the transaction between two instances of the `BankAccount` class. `Transfer` will do all of this, as well as check the validity of the accounts before the transaction occurs. `Transfer` should be able to reject a transaction if the accounts aren't valid or if the sender doesn't have the money.

## Lab

A bank account:
- is associated with a user's `name`.
- is opened with a `balance` of exactly $1000.
- has a `status`, and can be `open`, `closed`, or `zero`. An account is initially always `open`.

> _Note: The name on the account should not be able to be changed, but we're going to ignore that for now._

1. Build a new class called `BankAccount` and instantiate a new account for a user named "Kiran".
    1. Confirm that Kiran's new account is of the type `BankAccount`.
    2. Confirm that the name on Kiran's account is "Kiran".
    3. Confirm that Kiran's account has a balance of $1000.
    4. Confirm that Kiran's account is `open`.
    5. Set Kiran's balance to $2000. Confirm his new account balance.

2. What other properties might a bank account need? Add three more properties to the `BankAccount` class. 

3. Write a new method for the `BankAccount` class called `deposit` that adds money to the account.

4. Write a new method for the `BankAccount` class called `check_balance` that displays a message to the user indicating their balance.

5. Write a new method for the `BankAccount` class called `is_valid` that determines whether the account is valid (open and with funds) or not. The method returns `true` if the bank account is `open`. If the account is `closed` or `zero`, the method returns `false`.
    1. Instantiate a new account, and set its balance to 0.
    2. Check that the status of the account is `zero`.
    3. Check whether the account is valid.
    4. Instantiate another new account, and set its status to `closed`.
    5. Check whether the account is valid.

6. Write a new method for the `BankAccount` class called `close_account` that closes an account.

### Intermediate 

7. Make a new bank account for "Amanda".
8. Build a new class called `Transfer` that initializes with a sender, a recipient, and an amount. Then instantiate a new `Transfer` that sends $50 from Amanda to Kiran.
    1. Confirm that the transfer is of the type `Transfer`.
    2. Confirm that the transfer had a sender named Amanda, a recipient named Kiran, and an amount of $50.
9. Write a new method for the `Transfer` class called `both_valid` that confirms whether both accounts are valid.
    1. Confirm that the transfer from Amanda to Kiran is a valid transaction.
    2. Confirm that the `both_valid` method uses the `valid` method on each `BankAccount`.
10. Add a property to the `Transfer` class called `status`:
    - The `status` of a transfer is always initially `pending`. 
    - A transfer's status is `complete` once it has occurred.
    - A transfer's status is `rejected` if the sender doesn't have sufficient funds. If this occurs, the sender gets the message: "Transaction rejected. Please check your account balance."
    - A transfer's status is `reversed` if money is returned from a recipient to a sender, but only for a transfer that was `complete`.
11. Write a new method for the `Transfer` class called `execute_transaction` that removes money from the sender's account, deposits that same amount of money into the recipient's account, and sets the status of the transfer to `complete`.
    1. Confirm that the status of the transfer is `complete` after the transaction has taken place, and that the account balances are what you would expect.

### Stretch

11. Use the `Transfer` class to send $4000 from Kiran to Amanda.
    1. Confirm that the transfer is `rejected` and display the message "Transaction rejected. Please check your account balance."
12. Write a new method for the `Transfer` class called `reverse_transfer` that reverses the transfer and sets the status to `reversed`.
    1. Confirm that a reversed transaction for $50 from Kiran back to Amanda has the status `reversed` and that the account balances are what you would expect.
    2. Confirm that a transfer can only be reversed if it had previously been `completed`.

### Double-Stretch

13. Have you tried to change the name on an account? Do you find it a bit weird that we _could_ just swap in a new name on an account? Explore and implement "getters" and "setters" in order to fix the value of a property. Then try to change the name on an account and see what happens.
