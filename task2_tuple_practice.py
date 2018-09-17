"""
Task2.

Usages of tuple comprehensions.
"""

list1 = ['a', 'b', 'c']

# tuple from list
tup = tuple(list1)
print("tuple from list - {0}".format(tup))

# list from tuple
tuple1 = ('a', 'b', 'c')
list1 = list(tuple1)
print("list from tuple - {0}".format(list1))

a, b, c = 'a', 2, 'gamma'
tuple2 = (('a', 'b', 'c'), )
print("tuple with one element - {0}".format(tuple2,len(tuple2)))
