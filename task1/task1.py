"""Task1: some examples."""
import re

# line 1

print('Hello, world!\n')

# line 2

name = input('What is your name?')
print('Hi, %s.\n' % name)

# line 3

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# line 4

parents, babies = (1, 1)
while babies < 100:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)

# line 5


def greet(name):
    """Print my name."""
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

# line 6


for test_string in ['555-1212', 'ILL-EGAL']:
    if re.match(r'^\d{3}-\d{4}$', test_string):
        print(test_string, 'is a valid US local phone number')
    else:
        print(test_string, 'rejected')
