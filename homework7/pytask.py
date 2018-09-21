"""Solution for Dictionary practice."""


def generate_numbers(n):
    """Generate numbers and their squares in specific range."""
    return {i: i ** 2 for i in range(1, n + 1)}


def count_characters(string):
    """Count character occurrences in input string."""
    return {character: string.count(character) for character in string}


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
