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


def fizzbuzz(i):
    """Fizzbuzz game."""
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i


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
