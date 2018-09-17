"""Runner function."""


import pytasks


def runner(*name_func):
    """Call specified function(s)."""
    if len(name_func) == 0:
        print(pytasks.count_character('abcadc'))
        print(pytasks.is_palindrome('abba'))
        print(pytasks.fizzBuzz())
        print(pytasks.generate_numbers(20))
    for func in name_func:
        if func == 'count_character':
            print(pytasks.count_character('aabbccf'))
        elif func == 'is_palindrome':
            print(pytasks.is_palindrome('aabbccf'))
        elif func == 'fizzBuzz':
            print(pytasks.fizzBuzz())
        elif func == 'generate_numbers':
            print(pytasks.generate_numbers(20))
        else:
            print('%s is an invalid name of function.' % func)


runner('generate_numbers', 'fizzBuzz')
