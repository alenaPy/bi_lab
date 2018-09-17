"""Checking if the string is palindrome."""


def is_palindrome(str):
    """Allow to check if the string is palindrome."""
    for char in "_&^%$#@* ,.:;'":
        str = str.replace(char, "")

    if str[0::1].lower() == str[::-1].lower():
        return True
    else:
        return False


"""Fizzbuzz game."""


def fizzBuzz():
    """Fizzbuzz game."""
    res_list = []
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            res_list.append("FizzBuzz")
        elif (i % 5 == 0):
            res_list.append("Buzz")
        elif (i % 3 == 0):
            res_list.append("Fizz")
        else:
            res_list.append(i)
    return res_list


def count_character(count_me_string):
    """Count characters in the string."""
    dict_1 = {}
    for i in count_me_string:
        count_me_string.count(i)
        dict_1.update({i: count_me_string.count(i)})
    return dict_1


def generate_numbers(n):
    """Generate keys and their squares as values."""
    return {i: i ** 2 for i in range(1, n + 1)}
