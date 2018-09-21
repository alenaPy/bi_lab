"""Pytasks Module."""


def generate_numbers(n=20):
    """Func generates number for dictionary."""
    return n ** 2


def count_characters(count_me_string, i):
    """Count and return the numbers of each character in the str argument."""
    return sum(x is i for x in count_me_string)


def fizz_buzz(n):
    """Recreate FizzBuzz game."""
    if n % 3 == 0 and n % 5 != 0:
        return('Fizz')
    elif n % 5 == 0 and n % 3 != 0:
        return('Buzz')
    elif n % 5 == 0 and n % 3 == 0:
        return('FizzBuzz')
    else:
        return(n)


def isPalindrome(s):
    """Return true if the string is a palindrome; false otherwise."""
    """Determine if input string is a palindrome."""
    import re
    regex = re.compile('\w|\d')
    treated_string = regex.findall(s.lower())
    if treated_string == treated_string[::-1]:
        return True
    else:
        return False
