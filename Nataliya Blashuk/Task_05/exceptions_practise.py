"""Task3 exceptions practice."""

# 1 DevisionError exception


def division_by_zero(a=5, b=0):
    """Catch the DevisionError exception."""
    try:
        a/b
    except ZeroDivisionError:
        print("Error! Division by zero is mistake")


division_by_zero()

# 2 IndexError exception


def print_list_element(the_list, index):
    """Handle a possible IndexError."""
    try:
        print(the_list[index])
    except IndexError:
        print("Index %d is out of range. List length is %d" %
              (index, len(the_list)))


print_list_element([1, 3, 5, 7], 9)

# 3 KeyError exception


def add_to_list_in_dict(the_dict, list_name, element):
    """Add an element to a list inside a dict of lists."""
    try:
        exst_list = the_dict[list_name]
    except KeyError:
        print("The dictionary hasn`t got the list %s" % list_name)
        the_dict[list_name] = []
        exst_list = the_dict[list_name]
    else:
        print("Existing list is ", str(exst_list))
    finally:
        exst_list.append(element)
        print("Added %s to %s." % (element, list_name))


names = {"Female": ["Hilary", "Kate", "Fiona"]}
add_to_list_in_dict(names, "Male", "Jack")
add_to_list_in_dict(names, "Female", "Rose")
