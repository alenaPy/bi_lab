"""
Task2.

Usages of list comprehensions.
"""

list1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
print("first list - {0} ".format(list1))

# slice list above
list_slice = list1[::2]
print("sliced list - {0}".format(list_slice))


list2 = ['1a', '2a', '3a', '4a']
print("second list - {0}".format(list2))

# pop
print("element from list2 - {0}".format(list2.pop(1)))

list_copy = list2.copy()
print("copied list2 - {0}".format(list2))
list_copy.insert(1, '2a')
print("copied list2 after inserting - {0}".format(list_copy))
