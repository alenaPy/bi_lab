"""Pytask."""


def generate_numbers():
    """Generate numbers."""
    print()

    print(generate_numbers)

    print()

    numbers = 20

    dict_1 = {}

    for i in range(1, numbers + 1):

        dict_1[i] = i * i

    print(dict_1)

    return dict_1


def count_characters():
    """Count characters."""
    print()

    print(count_characters)

    print()

    count_me_string = "Natallia"

    dict_1 = {}

    for i in count_me_string:

        dict_1[i] = count_me_string.count(i)

    print(dict_1)

    return dict_1


def fizzbuzzz():
    """Fizzbuzzz."""
    print()

    print(fizzbuzzz)

    print()

    for fizzbuzz in range(101):

        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:

            print("fizzbuzz")

        elif fizzbuzz % 3 == 0:

            print("fizz")

        elif fizzbuzz % 5 == 0:

            print("buzz")

        else:

            print(fizzbuzz)


def is_palindrome():
    """Palindrome."""
    print()

    print(is_palindrome)

    print()

    my_str = "addDa"

    my_str = my_str.casefold()

    rev_str = my_str[::-1]

    print(my_str == rev_str)

    if my_str == rev_str:

        return True

    else:

        return False
