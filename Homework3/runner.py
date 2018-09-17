"""Function for running selected functions."""


def runner(*functions):
    """Run selected functions."""
    import pytasks
    if len(functions) == 0:
        print(pytasks.generate_numbers())
        print(pytasks.count_characters())
        print(pytasks.fizzbuzz())
        print(pytasks.is_palindrome())
    for func in functions:
        if func == 'generate_numbers':
            param = input('Input parameter value for generate_numbers():')
            print(pytasks.generate_numbers(int(param)))
        elif func == 'count_characters':
            param = input('Input parameter value for count_characters():')
            print(pytasks.count_characters(param))
        elif func == 'fizzbuzz':
            param = input('Input parameter value for fizzbuzz():')
            print(pytasks.fizzbuzz(int(param)))
        elif func == 'is_palindrome':
            param = input('Input parameter value for is_palindrome():')
            print(pytasks.is_palindrome(param))
        else:
            print('%s is an invalid name of function.' % func)
