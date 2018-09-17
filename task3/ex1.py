"""List practice."""

'''1.Use a list comprehension to construct the list
['ab', 'ac', 'ad', 'bb', 'bc', 'bd']'''

list1 = ['a', 'b']
list2 = ['b', 'c', 'd']
res1 = [x1 + x2 for x1 in list1 for x2 in list2]
print('1.', res1)

'''2.Use a slice on the above list to construct the list ['ab', 'ad', 'bc']'''

print('2.', res1[::2])

'''3.Use a list comprehension to construct the list ['1a', '2a', '3a', '4a']'''

res3 = [str(i) + 'a' for i in range(1, 5)]
print('3.', res3)

'''4.Simultaneously remove the element '2a' from the above list and print it'''

ix4 = res3.index('2a')
el4 = res3.pop(ix4)
print('4.', el4, '; List:', res3)

'''5.Copy the above list and add '2a' back into the list
such that the original is still missing it'''

res5 = res3.copy()
res5.insert(ix4, el4)
print('5. A copy with the restored element:', res5,
      '; Original, the element is still absent:', res3)
