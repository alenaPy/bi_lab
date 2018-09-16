"""Checking if the string is palindrome."""

print("Input string:")
name = input()


def is_palindrome(str):
    """Allow to check if the string is palindrome."""
    for char in "_&^%$#@* ,.:;'":
        str = str.replace(char, "")

    if str[0::1].lower() == str[::-1].lower():
        print("Palindrome")
    else:
        print("Not a palindrome")


is_palindrome(name)
