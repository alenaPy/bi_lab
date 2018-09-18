"""Function for running selected functions."""


import pytasks

dictionary = {'count_characters': pytasks.count_characters,

              'generate_numbers': pytasks.generate_numbers,

              'fizz_buzz': pytasks.fizz_buzz,

              'isPalindrome': pytasks.isPalindrome}


def runner(*func):
    """Dispatcher for all functions or their combinations in pytasks module."""

    if len(func) == 0:

        for function in dictionary:
            print(dictionary[function]())

    for function in func:

        if function not in dictionary:

            print('There is/are no such function/s in pytasks module')

            continue


        else:

            print(dictionary[function]())


runner()

runner('fizz_buzz')

runner('count_characters', 'generate_numbers')

runner('count_characters', 'generate_numbers', 'fizz_buzz', 'isPalindrome')

runner('isPalindrome')

runner('7877', 'count_characters')