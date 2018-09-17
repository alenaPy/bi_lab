# 1. on CheckiO your solution should be a function
# 2. the function should return the right answer, not print it.
# task1.


def say_hi(name: str, age: int) -> str:

    return "Hi. My name is %s and I'm %d years old" % (name, age)


if __name__ == '__main__':

    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", "First"
    assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", "Second"
    print('Done. Time to Check.')
