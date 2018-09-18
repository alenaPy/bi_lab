"""Module and Functions practice."""
import re


def is_polindrome():
    """Check if it is polindrome."""
    p = input("Enter a palindrome: ")
    p = p.replace(" ", "")
    s = re.sub("[!@#$%^&*?_()-+,./\|'~]", '', p).lower()
    print("It is palindrome" if s == s[::-1] else "NO")


def fizzbuzz():
    """Fizzbuzz function."""
    n = int(input("Enter max number: "))
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def generate_numbers(n=20):
    """Return dictionary key n, value - square of key."""
    print({x: x ** 2 for x in range(1, n + 1, 1)})


def count_characters():
    """Count and return numbers of each character."""
    count_me_string = input("Enter string: ")
    print({x: count_me_string.count(x) for x in count_me_string})
