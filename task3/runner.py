"""Functions runner module."""
import pytasks


def runner(*funcs):
    """Run functions implemented in pytasks module."""
    for func in funcs:
        print(func())


# example
runner(pytasks.generate_numbers, pytasks.fizzbuzz)
