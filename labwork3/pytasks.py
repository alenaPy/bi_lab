"""Pytasks Module."""


import re


def generate_numbers(n=20):
    """Func generates number for dictionary."""

    dict1 = {i: i ** 2 for i in range(1, n + 1)}
    return dict1


def count_characters(count_me_string='sldvsvpnsodvi'):
    """Count and return the numbers of each character in the str argument."""
    dict2 = {i: sum(x is i for x in count_me_string) for i in
             set(list(count_me_string))}
    return dict2


def fizz_buzz():
    """Recreate FizzBuzz game."""

    for n in range(1, 101):
        if n % 3 == 0 and n % 5 != 0:
            print('Fizz,')
        elif n % 5 == 0 and n % 3 != 0:
            print('Bizz,')
        elif n % 5 == 0 and n % 3 == 0:
            print('FizzBizz,')
        else:
            print(n, ",")

    return


def isPalindrome(p_str='О, лета тело!'):
    """Return true if the string is a palindrome; false otherwise."""

    s = input('Enter string\n')

    leng = len(s)

    for char in s:
        if char in " ?.!/;:":
            s = (s.replace(char, '').lower())
        else:
            s = s.lower()

    for i in range(leng // 2):
        if s[i] != s[-leng - i]:
            print("It's not palindrome")
            quit()

    print("It's palindrome")

    return