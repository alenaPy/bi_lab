"""
Description of script.

It takes data for one item and calculate total cost.
    Example.
    Input: one item price is 3 dollars 20 cents, calculate price for 3 items
    Output data: Total cost:  9 dollars 20 cents.

"""


def fb(n):
    """Return number or specific alias."""
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


print("\n".join(fb(n) for n in range(1, 101)))
