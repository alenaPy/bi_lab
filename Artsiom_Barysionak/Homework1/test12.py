"""Counting balance."""


class BankAccount(object):
    """Class containing functions applying changes to balance."""

    def __init__(self, initial_balance=0):
        """Initializy balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Apply deposit."""
        self.balance += amount

    def withdraw(self, amount):
        """Apply withdraw."""
        self.balance -= amount

    def overdrawn(self):
        """Count balance."""
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(5)
print('Account balance is', my_account.balance, '$')
