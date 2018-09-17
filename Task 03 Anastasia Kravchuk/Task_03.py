"""Task 03."""

"""1) List practice."""


# 1. Use a list comprehension to construct the list ['ab', 'ac', 'ad', 'bb',
# 'bc', 'bd'].
list1 = [('{0}{1}'.format(x, y)) for x in ['a', 'b'] for y in ['b', 'c', 'd']]

# 2. Use a slice on the above list to construct the list ['ab', 'ad', 'bc'].
list2 = list1[0:len(list1):2]

# 3. Use a list comprehension to construct the list ['1a', '2a', '3a', '4a'].
list3 = [('{0}a'.format(x)) for x in range(1, 5)]

# 4. Simultaneously remove the element '2a' from the above list and print it.

print(" list3 with removed element '2a' : ", list3.pop(list3.index('2a')))

# 5. Copy the above list and add '2a' back into the list such that the original
#  is still missing it.
list4 = list3[:]
list4.insert(1, '2a')


"""2) Tuple practice."""

# 1. Create the list ['a', 'b', 'c'], then create a tuple from that list.

list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)

# 2. Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
# (Hint: the material needed to do this has been covered, but it's not
# entirely obvious)

tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
# [list(i) for i in tuple2]

# 3. Make the following instantiations simultaneously: a = 'a', b=2, c='gamma'.
#  (That is, in one line of code).
a, b, с = 'a', 2, 'gamma'


# 4. Create a tuple containing just a single element which in turn contains
# the three elements 'a', 'b', and 'c'. Verify that the length is actually 1
# by using the len() function.

tuple4 = (tuple2,)
len(tuple4)


"""3) Dictionary practice."""

# 1. Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included) and the values
# are square of keys. n – function argument. Default is 20.


def generate_numbers(number=20):
    """Generate dictionary: {number, number^2}."""
    return {i: i ** 2 for i in range(1, number+1)}


generate_numbers()

generate_numbers(18)

# 2. Define a function count_characters(count_me_string) which count and return
# the numbers of each character in a count_me_string argument


def cogenerate_numbers(count_me_string):
    """Generate dictionary: {symbol, number of said symbol in string}."""
    return {i: sum(x is i for x in count_me_string) for i in
            sorted(set(list(count_me_string)))}


cogenerate_numbers("3223  reh! erg NrR")
cogenerate_numbers("nuyn 45gfh")
cogenerate_numbers("abcdefgabc")

"""4) Module and Functions practice."""

# pytasks.py and runner.py are placed in the current folder
