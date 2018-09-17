"""Palindrome."""


def ispalindrome(s):
    """Reversed."""
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False


s = "Dammit I'm Mad".lower()
s = s.replace(' ', '')
s = s.replace("'", '')
t = ispalindrome(s)

if t:
    print("Yes")
else:
    print("No")


# Money calculation


def istotalsum(dollars, cents, count):
    """Price."""
    a = (dollars * 100 + cents) * count % 100
    b = dollars * 100 + cents
    print("Total cost: {} dollars {} cents".format(b * count // 100, a))


istotalsum(7, 60, 3)

# FizzBuzz
for i in range(1, 100):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))
