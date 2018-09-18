"""
Task2.

runner.
"""

import pytasks


def runner(args):
    """Runner."""
    if args != 0:
        for i in args:
            getattr(pytasks, i)()
    else:
        getattr(pytasks, 'generate_numbers')()
        getattr(pytasks, 'count_characters')()
        getattr(pytasks, 'fizzbuzz')()
        getattr(pytasks, 'ispalindrome')()
    return
