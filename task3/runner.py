"""Functions runner module."""
from inspect import getmembers, isfunction
import pytasks


def runner(*funcs):
    """Run functions implemented in pytasks module."""
    meta = [obj for obj in getmembers(pytasks) if isfunction(obj[1])]
    all_funcs = list(meta[i][0] for i in range(len(meta)))

    if len(funcs) == 0:
        res = all_funcs
    else:
        res = funcs
    for func in res:
        print(eval('pytasks.' + func + '()'))


# example
runner('fizzbuzz')
