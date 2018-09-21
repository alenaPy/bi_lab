"""Function."""


def number_square(i):
    """Generate numbers and their squares in specific range."""
    return i ** 2


def count_characters(string, character):
    """Count character occurrences in input string."""
    return string.count(character)


def fizzbuzz(i):
    """Fizzbuzz function."""
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i


def is_palindrome(p):
    """Check if it is palindrome."""
    import re
    p = p.replace(" ", "")
    s = re.sub("[!@#$%^&*?_()-+,./\|'~]", '', p).lower()
    if s == s[::-1]:
        return True
    else:
        return False
