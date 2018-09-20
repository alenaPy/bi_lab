"""Exceptions."""


# 1
def division_zero():
    """ZeroDivisionError."""
    a, b = 5, 0
    try:
        a / b
    except ZeroDivisionError:
        print('Division by zero is forbidden.')


division_zero()


# 2
def print_list_element(the_list, index):
    """IndexError."""
    try:
        print(the_list[index])
    except IndexError:
        a = str(len(the_list))
        print('Index is ' + str(index) + ' out of range. List length = ' + a)


print_list_element([1, 2], 25)


# 3
def add_to_list_in_dict(dict1, list1, element):
    """KeyError."""
    try:
        current_list = dict1[list1]
    except KeyError:
        print("Dictionary has no list %s" % list1)
        dict1[list1] = []
        current_list = dict1[list1]
    else:
        c = str(current_list)
        print("List has ", c)
    finally:
        current_list.append(element)
        print("Added %s to %s." % (element, list1))


country_dict = {'Europe': ['Austria', 'Belarus', 'Germany']}
add_to_list_in_dict(country_dict, 'Asia', 'Afghanistan')
add_to_list_in_dict(country_dict, 'Scandinavia', 'Norway')
