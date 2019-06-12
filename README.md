## Objective

<img src="https://after-school-assets.s3.amazonaws.com/jerry-mcguire.gif" width="300px" align="right" hspace="10"> We're going to build a `BankAccount` class where two instances of the class can transfer money to each other through a `Transfer` class.

You can't just transfer money to another account without the bank running checks first, and the `Transfer` class acts as a space to check the transaction between two instances of the `BankAccount` class. `Transfer` will do all of this, as well as check the validity of the accounts before the transaction occurs. `Transfer` should be able to reject a transaction if the accounts aren't valid or if the sender doesn't have the money.

### Characteristics of a Bank Account

- A bank account is associated with a user's `name`.
    - The name on the account should not be able to be changed.
- A bank account is opened with a `balance` of exactly $1000.
- A bank account has a `status`, and can be `open`, `closed`, or `broke`.
    - An account is initially always `open`.
- A bank account has a method to `deposit` money into the account. The deposit should change the balance.
- A bank account has a method called `check_balance` that tells the user how much is in their account.
- A bank account has a method to check whether the account `is_valid`.
    - The method returns `true` if the bank account is `open`. If the account is `closed` or `broke`, the method returns `false`.
- A bank account has a method called `close_account` that changes the status to `closed`.

### Characteristics of a Transfer

- A transfer must initialize with a sender, a recipient, and an amount.
- A transfer has a method called `both_valid` that checks whether the transfer is between two valid accounts.
- The `status` of a transfer is always initially `pending`.
    - A transfer's status is `complete` once it has occurred.
    - A transfer's status is `rejected` if the sender doesn't have sufficient funds. If this occurs, the sender gets the message: "Transaction rejected. Please check your account balance."
    - A transfer's status is `reversed` if money is returned from a recipient to a sender, but only for a transfer that was `complete`.
- A transfer has a method called `execute_transaction` that removes money from the sender's account, deposits that same amount of money into the recipient's account, and sets the status of the transfer to `complete`.
- A transfer has a method called `reverse_transfer` that transfers money from a recipient back to a sender.


## Lab

1. Build a new class called `BankAccount` and instantiate a new account for a user named "Avi".
    1. Confirm that Avi's new account is of the type `BankAccount`.
    2. Confirm that the name on Avi's account is "Avi".
    3. Confirm that Avi's account has a balance of $1000.
    4. Confirm that Avi's account is `open`.
    5. Set Avi's balance to $2000. Confirm his new account balance.
2. What other properties might a bank account need? Add three more properties to the `BankAccount` class. 
3. Write a new method for the `BankAccount` class called `deposit` that adds money to the account.
4. Write a new method for the `BankAccount` class called `check_balance` that displays a message to the user indicating their balance.
5. Write a new method for the `BankAccount` class called `is_valid` that determines whether the account is valid (open and with funds) or not.
    1. Instantiate a new account, and set its balance to 0.
    2. Check that the status of the account is `broke`.
    3. Check whether the account is valid.
    4. Instantiate another new account, and set its status to `closed`.
    5. Check whether the account is valid.
6. Write a new method for the `BankAccount` class called `close_account` that closes an account.

### Intermediate 

7. Make a new bank account for "Amanda".
8. Build a new class called `Transfer`, then instantiate a new `Transfer` that sends $50 from Amanda to Avi.
    1. Confirm that the transfer is of the type `Transfer`.
    2. Confirm that the transfer had a sender named Amanda, a recipient named Avi, a status of `pending`, and an amount of $50.
9. Write a new method for the `Transfer` class called `both_valid` that confirms whether both accounts are valid.
    1. Confirm that the transfer of from Amanda to Avi is a valid transaction.
    2. Confirm that the `both_valid` method uses the `valid` method on each `BankAccount`.
10. Write a new method for the `Transfer` class called `execute_transaction` that sets the balance of each account and changes the transfer status to `complete`.
    1. Confirm that the status of the transfer is `complete` after the transaction has taken place, and that the account balances are what you would expect.

### Stretch

11. Use the `Transfer` class to send $4000 from Avi to Amanda.
    1. Confirm that the transfer is `rejected` and display the message "Transaction rejected. Please check your account balance."
12. Write a new method for the `Transfer` class called `reverse_transfer` that reverses the transfer and sets the status to `reversed`.
    1. Confirm that a reversed transaction for $50 from Avi back to Amanda has the status `reversed` and that the account balances are what you would expect.
    2. Confirm that a transfer can only be reversed if it had previously been `completed`.

### Double-Stretch

13. Have you tried to change the name on an account? Do you find it a bit weird that we _could_ just swap in a new name on an account? Explore and implement "getters" and "setters" in order to fix the value of a property. Then try to change the name on an account and see what happens.
