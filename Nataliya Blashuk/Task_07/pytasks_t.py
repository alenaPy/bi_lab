"""File with functions for unittests."""

import re


def count_characters(count_me_string="abcdefgabc", chr="a"):
    """Return the number of character in string count_me_string."""
    return count_me_string.count(chr)


def fizz_buzz(i):
    """FizzBuzz."""
    if i % 3 == 0 and i % 5 == 0:
        return ("FizzBuzz")
    elif i % 3 == 0:
        return ("Fizz")
    elif i % 5 == 0:
        return ("Buzz")
    else:
        return i


def is_palindrome(input_str="Red rum, sir, is murder"):
    """is_palindrome check is the input string palindrome or not."""
    check_str = re.sub('[:;,.!@#$0123456789]', '', input_str).lower()
    check_str = check_str.replace(" ", "")
    reversed_str = "".join(reversed(check_str))
    return check_str == reversed_str


def square_number(i):
    """Return the square of the input number."""
    return i ** 2
