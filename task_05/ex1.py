"""Regular Expressions."""

import re


def extr_email():
    """Find all email addresses in string. Space is a separator."""
    strng = input("Input a string, preferably containing am email: ")
    pattern = re.compile(r'^[A-Za-z][\w!#$%&\'*+\-/=?^_`{|}~]+'
                         r'@[A-Za-z]+\.[A-Za-z]+$')
    res = []
    for obj in strng.split():
        if re.search(pattern, obj):
            res.append(obj)
    print(res)


def extr_345():
    """Find all three, four, five characters long words in a string."""
    strng = input("Input a string: ")
    pattern = re.compile(r'\b.{3,5}\b')
    res = []
    for obj in strng.split():
        if re.search(pattern, obj):
            res.append(obj)
    print(res)


def extr_nums():
    """Separate and print the numbers of a given string."""
    strng = input("Input a string: ")
    pattern = re.compile(r'\d+')
    print(re.findall(pattern, strng))


def rpl():
    """Replace whitespaces with an underscore and vice versa."""
    def rpl_choise(sbstr):
        """Choose dynamically a replace character."""
        if sbstr[0] == ' ':
            return '_'
        else:
            return ' '

    strng = input("Input a string: ")
    print(re.sub(r'\s|_', rpl_choise, strng))


# extr_email()
# extr_345()
# extr_nums()
# rpl()
