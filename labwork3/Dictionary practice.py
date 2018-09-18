"""Task 3."""

# Task 3.1


def generate_numbers(n=20):
    """Func generates number for dictionary."""

    dict1 = {i: i ** 2 for i in range(1, n + 1)}
    return dict1


print(generate_numbers(20))

# Task 3.2


def count_characters(count_me_string):
    """Count and return the numbers of each character in the str argument."""
    dict2 = {i: sum(x is i for x in count_me_string) for i in
             set(list(count_me_string))}
    return dict2


print(count_characters('abcdefgabc'))
