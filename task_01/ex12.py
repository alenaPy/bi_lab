"""Classes."""


class BankAccount(object):
    """Store bank account information."""

    def __init__(self, initial_balance=0):
        """Set initial balance equal 0."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Increase balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Decrease balance."""
        self.balance -= amount

    def overdrawn(self):
        """Check whether the balance is null."""
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)
