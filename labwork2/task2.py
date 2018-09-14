"""Labwork2."""

# Task2. Purchase money calculation.
M=input('Enter dollars: \n')
N=input('Enter cents: \n')
L=input('Enter number of items: \n')

def cost(M, N, L):
    """Return total cost."""
    c=(int(M) + int(N) / 100)*int(L)
    return c

t=cost(M, N, L)

print('Total cost %.2f%%' % (t))