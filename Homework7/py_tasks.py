"""Solution for Dictionary practice."""


def number_square(i):
    """Generate numbers and their squares in specific range."""
    return i ** 2


def count_characters(string, character):
    """Count character occurrences in input string."""
    return string.count(character)


def fizzbuzz(i):
    """Assign value to input number according to FizzBuzz rule."""
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i


def is_palindrome(string):
    """Determine if input string is a palindrome."""
    import re
    regex = re.compile('\w|\d')
    treated_string = regex.findall(string.lower())
    if treated_string == treated_string[::-1]:
        return True
    else:
        return False
