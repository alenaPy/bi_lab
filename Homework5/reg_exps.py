"""Solution for Regular Expressions."""
import re


def email_search():
    """Find emails in the string."""
    email_pattern = re.compile("""
    ^[a-zA-Z][\w!#\$%\&\'\*\+-/=\?\^_`\{\|\}~]{2,}@\w{2,}\.[a-zA-Z\.]{2,}$
    """, re.X)
    matches = []
    string = input('Enter a string for email search:')
    for substring in string.split():
        if len(email_pattern.findall(substring)) != 0:
            matches.append(email_pattern.findall(substring))
    if len(matches) == 0:
        print('There is no email in the string.')
    else:
        print('Emails in the string are:', matches)


def length_check():
    """Find words of 3-5 characters length in the string."""
    word_pattern = re.compile('^[a-z]{3,5}$', re.I)
    matches = []
    string = input('Enter a string for exact length word search:')
    for substring in string.split():
        if len(word_pattern.findall(substring)) != 0:
            matches.append(word_pattern.findall(substring))
    if len(matches) == 0:
        print('There is no such a word in the string.')
    else:
        print('Such words in the string are:', matches)


def string_numbers():
    """Extract numbers fron the string."""
    number_pattern = re.compile('\d')
    matches = []
    string = input('Enter a string for numbers search:')
    for substring in string.split():
        if len(number_pattern.findall(substring)) != 0:
            matches.append(number_pattern.findall(substring))
    if len(matches) == 0:
        print('There is no number in the string.')
    else:
        print('Numbers in the string are:', matches)


def replace_characters(match_object):
    """Replace characters."""
    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


def string_with_replacements():
    """Replace characters in the input string."""
    string = input('Enter a string for replacing:')
    print('Result is:', re.sub('\s|_', replace_characters, string))


# email_search()
# length_check()
# string_numbers()
# string_with_replacements()
