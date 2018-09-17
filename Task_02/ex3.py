"""Fizz Buzz."""


def main():
    """Main."""
    fizz_buzz()


def fizz_buzz():
    """FizzBuzz."""
    print("\n".join(["Fizz" * (i % 3 == 0) + "Buzz" *
                     (i % 5 == 0) or str(i) for i in range(1, 100)]))


main()
