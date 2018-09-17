"""Introduce a person with a given parameters in attributes."""


def say_hi(name: str, age: int) -> str:
    """SayHi."""
    return "Hi. My name is %s and I'm %d years old" % (name, age)


if __name__ == '__main__':
    Alex = "Hi. My name is Alex and I'm 32 years old", "First"
    Frank = "Hi. My name is Frank and I'm 68 years old", "Second"
    assert say_hi("Alex", 32) == Alex
    assert say_hi("Frank", 68) == Frank
    print('Done. Time to Check.')


"""Starts with a capital letter and ends with a dot."""


def correct_sentence(text: str) -> str:
    """CorrectSentence."""
    if text.endswith('.'):
        text
    else:
        text += '.'
    return text[0].upper() + text[1:]


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")


"""You are given a string where you have to find its first word.
There can be dots and commas in a string.
A string can start with a letter or, for example, a dot or space.
A word can contain an apostrophe and it's a part of a word.
The whole text can be represented with one word and that's it."""


def first_word(text: str) -> str:
    """FirstWord."""
    text = text.replace(',', ' ')
    text = text.replace('.', ' ')
    text = text.strip()
    return text.split(' ')[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")


"""Index of the second occurrence of the second string in the first one."""


def second_index(text: str, symbol: str) -> [int, None]:
    """SecondIndex."""
    count_s = text.count(symbol)
    first_pos = text.find(symbol)
    if count_s >= 2:
        pos = text.find(symbol, first_pos+1)
    else:
        pos = None
    return pos


if __name__ == 'main':

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
