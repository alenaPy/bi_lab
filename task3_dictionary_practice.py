"""
Task2.

Usages of dictionary comprehensions.
"""


def generate_numbers(n=20):
    """Return a dictionary with square if keys"""
    import math
    dic = {}
    for x in range(n):
        dic[x + 1] = int(math.pow(x + 1, 2))
    return dic


if __name__ == '__main__':
    print(generate_numbers(3))


def count_characters(cnt_str):
    """Return a dictionary with symbols count in a given line"""
    dic = {}
    for x in range(len(cnt_str)):
        cnt = 0
        for y in range(len(cnt_str)):
            if cnt_str[x] == cnt_str[y]:
                cnt += 1
        dic[cnt_str[x]] = cnt
    return dic


if __name__ == '__main__':
    print(count_characters('aabhjdsklagdkjcda'))
