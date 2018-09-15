"""Index Power.

You are given an array with positive numbers and a number N.
You should find the Nth power of the element in the array with the index N.
If N is outside of the array, then return -1.
"""

# https://py.checkio.org/en/mission/index-power/


def index_power(arg, n):
    """Return the Nth power of the Nth element or -1 If N>len(arg)."""
    if n > len(arg) - 1:
        return -1
    else:
        return int(arg[n])**n


input_val = input('Please input comma separated numbers: ')
num_list = input_val.split(",")
n = int(input('Please input a number less than list\'s length: '))
print("index_power function test: ", index_power(num_list, n))
