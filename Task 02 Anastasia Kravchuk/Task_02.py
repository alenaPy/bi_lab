"""Task 02."""
import re

# task 2.1

s = input("Please enter your string: \n")


def isPalindrome(p_str):
    """Return true if the string is a palindrome; false otherwise."""
    p_str = re.sub("[!@#$,’,'?:]", "", p_str)
    print(p_str.replace(" ", "").lower() ==
          p_str.replace(" ", "").lower()[:: -1])


isPalindrome(s)

# task 2.2


def totalSum(dollars, cents, count):
    """Evaluate total cost."""
    print("Total cost: {} dollars {} "
          "cents".format((dollars * 100 + cents) * count // 100,
                         (dollars * 100 + cents) * count % 100))


totalSum(7, 60, 3)


# task 2.3


def fizzBuzz():
    """Recreate FizzBuzz game."""
    for i in range(1, 101):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 5 == 0):
            print("Buzz")
        elif (i % 3 == 0):
            print("Fizz")
        else:
            print(i)


fizzBuzz()

# task 2.4

# Elementary task №1 :


def say_hi(name: str, age: int):
    """Print greetings to the chosen person."""
    return "Hi. My name is {} and I'm {} years old".format(name, str(age))


# Elementary task №2 :

def correct_sentence(text: str) -> str:
    """Correct the given sentence."""
    t = text[:1].upper() + text[1:] + '.' if not text.endswith('.') \
        else text.capitalize()
    return t


# Elementary task №3 :


def first_word(text: str):
    """Return the first word in a given text."""
    return re.match(r'\W*(\w[^,. !?"]*)', text).groups()[0]


# Elementary task №4 :

def second_index(text: str, symbol: str) -> [int, None]:
    """Return the second index of a symbol in a given text."""
    return text.index(symbol, text.index(symbol) + 1) \
        if text.count(symbol) >= 2 else None


# Elementary task №5 :

def between_markers(text: str, begin: str, end: str):
    """Return substring between two given markers."""
    if (text.count(end) > 0 and text.count(begin) > 0 and
            text.index(end) < text.index(begin)):
        return ''
    if text.count(begin) == 0:
        start = 0
    else:
        start = text.index(begin) + len(begin)
    if text.count(end) == 0:
        fin = len(text)
    else:
        fin = text.index(end, start)
    return text[start:fin]
