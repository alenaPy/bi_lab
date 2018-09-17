"""Solution for Dictionary practice."""


def generate_numbers(n=20):
    """Generate numbers and their squares in specific range."""
    return {i: i ** 2 for i in range(1, n + 1)}


def count_characters(count_me_string='abcdefgabc'):
    """Print characters and their number of occurrences in parameter string."""
    return {character: count_me_string.count(character)
            for character in count_me_string}


def fizzbuzz(n=100):
    """Assign values to digital sequence according to FizzBuzz rule."""
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append('FizzBuzz')
        elif i % 3 == 0:
            output.append('Fizz')
        elif i % 5 == 0:
            output.append('Buzz')
        else:
            output.append(i)
    return output


def is_palindrome(string=''):
    """Determine if input string is a palindrome."""
    import re
    regex = re.compile('\w|\d')
    treated_string = regex.findall(string.lower())
    if treated_string == treated_string[::-1]:
        return True
    else:
        return False
