def third_power(i):
    return i ** 3


def fizzbuzz(i):
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return i


def character_count(string, character):
    return string.count(character)


def ispalindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    s = s.replace("'", '')
    rev = ''.join(reversed(s))
    if s == rev:
        return True
    return False
