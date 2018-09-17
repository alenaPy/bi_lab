"""Runner function."""
import pytasks
func_dict = {'is_polindrome': pytasks.is_polindrome,
             'fizzbuzz': pytasks.fizzbuzz,
             'generate_numbers': pytasks.generate_numbers,
             'count_characters': pytasks.count_characters}


def runner(*f):
    """Runner function."""
    if len(f) == 0:
        pytasks.is_polindrome()
        pytasks.fizzbuzz()
        pytasks.generate_numbers()
        pytasks.count_characters()
    else:
        for func in f:
            if func not in func_dict:
                print('Unknown function: ' + func)
                continue
            else:
                func_dict[func]()


# runner()
# runner('123')
# runner('123', 'fizzbuzz')
# runner('is_polindrome', 'count_characters')
