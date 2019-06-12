

### Objective
<img src="https://after-school-assets.s3.amazonaws.com/jerry-mcguire.gif" width="300px" align="right" hspace="10"> We're going to build a `BankAccount` class where two instances of the class can transfer money to each other through a `Transfer` class.

You can't just transfer money to another account without the bank running checks first, and the `Transfer` class acts as a space to check the transaction between two instances of the `BankAccount` class. `Transfer` will do all of this, as well as check the validity of the accounts before the transaction occurs. `Transfer` should be able to reject a transaction if the accounts aren't valid or if the sender doesn't have the money.

### Characteristics of a Bank Account

- A bank account is associated with a user's `name`.
- The name on the account cannot be changed.
- A bank account is opened with exactly $1000.
- A bank account has a status, and can be `open`, `closed`, or `broke`. An account is initially always `open`.
- A `valid` bank account is `open`. If the account is `closed` or `broke`, the account is `invalid`.
- You can deposit money into an account. The deposit should change the balance.

### Characteristics of a Transfer

- A transfer must initialize with a sender, a recipient, and an amount.
- A transfer is always initially `pending`.
- A transfer must only be between two valid accounts.
- A transfer can execute successfully by removing money from the sender's account and depositing that same amount of money into the recipient's account.
- A transfer's status is `complete` once it has occurred.
- A transfer's status is `rejected` if the sender doesn't have sufficient funds. If this occurs, the sender gets the message: "Transaction rejected. Please check your account balance."
- A transfer's status is `reversed` if money is returned from a recipient to a sender, but only for a transfer that was `complete`.

### Lab

1. Use your `BankAccount` class and instantiate a new Bank Account for a user named "Avi".
    1. Confirm that Avi's new account is of the type `BankAccount`.
    2. Confirm that the name on Avi's account is "Avi".
    3. Confirm that Avi's account has a balance of $1000.
    4. Confirm that Avi's account is `open`.
    5. Confirm that you can't change the name on Avi's account to "Bob".
2. Write a new method for the `BankAccount` class called `deposit` that adds money to the account.
3. Write a new method for the `BankAccount` class that displays a message to the user indicating their balance.
4. Write a new method for the `BankAccount` class that determines whether the account is `valid` (open and with funds) or not.
    1. Instantiate a new account, and set its balance to 0.
    2. Check that the status of the account is `broke`.
    3. Check whether the account is valid.
    4. Instantiate a new account, and set its status to `closed`.
    5. Check whether the account is valid.
5. Write a new method for the `BankAccount` class called `close_account` that closes an account.
6. Make a new bank account for "Amanda".
7. Use the `Transfer` class to send $50 from Amanda to Avi.
    1. Confirm that the transfer is of the type `Transfer`.
    2. Confirm that the transfer had a sender named Amanda, a recipient named Avi, a status of `pending`, and an amount of $50.
8. Write a new method for the `Transfer` class called `both_valid` that confirms whether both accounts are valid.
    1. Confirm that the transfer of from Amanda to Avi is a valid transaction.
    2. Confirm that the `both_valid` method uses the `valid` method on each `BankAccount`.
9. Write a new method for the `Transfer` class called `execute_transaction` that sets the balance of each account and changes the transfer status to `complete`.
    1. Confirm that the status of the transfer is `complete` after the transaction has taken place, and that the account balances are what you would expect.
10. Use the `Transfer` class to send $4000 from Avi to Amanda.
    1. Confirm that the transfer is `rejected` and display the message "Transaction rejected. Please check your account balance."
11. Write a new method for the `Transfer` class called `reverse_transfer` that reverses the transfer and sets the status to `reversed`.
    1. Confirm that a reversed transaction for $50 from Avi back to Amanda has the status `reversed` and that the account balances are what you would expect.
    2. Confirm that a transfer can only be reversed if it had previously been `completed`.
