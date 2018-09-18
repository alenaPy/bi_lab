"""Labwork3 Natallia Haisionak."""

# 1

list1 = [x + y for x in('a', 'b') for y in('b', 'c', 'd')]
list2 = list1[0:0:2]
list3 = [str(x) + y for x in [1, 2, 3, 4] for y in ['a']]
print(list3.pop(1))
list4 = list3[:]
list4.insert(1, '2a')
print(list3)
print(list4)

# 2

list5 = ['a', 'b', 'c']
t1 = tuple(list5)
list6 = list(t1)
print(t1)
a, b, c = 'a', 2, 'gamma'
t2 = (t1,)
print(len(t2))

# 3


def generate_numbers(n=20) ->dict:
    """Return dictionary key 1-n, value - square of key."""
    return {x: x ** 2 for x in range(1, n + 1, 1)}


print(generate_numbers())


def count_characters(count_me_string) ->dict:
    """Count and return numbers of each character."""
    return {x: count_me_string.count(x) for x in count_me_string}


print(count_characters('abcdefgabc'))
