"""Palindrome."""


import re


def main():
    """Main."""
    is_palindrome(input('Type your string: \n'))


def is_palindrome(instr):
    """Palindrome checker."""
    string = re.sub(r'[^\w]', '', instr).lower()
    if string == string[::-1]:
        print('"{0}" is Palindrome'.format(instr))
    else:
        print('"{0}" is not Palindrome'.format(instr))


main()
