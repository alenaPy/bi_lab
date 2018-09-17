"""List practice."""

# 1. Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
lst = [('{0}{1}'.format(x, y)) for x in ['a', 'b'] for y in ['b', 'c', 'd']]
print(lst)

# 2. Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
print(lst[::2])

# 3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
lst = [('{0}{1}'.format(x, y)) for x in range(1, 5) for y in ['a']]
print(lst)

# 4. Simultaneously remove the element '2a' from the above list and print it.
lst.remove('2a')
print(lst)

# 5. Copy the above list and add '2a' back into the list such that the original
# is still missing it.
new_list = lst[:]
new_list.append('2a')
print(new_list)
print(lst)
