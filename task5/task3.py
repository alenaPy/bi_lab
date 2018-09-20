"""Task5."""


def except_dev_by_zero(n):
    """Detect zero division."""
    try:
        return n/0
    except ZeroDivisionError:
        print("Couldn't divide by zero!")


def print_list_element(thelist, index):
    """Detect index error."""
    try:
        print(thelist[index])
    except IndexError:
        print("Index error!")


def add_to_list_in_dict(thedict, listname, element):
    """Detect dict index."""
    try:
        listt = thedict[listname]
    except KeyError:
        print("Listname doesn't exist")
        thedict[listname] = []
        print("Created %s." % listname)
    else:
        print("%s already has %d elements." % (listname, len(listt)))
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


if __name__ == '__main__':
    dic = {'1': [], '2': []}
    add_to_list_in_dict(dic, '2', 1)
