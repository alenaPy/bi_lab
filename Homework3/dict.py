"""Solution for Dictionary practice."""


def generate_numbers(n=20):
    """Generate numbers and their squares in specific range."""
    return {i: i ** 2 for i in range(1, n + 1)}


def count_characters(count_me_string):
    """Print characters and their number of occurrences in parameter string."""
    return {character: count_me_string.count(character)
            for character in count_me_string}


print(generate_numbers())
print(count_characters('abcdefgabc'))
