"""Print a string."""


class BankAccount(object):
    """Print a string."""
    def __init__(self, initial_balance=0):
        """Print a string."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Print a string."""
        self.balance += amount

    def withdraw(self, amount):
        """Print a string."""
        self.balance -= amount

    def overdrawn(self):
        """Print a string."""
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)
