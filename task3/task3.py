
import Task_4

# List practice
# 1.1

List = [('{0}{1}'.format(x,y)) for x in ['a', 'b'] for y in ['b', 'c', 'd']]
print(List)

# 1.2

List_2 = (List[::2])
print(List_2)

# 1.3

List_3 = [('{0}a'.format(x)) for x in range(1,5)]
print(List_3)

# 1.4

print("Removed element '2a' : ", List_3.pop(List_3.index('2a')))
print(List_3)

# 1.5

List_4 = List_3[:]
List_4.insert(1, '2a')
print(List_4)

# Tuple practice
# 2.1

List_1 = ['a', 'b', 'c']
Tuple_1 = tuple(List_1)
print(Tuple_1)

# 2.2

Tuple_2 = ('a', 'b', 'c')
List_2 = list(Tuple_2)
print(List_2)

# 2.3

a, b, с = 'a', 2, 'gamma'

# 2.4

Tuple_4 = (Tuple_2,)
len(Tuple_4)
print(Tuple_4)


# Dictionary practice
# 1.1

def generate_numbers(number=20):
    """Generate dictionary: {number, number^2}."""
    return {i: i ** 2 for i in range(1, number + 1)}


generate_numbers()
generate_numbers(18)

# 1.2


def generate_numbers(number=20):
    """Generate dictionary: {number, number^2}."""
    return {i: i ** 2 for i in range(1, number + 1)}


generate_numbers()
generate_numbers(18)


dictionary = {'cogenerate_numbers': Task_4.cogenerate_numbers,
              'generate_numbers': Task_4.generate_numbers,
              'fizz_buzz': Task_4.fizz_buzz,
              'isPalindrome': Task_4.isPalindrome}


def runner(*func):
    """Dispatcher for all functions or their combinations in Task_4 module."""
    if len(func) == 0:
        for function in dictionary:
            print(dictionary[function]())

    for function in func:
        if function not in dictionary:
            print('There is/are no such function/s in Task_4 module')
            continue
        else:

            print(dictionary[function]())


runner()
runner('fizz_buzz')
runner('cogenerate_numbers', 'generate_numbers')
runner('cogenerate_numbers', 'generate_numbers', 'fizz_buzz', 'isPalindrome')
runner('isPalindrome')
runner('34', 'cogenerate_numbers')

