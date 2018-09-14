"""Easy Unpack."""

# https://py.checkio.org/en/mission/easy-unpack/


def easy_unpack(tuple_arg):
    """Get an tuple and returns a tuple with 3 elements - first, third.

    And second to the last for the given array.
    """
    if type(tuple_arg) is not tuple:
        raise Exception("Invalid argument type")
    res = (tuple_arg[0], tuple_arg[2], tuple_arg[-2])
    return tuple(res)


input_val = input('Please input comma separated strings/numbers/characters: ')
sep_list = input_val.split(",")
tpl = tuple(sep_list)
res = easy_unpack(tpl)
print(res)
