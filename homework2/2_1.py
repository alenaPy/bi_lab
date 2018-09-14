"""Determine if string is a palindrome."""
import re
string = input('Input row: ')
test = re.compile('\w|\d')
treated_string = test.findall(string.lower())
if treated_string == treated_string[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
