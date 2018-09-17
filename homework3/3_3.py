"""DictionaryTask."""


def generate_numbers(number=20):
    """Create dictionary."""
    dict_first = {}
    for x in range(1, number + 1):
        dict_first[x] = x * x
    return dict_first


print(generate_numbers())
print()

count_me_string = input('Enter text: ')


def count_characters(count_me_string):
    """Create dictionary."""
    dict_sec = {}
    for x in count_me_string:
        dict_sec[x] = count_me_string.count(x)
    return dict_sec


print(count_characters(count_me_string))
