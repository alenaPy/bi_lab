"""Finding palindrome."""
import re

# string initialization
in_string = input("Please input a string: ")

# removing all non-alphanumeric symbols
mod_in_string = re.sub(r'\W+', '', in_string)

# checking whether the string is a palindrome
if mod_in_string.lower() == mod_in_string[::-1].lower():
    print("Input string is a palindrome")
else:
    print("Input string is not a palindrome")
