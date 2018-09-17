"""Pytasks Module."""

import re


def generate_numbers(number=20):
    """Generate numbers for dictionary: {i, i^2} in given range (1,n)."""
    return {i: i ** 2 for i in range(1, number+1)}


def cogenerate_numbers(count_me_string='abcdefgabc'):
    """Generate dictionary {character : number of character instances}."""
    return {i: sum(x is i for x in count_me_string) for i in
            sorted(set(list(count_me_string)))}


def fizz_buzz():
    """Recreate FizzBuzz game."""
    return [(not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n for n
            in range(1, 101)]


def isPalindrome(p_str='О, лета тело!'):
    """Return true if the string is a palindrome; false otherwise."""
    p_str = re.sub("[!@#$,’,'?:]", "", p_str).lower()
    return p_str.replace(" ", "") == p_str.replace(" ", "")[:: -1]
