"""Completed tasks from site py.checkio.org."""


# Exercise 1
def say_hi(name: str, age: int) -> str:
    """Task Say Hi."""
    return "Hi. My name is %s and I`m %d years old" % (name, age)


# Exercise 2
def correct_sentence(text: str) -> str:
    """Task Correct Sentence."""
    text = text[::1].capitalize()
    if not text.endswith("."):
        text += "."
    return text


# Exercise 3
def first_word(text: str) -> str:
    """Task First Word."""
    text = text.replace(".", " ").replace(",", " ").lstrip(" ")
    f_word = text.find(" ")
    return text[0:f_word]
