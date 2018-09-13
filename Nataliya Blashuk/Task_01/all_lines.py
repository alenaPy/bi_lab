"""File with simple examples."""
# 1 lines: Output
print('Hello, world!')

# 2 line: Input, assignment
name = input('What is your name?\n')
print('Hi, %s.' % name)

# 3 lines: For loop, built-in enumerate function, new style formatting
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# 4 lines: Fibonacci, tuple assignment
parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)


# 5 lines: Functions
def greet(name):
    """Greet prints greetings."""
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')


# 12 lines: Classes
class BankAccount(object):
    """Class provides information about bank account."""

    def __init__(self, initial_balance=0):
        """Bank account balance."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Bank account deposit."""
        self.balance += amount

    def withdraw(self, amount):
        """Bank account withdraw."""
        self.balance -= amount

    def overdrawn(self):
        """Bank account overdrawn."""
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)
