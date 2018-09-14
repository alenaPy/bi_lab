import re

def reverse(s):
    return s[::-1]

def is_palindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    return False

s = input("Enter a string:\n")
s = s.lower()
s = re.sub("[!?@#$,_]", "", s)
s = s.replace(" ", "")
res = is_palindrome(s)

if (res):
    print("Yes, this is a palindrome.")
else:
    print("No, this is not a palindrome.")
