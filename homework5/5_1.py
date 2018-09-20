"""RegularExpressions."""


import re

text = input("Enter text: " + '\n')
expression = re.compile(r"(\S+@\S+)")
email = expression.findall(text)
print(email)
print(re.findall(r"\b\w{3,5}\b", text))
print(re.sub(r'[^0-9 ]', '', text))


def replace_char(match_object):
    """ReplaceChar."""
    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


print(re.sub('\s|_', replace_char, text))
