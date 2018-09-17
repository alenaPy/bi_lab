"""Dictionary practice."""

'''1.Define a function generate_numbers(number) which returns a dictionary
where the keys are numbers between 1 and n (both included)
and the values are square of keys. n – function argument. Default is 20.'''


def generate_numbers(n=20):
    """Return a dictionary, keys ∈ [1, arg], values are square of keys."""
    return {i: i**2 for i in range(1, int(n) + 1)}


arg1 = input('1. Input a number: ')
print(generate_numbers(arg1))

'''2.Define a function count_characters(count_me_string) which count
and return the numbers of each character in a count_me_string argument.'''


def count_characters(arg):
    """Count and return the numbers of each character in arg."""
    return dict(zip(arg, list(map(lambda x: arg.count(x), arg))))


arg2 = list(input('2. Input a string: '))
print(count_characters(arg2))
