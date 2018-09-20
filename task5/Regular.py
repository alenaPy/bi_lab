"""Regular Expressions."""
import re
# find all email addresses in string.
string_1 = 'I have two emails one of this is arina.kondrashevich@mail.ru and the other one is beliashik97@mail.ru '
emails = re.findall(r'\w+@\w+\.\w+', string_1)
print(emails)


# find all 3, 4, 5 characters long words in a string.
string_2 = 'Hello! My name is Aryna. I''m student of Belarusian state university of informatics and radio electronics '
words = re.findall(r'\w+', string_2)
for i in words:
    if len(i) in (3, 4, 5):
        print(i)


# separate and print the numbers of a given string.
string_3 = 'I''m 20 years old. I was born in 1997'
result = re.findall(r'\d+', string_3)
print(result)


# replace whitespaces with an underscore and vice versa.
string_4 = 'Hello_my_dear friend. I miss you.'


def replace_char(match_object):

    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


result = re.sub('\s|_', replace_char, string_4)
print(result)
