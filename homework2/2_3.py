"""Print values of digital sequence according to FizzBuzz rule."""


def fizzbuzz(i):
    """Assign values to digital sequence according to FizzBuzz rule."""
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz'
    elif i % 3 == 0:
        return 'Fizz'
    elif i % 5 == 0:
        return 'Buzz'
    else:
        return str(i)


print("\n".join(fizzbuzz(i) for i in range(101)))
