"""Solution for Tuple practice."""
# Create the list ['a', 'b', 'c'], then create a tuple from that list.
source_list = ['a', 'b', 'c']
tuple1 = tuple(source_list)
print('Tuple created from list is', tuple1)
# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
source_tuple = ('a', 'b', 'c')
list1 = list(source_tuple)
print('List created from tuple is', list1)
# Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
a, b, c = 'a', 2, 'gamma'
print('Created variables are:', a, b, c)
# Create a tuple containing just a single element
# which in turn contains the three elements 'a', 'b', and 'c'
tuple3 = source_tuple,
print('Created tuple is', tuple3)
print('The length of this tuple is actually', len(tuple3))
