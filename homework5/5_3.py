"""Exceptions."""


def division_zero():
    """ZeroDivisionError."""
    x, y = 5, 0

    try:

        x / y

    except ZeroDivisionError:

        print('Division by zero error.')


division_zero()


def print_list_element(the_list, index):
    """IndexError."""
    try:

        print(the_list[index])

    except IndexError:

        x = str(len(the_list))

        print('Index is ' + str(index) + ' out of range. List length = ' + x)


print_list_element([1, 2], 25)


def add_to_list_in_dict(dict1, list1, element):
    """Error."""
    try:

        current_list = dict1[list1]

    except KeyError:

        print("Dictionary has no list %s" % list1)

        dict1[list1] = []

        current_list = dict1[list1]

    else:

        z = str(current_list)

        print("List has ", z)

    finally:

        current_list.append(element)

        print("Added %s to %s." % (element, list1))


country_dict = {'Cars': ['Audi', 'Toyota', 'BMV']}

add_to_list_in_dict(country_dict, 'Airplane', 'Boeing')

add_to_list_in_dict(country_dict, 'Helicopter', 'Lynx')
