"""Solution for Dictionary practice."""


def third_power(i):
    """Generate numbers and their squares in specific range."""
    return i ** 3


def character_count(string, character):
    """Count character occurrences in input string."""
    return string.count(character)


def ispalindrome(s):
    """Reversed."""
    s = s.lower()
    s = s.replace(' ', '')
    s = s.replace("'", '')

    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False


def fizzbuzz(i):
    """Fizzbuzz."""
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i
