"""
Description of script.

The results of task4.
"""


def say_hi(name: str, age: int) -> str:
    """Hi."""
    return "Hi. My name is {0} and I'm {1} years old".format(name, age)


if __name__ == '__main__':
    assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"


def correct_sentence(text: str) -> str:
    """Return a sentence which starts with a cap letter and dot at the end."""
    if not text.endswith("."):
        text += "."
    text = text[0].upper() + text[1:]
    return text


if __name__ == '__main__':
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."


def first_word(text: str) -> str:
    """Return the first word in a given text."""
    import re
    text = re.sub('[,.]', ' ', text)
    text = text.strip(' ')
    return text.split(' ')[0]


if __name__ == '__main__':
    assert first_word("s.s") == "s"
    assert first_word(" a word ") == "a"
    assert first_word("... and so on ...") == "and"


def second_index(text: str, symbol: str) -> [int, None]:
    """Return the second index of a symbol in a given text."""
    if text.find(symbol) == -1:
        return None
    else:
        pos = text.find(symbol)
        if text[pos + 1:].find(symbol) == -1:
            return None
        else:
            return (text[pos + 1:].find(symbol) + 1) + pos


if __name__ == '__main__':
    assert second_index("s.s", "s") == 2
    assert second_index(" a word ", " ") == 2
    assert second_index("... and so on ...", "1") is None


def between_markers(text: str, begin: str, end: str) -> str:
    """Return substring between two given marks."""
    if text.find(begin) == -1 and text.find(end) == -1:
        return text
    elif text.find(begin) == -1:
        return text[:text.find(end)]
    elif text.find(end) == -1:
        return text[text.find(begin) + len(begin):]
    elif text.find(end) < text.find(begin):
        return ""
    else:
        return text[text.find(begin) + len(begin):text.find(end)]


if __name__ == '__main__':
    assert between_markers("s.s,s", ".", ",") == "s"
    assert between_markers(" a wor[.d] ", "w", "[.d]") == "or"
