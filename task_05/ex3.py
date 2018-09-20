"""Exceptions practice."""


def divbyzero_test():
    """Compute 5/0 and use try/except to catch the DivisionError exception."""
    try:
        5 / 0
    except ZeroDivisionError:
        print('Error: Division by zero')


divbyzero_test()


def print_list_element(thelist, index):
    """Handle a possible IndexError."""
    try:
        print(thelist[index])
    except IndexError:
        print('Error: Index out of range')


print_list_element([5, 7, 7, 45, 6, 46, 66, 6], 1)


def add_to_list_in_dict(thedict, listname, element):
    """Add an element to a list inside a dict of lists."""
    try:
        lst = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(lst)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


add_to_list_in_dict({1: [2, 545, 55, 325, 25, 5, 35623562]}, 2, 3)
