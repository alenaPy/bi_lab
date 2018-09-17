"""Print values of digital sequence according to FizzBuzz rule."""


def fizzbuzz(n):
    """Assign values to digital sequence according to FizzBuzz rule."""
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)


print("\n".join(fizzbuzz(n) for n in range(101)))
