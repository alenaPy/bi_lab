"""Module and Functions practice."""


def generate_numbers(number=20):
    """GenerateNumbers."""
    dict1 = {}
    for key in range(1, number + 1):
        dict1[key] = key * key
    return dict1


def count_characters(count_me_string):
    """CountCharacters."""
    dict2 = {}
    for i in count_me_string:
        dict2[i] = count_me_string.count(i)
    return dict2


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


def fizzbuzz(n=100):
    """Assign values to digital sequence according to FizzBuzz rule."""
    list1 = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            list1.append('FizzBuzz')
        elif i % 3 == 0:
            list1.append('Fizz')
        elif i % 5 == 0:
            list1.append('Buzz')
        else:
            list1.append(i)
            return list1
