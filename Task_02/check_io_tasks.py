"""Checkio.org tasks."""


def say_hi(name, age):
    """Say hi.

    In this mission you should write a function that introduce a
    person with a given parameters in attributes.
    Input: Two arguments. String and positive integer.
    Output: String.
    """
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)


def correct_sentence(text):
    """Correct sentence.

    Return a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    return text[:1].upper() + text[1:]+'.' \
        if not text.endswith('.') else text.capitalize()


def first_word(text):
    """You are given a string where you have to find its first word."""
    text = text.replace('.', ' ').replace(',', ' ').strip()
    text = text.split()
    return text[0]


def second_index(text: str, symbol: str) -> [int, None]:
    """Return the second index of a symbol in a given text."""
    if text.count(symbol) < 2:
        return None
    first = text.find(symbol)
    return text.find(symbol, first + 1)


def between_markers(text: str, begin: str, end: str) -> str:
    """Return substring between two given markers."""
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        return text.split(end)[0]
    elif end not in text:
        return text.split(begin)[1]
    else:
        text_after_begin_marker = text.split(begin)[1]
        if end not in text_after_begin_marker:
            return ''
        else:
            return text_after_begin_marker.split(end)[0]
