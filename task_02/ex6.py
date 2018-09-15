"""Digits Multiplication.

You are given a positive integer.
Your function should calculate the product of the digits excluding any zeroes.
"""

# https://py.checkio.org/en/mission/digits-multiplication/


def checkio(num):
    """Calculate the product of the digits excluding any zeroes."""
    pre_num = str(num).replace('0', '')
    res = 1
    for i in pre_num:
        res *= int(i)

    return res


num = input('Please input an integer number: ')
print("checkio function test: ", checkio(num))
