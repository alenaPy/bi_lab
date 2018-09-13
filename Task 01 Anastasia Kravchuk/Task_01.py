"""Task 01."""
# ====================== IMPORT ======================

import re
import sys
import glob
from time import localtime

# ====================== Line 1 ======================

print('Hello, world!')

# ====================== Line 2 ======================

name = input('What is your name?\n')
print('Hi, %s.' % name)

# ====================== Line 3 ===========s===========

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# ====================== Line 4 ======================

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# ====================== Line 5 ======================


def greet(name):
    """Meeting function."""
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

# ====================== Line 6 ======================

for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')

# ====================== Line 7 ======================

prices = {'apple': 0.40, 'banana': 0.50}
my_purchase = {
    'apple': 1,
    'banana': 6}
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print('I owe the grocer $%.2f' % grocery_bill)

# ====================== Line 8 ======================

# This program adds up integers in the command line

try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print('sum =', total)
except ValueError:
    print('Please supply integer arguments')

# ====================== Line 9 ======================

# indent your Python code to put into an email

# glob supports Unix style pathname extensions
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print('    ------' + file_name)

    with open(file_name) as f:
        for line in f:
            print('    ' + line.rstrip())

    print

# ====================== Line 10 ======================


activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting', }

time_now = localtime()
hour = time_now.tm_hour

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print(activities[activity_time])
        break
else:
    print('Unknown, AFK or sleeping!')

# ====================== Line 11 ======================

REFRAIN = '''
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
'''
bottles_of_beer = 99
while bottles_of_beer > 1:
    print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1))
    bottles_of_beer -= 1

# ====================== Line 12 ======================


class BankAccount(object):
    """Bank account class."""

    def __init__(self, initial_balance=0):
        """Initialize object."""
        self.balance = initial_balance

    def deposit(self, amount):
        """Increase balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Decrease balance."""
        self.balance -= amount

    def overdrawn(self):
        """Overdrawn."""
        return self.balance < 0


my_account = BankAccount(15)
my_account.withdraw(5)
print(my_account.balance)
