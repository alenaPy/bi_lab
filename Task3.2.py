"""TuplePractice."""


list1 = ['a', 'b', 'c']
tup1 = tuple(list1)
print(tup1)


tup2 = ('a', 'b', 'c')
list2 = list(tup2)
print(list2)


a, b, c = 'a', 2, 'gamma'
print(a, b, c)

tup3 = (tup2,)
print(len(tup3))
