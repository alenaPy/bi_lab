"""Task 1."""

# Task 1.1
lst = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']


# Task 1.2
lst2 = (lst[::2])


# Task 1.3
lst3 = ['1a', '2a', '3a', '4a']


# Task 1.4
print('The removed element is: %s' % lst3.pop(1))
print('LIST3: %s' % lst3)


# Task 1.5
lst5 = lst3[:]
lst5.insert(1, '2a')
print('LIST3: %s' % lst3)
print('LIST5: %s' % lst5)


