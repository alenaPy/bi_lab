"""The Most Frequent."""

# https://py.checkio.org/en/mission/the-most-frequent/


def most_frequent(list_arg):
    """You have a sequence of strings.

    And you’d like to determine
    the most frequently occurring string in the sequence.
    """
    if type(list_arg) is not list:
        raise Exception("Invalid argument type")

    '''str_num = {}
    for str in list_arg:
        if str in str_num:
            continue
        str_num[str] = list_arg.count(str)

    for str in str_num.keys():
        if str_num[str] == max(str_num.values()):
            return str'''
    # i like this variant more
    return max(list_arg, key=lambda x: list_arg.count(x))


input_val = input('Please input comma separated strings: ')
str_list = input_val.split(",")
print(most_frequent(str_list))
