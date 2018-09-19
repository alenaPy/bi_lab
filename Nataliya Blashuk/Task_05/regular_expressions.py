"""File contains completed task 1. Regular Expressions."""
import re

# 1
print("Task1")


def find_emails(str="Hi, here is my email: nataliya_blashuk@epam.com."):
    """Print list with all email addresses that contains in str."""
    for i in re.findall(r"\w+@\w+\.\w+", str):
        print(i)


find_emails()

# 2
print("\nTask2")


def find_words(str="The string contains some words with length "
                   "three, four and five. Let`s see them!"):
    """Print words with length 3,4,5."""
    for i in re.findall(r"\w+", str):
        if len(i) in (3, 4, 5):
            print(i)


find_words()

# 3
print("\nTask3")


def find_numbers(str="1 is one, 2 is two, 3 is three and so on"):
    """Print numbers that is in the string."""
    for i in re.findall(r"\d+", str):
        print(i)


find_numbers()

# 4
print("\nTask4")


def replace_characters(mobj):
    """Replace characters."""
    if mobj[0] == " ":
        return "_"
    else:
        return " "


def replaced_string(str="The string with _underscopes_"):
    """Replace characters in the input string."""
    print(re.sub("\s|_", replace_characters, str))
