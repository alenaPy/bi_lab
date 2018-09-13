"""Task1."""
# 1
print('Hello, world!')

# 2
name = input('What is your name?\n')
print('Hi, %s.' % name)

# 3
friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# 5


def greet(name):
    """Print name."""
    print('Hello', name)


greet('Jack')
greet('Jill')
greet('Bob')

# 11
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
