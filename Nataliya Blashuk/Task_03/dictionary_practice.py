"""Completed task 3.Dictionary practice from labwork3."""


# 3.1
def generate_numbers(number=20):
    """Generate numbers.

    Return the dictionary where keys are numbers
    between 1 and number and values are the square of the key.
    """
    return {i: i**2 for i in range(1, number + 1, 1)}


var = generate_numbers()
print(var)


# 3.2
def count_characters(count_me_string):
    """Return the number of each character in string count_me_string."""
    return {i: sum(x is i for x in count_me_string)
            for i in set(list(count_me_string))}


strng = count_characters("abcdefgabc")
print(strng)
