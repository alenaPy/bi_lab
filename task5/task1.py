"""Task5."""

import re


def check_email(line):
    """Find all emails."""
    print(re.findall("\w+@\w+\.[a-zA-Z]{2,3}", line))


def check_words(line):
    """Check word length."""
    print(re.findall(r"\b\w{3,5}\b", line))


def check_numbers(line):
    """Find all numbers."""
    print(re.sub(r'[^0-9]', '', line))


def check_underscores(line):
    """Replace underscore."""
    if line[0] == ' ':
        return '_'
    else:
        return ' '


check_email("Yauheni Bandarchyk genya_3@mail.ru yauheni_bandarchyk@epam.com ")
check_words("hello world yauheni bandarchyk")
check_numbers("789asdg456123")
print(re.sub('\s|_', check_underscores, "nsdfkj_sbj sdfa"))
