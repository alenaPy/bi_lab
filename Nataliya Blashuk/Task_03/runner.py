"""Completed task 4.Module and Functions practice from labwork3.

(Runner module).
"""

import pytasks

d = {"generate_numbers": pytasks.generate_numbers,
     "count_characters": pytasks.count_characters,
     "fizz_buzz": pytasks.fizz_buzz,
     "is_palindrome": pytasks.is_palindrome}


def runner(*f):
    """Show the result of functions in pytasks.py."""
    if len(f) == 0:
        for fnct in d:
            print(d[fnct]())
    for fnct in f:
        if fnct not in d:
            print("The function wasn`t found in the pytasks.py")
            continue
        else:
            print(d[fnct]())


runner()
runner("generate_numbers")
runner("generate_numbers", "is_palindrome")
