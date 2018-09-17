s = input('Enter string\n')

l = len(s)

for char in s:
    if char in " ?.!/;:":
        s = (s.replace(char, '').lower())
else:
    s = (s.lower())

for i in range(l // 2):
    if s[i] != s[-1 - i]:
        print("It's not palindrome %s" % s)
        quit()

print("It's palindrome %s" % s)
