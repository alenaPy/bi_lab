"""Run the functions program."""
import pytasks
func_dict = {'generate_numbers': pytasks.generate_numbers,
             'count_characters': pytasks.count_characters,
             'fizzbuzz': pytasks.fizzbuzz,
             'is_palindrome': pytasks.is_palindrome}


def runner(*f):
    """Run the functions."""
    if len(f) == 0:
        print(pytasks.generate_numbers(20))
        print(pytasks.count_characters('abcdefgabc'))
        print(pytasks.fizzbuzz())
        print(pytasks.is_palindrome('Was it a car or a cat I saw?'))
    else:
        for func in f:
            if func not in func_dict:
                print('Unknown function: ' + func)
                continue
            else:
                print(func_dict[func](20))

# runner()
# runner('fun1')
# runner('generate_numbers')
