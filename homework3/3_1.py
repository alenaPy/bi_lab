"""ListTask."""


list1 = ['a', 'b', 'c', 'd']
list2 = [fir + la for fir in list1[0:2] for la in list1[1:]]
print(list2)


list3 = list2[0::2]
print(list3)


list4 = ['1', '2', '3', '4']
list5 = [fir + la for fir in list4[0:] for la in list1[0]]
print(list5)


list6 = list5.pop(1)
print(list6)


list7 = list5.copy()
print(list7)


list7.insert(1, '2a')
print(list7)
