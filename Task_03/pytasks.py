"""Python previous tasks."""


import re


def is_palindrome(instr='Sator Arepo Tenet Opera Rotas'):
    """Palindrome checker."""
    string = re.sub(r'[^\w]', '', instr).lower()
    if string == string[::-1]:
        return '"{0}" is Palindrome'.format(instr)
    else:
        return '"{0}" is not Palindrome'.format(instr)


def fizz_buzz(n=100):
    """FizzBuzz."""
    return(["Fizz" * (i % 3 == 0) + "Buzz" *
                     (i % 5 == 0) or str(i) for i in range(1, n)])


def generate_numbers(number=20):
    """Generate numbers dictionary as number: number^2."""
    return {n: n ** 2 for n in range(1, number + 1)}


def count_characters(count_me_string='Lorem ipsum dolor sit amet'):
    """Count characters in count_me_string."""
    freq = {}
    for c in count_me_string:
        freq[c] = count_me_string.count(c)
    return freq
