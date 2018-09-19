"""Solution for Exception practice."""

# Dividing 5 by 0.
try:
    5 / 0
except ZeroDivisionError:
    print('You must not divide by zero.')

# Handling exception of broking the list boundaries.
list1 = []


def print_list_element(thelist, index):
    """Print the list element."""
    try:
        print(thelist[index])
    except IndexError:
        print('The list\'s boundaries were broken.')


print_list_element(list1, 0)

# Handling exception of not existing list in the dictionary.
dict1 = {'suka': []}


def add_to_list_in_dict(thedict, listname, element):
    """Write an element to the list in the dictionary."""
    try:
        list1 = thedict[listname]
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(list1)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


add_to_list_in_dict(dict1, 'suka1', 'puk')
