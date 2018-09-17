"""Defining the functions."""
import collections
import re


def generate_numbers(n):
    """Numbers generation."""
    d = dict()
    for x in range(1, n):
        d[x] = x ** 2
    return [d]


def count_characters(str):
    """Characters calculation."""
    d = collections.defaultdict(int)
    for letter in str:
        d[letter] += 1
    return[sorted(d.items())]


def fizzbuzz():
    """Fizz&Buzz check."""
    list1 = []
    for num in range(1, 101):

        if num % 3 == 0 and num % 5 == 0:
            list1.append("FizzBuzz")

        elif num % 3 == 0:
            list1.append("Fizz")

        elif num % 5 == 0:
            list1.append("Buzz")

        else:
            list1.append(num)
    return list1


def reverse(s):
    """Reversing the string."""
    s = s.lower()
    s = re.sub("[!?@#$,_]", "", s)
    s = s.replace(" ", "")
    return s[::-1]


def is_palindrome(s):
    """Palindrome check."""
    rev = reverse(s)

    if s == rev:
        return True
    return False
