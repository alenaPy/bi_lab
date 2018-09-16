"""
Task_1 from CheckIO.

On CheckIO your solution should be a function.
The function should return the right answer, not print it.
"""


def say_hi(name: str, age: int) -> str:
    """Say Hi to CheckIO."""
    string = "Hi. My name is %s and I'm %d years old" % (name, age)
    return string


if __name__ == '__main__':
    # These "asserts" using only for self-checking
    first_res = "Hi. My name is Alex and I'm 32 years old"
    assert say_hi("Alex", 32) == first_res, "First"
    second_res = "Hi. My name is Frank and I'm 68 years old"
    assert say_hi("Frank", 68) == second_res, "Second"
    print('Done. Time to Check.')

"""Task_2 from CheckIO. """


def correct_sentence(text: str) -> str:
    """Return a corrected sentence.

    It starts with a capital letter and ends with a dot.
    """
    text_mas = []
    if not text.endswith('.'):
        text_mas.append(text)
        text_mas.append('.')
        text = ''.join(text_mas)

    if not text[0].isupper():
        text_mas.clear()
        text_mas.append(text[0].upper())
        text_mas.append(text[1:])
        text = ''.join(text_mas)

    return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")

"""Task_3 from CheckIO."""


def first_word(text: str) -> str:
    """Return the first word in a given text."""
    for i in ',.':
        text = text.replace(i, ' ')

    text = text.strip()
    first_w_pos = text.strip().find(' ')
    if first_w_pos != -1:
        text = text[:first_w_pos]
    return text


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"

    print("Coding complete? Click 'Check' to earn cool rewards!")

"""Task_4 from CheckIO."""


def difference(*args):
    """Return difference between min and max value."""
    if args:
        min_n = min(args)
        max_n = max(args)
        return max_n - min_n
    else:
        return 0


# These "asserts" using only for self-checking
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        """Compare result of our function and right answer."""
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    res_third = "10.2-(-2.2)=12.4"
    assert almost_equal(difference(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(difference(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(difference(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), res_third
    assert almost_equal(difference(), 0, 3), "Empty"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""Task_5 from CheckIO."""


def left_join(phrases):
    """Join strings and replace "right" to "left"."""
    new_string = []
    for i in phrases:
        i = i.replace("right", "left")
        new_string.append(i)
    text = ','.join(new_string)
    return text


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    first_list = ("left", "right", "left", "stop")
    second_list = ("bright aright", "ok")
    third_list = ("brightness wright",)
    four_list = ("enough", "jokes")
    assert left_join(first_list) == "left,left,left,stop", "All to left"
    assert left_join(second_list) == "bleft aleft,ok", "Bright Left"
    assert left_join(third_list) == "bleftness wleft", "One phrase"
    assert left_join(four_list) == "enough,jokes", "Nothing to replace"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
