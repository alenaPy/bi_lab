"""Labwork2."""

# Task1. Checks palyndrom.
s = input('Enter string\n')

leng = len(s)

for char in s:
    if char in " ?.!/;:":
        s = (s.replace(char, '').lower())
    else:
        s = s.lower()

for i in range(leng//2):
    if s[i] != s[-leng - i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")
