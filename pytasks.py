"""
Task2.

pytasks.
"""


def generate_numbers(n=20):
    """Return a dictionary with square if keys"""
    import math
    dic = {}
    for x in range(n):
        dic[x+1] = int(math.pow(x + 1, 2))
    return dic


def count_characters(cnt_str='aaabndlsbfjks'):
    """Return a dictionary with symbols count in a given line"""
    dic = {}
    for x in range(len(cnt_str)):
        cnt = 0
        for y in range(len(cnt_str)):
            if cnt_str[x] == cnt_str[y]:
                cnt += 1
        dic[cnt_str[x]] = cnt
    return dic


def fb(n=20):
    """Return number or specific alias."""
    list1 = []
    for x in range(1, n):
        if x % 3 == 0 and x % 5 == 0:
            list1.insert(x, 'FizzBuzz')
        elif x % 3 == 0:
            list1.insert(x, 'Fizz')
        elif x % 5 == 0:
            list1.insert(x, 'Buzz')
        else:
            list1.insert(x, x)
    return list1


def is_palindrome(line='mmm'):
    import re
    line = re.sub('[ ,&?!\'.;:*/_0132456789\-]', '',line)
    if line != "" and line == ''.join(reversed(line)):
        return True
    else:
        return False
