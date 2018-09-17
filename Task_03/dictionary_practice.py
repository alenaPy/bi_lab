"""Dictionary practice."""


def generate_numbers(number=20):
    """Generate numbers dictionary as number: number^2."""
    return {n: n ** 2 for n in range(1, number + 1)}


def count_characters(count_me_string):
    """Count characters in count_me_string."""
    freq = {}
    for c in count_me_string:
        freq[c] = count_me_string.count(c)
    return freq


# Check
print(generate_numbers(5))
print(count_characters('abcdefgabc'))
