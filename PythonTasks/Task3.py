"""Homework3 results."""
import collections
# Task1.1
list1 = [x + y for x in ['a', 'b'] for y in ['b', 'c', 'd']]
print(list1)
# Task1.2
print(list1[0:5:2])
# Task1.3
list1 = [str(x) + y for x in [1, 2, 3, 4] for y in ['a']]
print(list1)
# Task1.4
del list1[1]
print(list1)
# Task1.5
list2 = list1[:]
print(list2)
list2.insert(1, '2a')
print(list2)
# Task2.1
list3 = ['a', 'b', 'c']
t = tuple(list3)
print(t)
# Task2.2
list3 = list(t)
print(list3)
# Task2.3
a, b, c = ('a', 2, 'gamma')
print(a, b, c)
# Task2.4
t2 = (t,)
print(t2)
len(t2)


# Task3.1
def generate_numbers(n):
    """Numbers generation."""
    d = dict()
    for x in range(1, n):
        d[x] = x ** 2
    return [d]


print(generate_numbers(20))
# Task3.2


def count_characters(str):
    """Characters calculation."""
    d = collections.defaultdict(int)
    for letter in str:
        d[letter] += 1
    return[sorted(d.items())]


print(count_characters('abcdefgabc'))
# Task4.1
