"""Easy Unpack.

Get an tuple and returns a tuple with 3 elements - first, third and
second to the last for the given array.
"""

# https://py.checkio.org/en/mission/easy-unpack/


def easy_unpack(arg):
    """Return 1st, 3rd and second to the last elements of the given array."""
    if len(arg) < 3:
        raise Exception("The length of a list/tuple must be greater than 2")
    res = (arg[0], arg[2], arg[-2])
    return tuple(res)


input_val = input('Please input comma separated strings/numbers/characters: ')
sep_list = input_val.split(",")
tpl = tuple(sep_list)
res = easy_unpack(tpl)
print('easy_unpack test: ', res)
