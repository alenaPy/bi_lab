"""Index Power."""

# https://py.checkio.org/en/mission/index-power/


def index_power(list_arg, n):
    """You are given an array with positive numbers and a number N.

    You should find the Nth power of the element in the array with the index N.
    If N is outside of the array, then return -1.
    """
    if type(list_arg) is not list:
        raise Exception("Invalid argument type")

    if n > len(list_arg) - 1:
        return -1
    else:
        return int(list_arg[n])**n


input_val = input('Please input comma separated numbers: ')
num_list = input_val.split(",")
n = int(input('Please input a number less than list\'s length: '))
print(index_power(num_list, n))
