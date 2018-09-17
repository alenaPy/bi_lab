"""TupleTask."""


list1 = ['a', 'b', 'c']
tup1e1 = tuple(list1)
print(tup1e1)


tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print(list2)


a, b, c = 'a', 2, 'gamma'
print(a, b, c)


tuple3 = (tuple2,)
print('Len is ', len(tuple3))
