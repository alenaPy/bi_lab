"""Exceptions."""

# 1


def division_zero():
    """Division by zero."""
    x, y = 26, 0
    try:
        x / y
    except ZeroDivisionError:
        print('Division by zero error.')


division_zero()


# 2
def print_list_element(the_list, index):
    """Index error."""
    try:
        print(the_list[index])
    except IndexError:
        print('Index = ' + str(index) + ' out of range. List length = ' +
              str(len(the_list)))


print_list_element([1, 7], 12)


# 3
def add_to_list_in_dict(the_dict, list_name, element):
    """Add an element to a list inside a dict of lists."""
    try:
        existing_list = the_dict[list_name]

    except KeyError:
        print("The dictionary doesn't contain the list %s" % list_name)
        the_dict[list_name] = []
        existing_list = the_dict[list_name]

    else:
        print("Existing_list is", str(existing_list))

    finally:
        existing_list.append(element)
        print("Added %s to %s." % (element, list_name))


cars_dict = {'fruits': ['apple', 'pear', 'cherry']}
add_to_list_in_dict(cars_dict, 'fruits', 'orange')
add_to_list_in_dict(cars_dict, 'flowers', 'rose')