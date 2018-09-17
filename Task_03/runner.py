"""Runner."""


import pytasks as pt


dictionary = {
    'is_palindrome': pt.is_palindrome(),
    'fizz_buzz': pt.fizz_buzz(),
    'generate_numbers': pt.generate_numbers(),
    'count_characters': pt.count_characters()
}


def runner(*instr):
    """Task runner."""
    if len(instr) == 0:
        for func in dictionary:
            print(dictionary[func])
    for func in instr:
        if func not in dictionary:
            print('There is no function with name "{0}"'.format(func))
        else:
            print(dictionary[func])


runner('is_palindrome', 'fizz_buzz', 'tt')
