"""Labwork2."""

# Task2. Purchase money calculation.
M = input('Enter dollars: \n')
N = input('Enter cents: \n')
L = input('Enter number of items: \n')


def cost(m, n, l):
    """Return total cost."""
    c = (int(m) + int(n) / 100) * int(l)
    return c


t = cost(M, N, L)

print('Total cost %.2f%%' % t)
