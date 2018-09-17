"""Module that contains definition for functions from previous tasks."""


def generate_numbers(n=20):
    """Return a dictionary, keys ∈ [1, arg], values are square of keys."""
    return {i: i**2 for i in range(1, int(n) + 1)}


def count_characters(arg=''):
    """Count and return the numbers of each character in arg."""
    return dict(zip(arg, list(map(lambda x: arg.count(x), arg))))


def fizzbuzz():
    """Implement FizzBuzz."""
    res = []
    for i in range(1, 101):
        res.append('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    return res


def is_palindrome(arg=''):
    """Find palindrome."""
    import re

    # removing all non-alphanumeric symbols
    mod_in_string = re.sub(r'\W+', '', arg)

    # checking whether the string is a palindrome
    if mod_in_string.lower() == mod_in_string[::-1].lower():
        return True
    else:
        return False
