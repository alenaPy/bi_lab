"""Exception Practice."""


# Dividing 5 by zero.
def zero_div():
    """Division by zero."""
    x, y = 5, 0
    try:
        x / y
    except ZeroDivisionError:
        print('Division by zero error. You must not divide by zero.')


zero_div()

# Handling exception of broking the list boundaries.
lst = [1, 2, 3]


def print_list_element(lst, index):
    """Index is out of boundary error."""
    try:
        print(lst[index])
    except IndexError:
        print('Index is out of boundaries.')


print_list_element(lst, 3)


def add_to_list_in_dict(the_dict, list_name, element):
    """Add an element to a list inside a dict of lists."""
    try:
        lst1 = the_dict[list_name]
    except KeyError:
        print("The dictionary doesn't contain the list %s" % list_name)
        the_dict[list_name] = []
        lst1 = the_dict[list_name]
    else:
        print("Existing_list is", str(lst1))
    finally:
        lst1.append(element)
        print("Added %s to %s." % (element, list_name))


dict1 = {'clothes': ['skirt', 'dress', 'jeans']}
add_to_list_in_dict(dict1, 'clothes', 'pullover')
add_to_list_in_dict(dict1, 'coffee', 'latte')
