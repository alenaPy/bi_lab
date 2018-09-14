"""Finding palindrome."""
import re

palStr = input("Enter the string to check is it palindrome or not: \n")


def is_palindrome(input_str):
    """is_palindrome check is the input string palindrome or not."""
    check_str = re.sub('[:;,.!@#$0123456789]', '', input_str).lower()
    check_str = check_str.replace(" ", "")
    reversed_str = "".join(reversed(check_str))
    if check_str == reversed_str:
        print("This string %s is palindrome" % input_str)
    else:
        print("The string %s is not palindrome" % input_str)


is_palindrome(palStr)
