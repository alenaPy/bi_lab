# 1


def division_zero():

    x, y = 5, 0
    try:
        x / y
    except ZeroDivisionError:
        print('Division by zero error.')
        print('-----------------------')


division_zero()

# 2


def print_all_elements(the_list, index):
    try:
        print(the_list[index])
    except IndexError:
        print('Index = ' + str(index) + ' out of range. List length = ' +
              str(len(the_list)))


print_all_elements([1, 5], 20)

# 3


def add_element(the_dict, list_name, element):
    try:
        existing_list = the_dict[list_name]
    except KeyError:
        print("The dictionary doesn't contain the list %s" % list_name)
        print('---------------------------------------------')
        the_dict[list_name] = []
        existing_list = the_dict[list_name]
    else:
        print("Existing_list is", str(existing_list))
    finally:
        existing_list.append(element)
        print("Added %s to %s." % (element, list_name))


dictionary = {'cars': ['Skoda', 'Audi', 'Mercedes']}
add_element(dictionary, 'Kia', 'Reno')
add_element(dictionary, 'Volvo', 'Ford')
