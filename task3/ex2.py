"""Tuple practice."""

'''1.Create the list ['a', 'b', 'c'], then create a tuple from that list'''

res1 = tuple(['a', 'b', 'c'])
print('1.', res1)

'''2.Create the tuple ('a', 'b', 'c'), then create a list from that tuple'''

print('2.', list(res1))

'''3.Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
(That is, in one line of code).'''

print('3.', ('a', 2, 'gamma'))

'''4.Create a tuple containing just a single element which in turn contains
the three elements 'a', 'b', and 'c'.
Verify that the length is actually 1 by using the len() function.'''

res4 = (('a', 'b', 'c'),)
print('4.', len(res4))
