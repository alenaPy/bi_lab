"""Completed task 4.Module and Functions practice from labwork3."""

import re


def generate_numbers(number=20):
    """Generate numbers.

    Return the dictionary where keys are numbers
    between 1 and number and values are the square of the key.
    """
    return {i: i**2 for i in range(1, number + 1, 1)}


def count_characters(count_me_string):
    """Return the number of each character in string count_me_string."""
    return {i: sum(x == i for x in count_me_string)
            for i in set(list(count_me_string))}


def fizz_buzz():
    """FizzBuzz."""
    return [(not (i + 1) % 3) * "Fizz" + (not (i + 1) % 5) * "Buzz" or i for i
            in range(100)]


def is_palindrome(input_str):
    """is_palindrome check is the input string palindrome or not."""
    check_str = re.sub('[:;,.!@#$0123456789]', '', input_str).lower()
    check_str = check_str.replace(" ", "")
    reversed_str = "".join(reversed(check_str))
    return check_str == reversed_str
