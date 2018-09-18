"""
Task2.

Usages of list comprehensions.
"""


list1 = [i+j for i in ['a', 'b'] for j in ['b', 'c', 'd']]
print("first list - {0} ".format(list1))

# slice list above
list_slice = list1[::2]
print("sliced list - {0}".format(list_slice))


list2 = [str(i)+'a' for i in range(1, 5)]
print("second list - {0}".format(list2))

# pop
print("element from list2 - {0}".format(list2.pop(1)))

list_copy = list2.copy()
print("copied list2 - {0}".format(list2))
list_copy.insert(1, '2a')
print("copied list2 after inserting - {0}".format(list_copy))
