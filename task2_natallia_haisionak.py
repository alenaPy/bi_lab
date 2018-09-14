"""labwork2 Natallia Haisionak."""
import re

# 1
p = input("Enter a palindrome: ")
p = p.replace(" ", "")
s = re.sub("[!@#$%^&*?_()-+,./\|'~]", '', p).lower()
print("It is palindrome" if s == s[::-1] else "NO")

# 2


def price(m, n, l):
    """Purchase money calculation."""
    pr = (m*100+n)*l
    print('Total cost: {0} dollars {1} cents.'.format(pr//100, pr % 100))


price(5, 20, 3)

# 3
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 4(1-5)


def say_hi(name, age):
    """Name and age."""
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)


print(say_hi('Natasha', 30))


def correct_sentence(text: str) ->str:
    """Correct sentence."""
    text = text[:1].upper()+text[1:]
    if text[len(text)-1] == '.':
        text = text
    else:
        text = text + '.'
    return text


print(correct_sentence("greeting, friends."))


def first_word(text):
    """First word."""
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


print(first_word("Hello, world"))


def second_index(text: str, symbol: str) -> [int, None]:
    """Second index."""
    return text.index(symbol,
                      text.index(symbol) + 1) if text.count(symbol) >= 2 \
        else None


print(second_index("sims", "s"))
