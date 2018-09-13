"""Printing the number of children in Fibonacci sequence."""
parents, babies = (1, 1)
while babies < 150:
    print('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)
