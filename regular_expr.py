"""Regular Expressions."""
import re

# Write a program to find all email addresses in string.
s1 = 'My email is natallia_haisionak@epam.com '
result = re.findall(r'\w+@\w+\.\w+', s1)
print(result)

# Write a program to find all 3, 4, 5 characters long words in a string.
s2 = 'London is the capital and most populous city of England and the UK!'
result = re.findall(r'\b\w{3,5}\b', s2)
print(result)

# Write a program to separate and print the numbers of a given string.
s3 = 'London\'s average July high is 24 °C (74 °F).'
result = re.findall(r'\d+', s3)
print(result)

# Write a program to replace whitespaces with an underscore and vice versa.
s4 = 'It_was_founded by the Romans, who named it Londinium.'


def replace_char(match_object):
    """Replace whitespaces with an _ and vice versa."""
    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


result = re.sub('\s|_', replace_char, s4)
print(result)
