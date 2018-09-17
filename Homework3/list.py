"""Solution for List practice."""
# Use a list comprehension to construct the list
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
letters = ['a', 'b', 'c', 'd']
list1 = [first_letter + second_letter
         for first_letter in letters[:2] for second_letter in letters[1:]]
print('List1 is', list1)
# Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
odd_elements = list1[::2]
print('Odd elements of List1 are', odd_elements)
# Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
list2 = [str(digit) + 'a' for digit in range(1, 5)]
print('List2 is', list2)
# Simultaneously remove the element '2a' from the above list and print it.
list3 = list2.pop(1)
print('Removed element from List2 is', list3)
# Copy the above list and add '2a' back into the list
# such that the original is still missing it.
list4 = list2[:]
list4.insert(1, '2a')
print('List with the previously removed element is', list4)
print('Previous list is', list2)
