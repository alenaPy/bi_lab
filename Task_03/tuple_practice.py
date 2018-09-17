"""Tuple practice."""

# 1. Create the list ['a', 'b', 'c'], then create a tuple from that list.
lst = ['a', 'b', 'c']
lst = tuple(lst)
print(lst)

# 2. Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
tpl = ('a', 'b', 'c')
tpl = list(tpl)
print(tpl)

# 3. Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
a, b, c = 'a', 2, 'gamma'

# 4. Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'. Verify that the length is actually 1
# by using the len() function.
tpl1 = (tpl,)
print(len(tpl1))
