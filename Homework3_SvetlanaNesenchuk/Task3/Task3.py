"""List practice point1."""
letters = ['a', 'b', 'c', 'd']
list0 = [first_letter + second_letter
         for first_letter in letters[:2] for second_letter in letters[1:]]
print(list0)
"""List practice point2"""
list1 = list0[::2]
print(list1)
"""List practice point3"""
list2 = ['1', '2', '3', '4', 'a']
list3 = [first_letter + second_letter for first_letter in list2[:4]
         for second_letter in list2[4:]]
print(list3)
"""List practice point4"""
a = list3.pop(1)
print(a)
""""List practice point5"""
print(list3)
list4 = list3[:]
list4.insert(1, a)
print(list4)
""""Tuple practice point1"""
lst = ['a', 'b', 'c']
tuple1 = tuple(lst)
print(tuple1)
"""Tuple practice point2"""
tuple2 = ('a', 'b', 'c')
list5 = list(tuple2)
print(list5)
"""Tuple practice point3"""
x, y, z = 'a', 2, 'gamma'
print(x)
print(y)
print(z)
"""Tuple practice point4"""
tuple3 = (list5,)
print(tuple3)
print(len(tuple3))
"""Dictionary practice point1"""


def generate_numbers(n=20):
    """Generate keys and their squares as values."""
    return {i: i ** 2 for i in range(1, n + 1)}


print(generate_numbers())

"""Dictionary practice point1"""


def count_character(count_me_string):
    """Count characters in specified string."""
    dict_1 = {}
    for i in count_me_string:
        count_me_string.count(i)
        dict_1.update({i: count_me_string.count(i)})
    return dict_1


print(count_character("ababababctc"))
