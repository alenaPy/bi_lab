"""The Most Frequent.

You have a sequence of strings and you’d like to determine
the most frequently occurring string in the sequence.
"""

# https://py.checkio.org/en/mission/the-most-frequent/


def most_frequent(arg):
    """Determine the most frequently occurring string in the sequence."""
    '''str_num = {}
    for str in arg:
        if str in str_num:
            continue
        str_num[str] = arg.count(str)

    for str in str_num.keys():
        if str_num[str] == max(str_num.values()):
            return str'''
    # i like this variant more
    return max(arg, key=lambda x: arg.count(x))


input_val = input('Please input comma separated strings: ')
str_list = input_val.split(",")
print("most_frequent function test: ", most_frequent(str_list))
