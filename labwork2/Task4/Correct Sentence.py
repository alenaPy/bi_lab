"""For the input of your function will be given one sentence. You have to
return its fixed copy in a way so it’s always starts with a capital letter
and ends with a dot.
Pay attention to the fact that not all of the fixes is necessary. If a sentence
already ends with a dot then adding another one will be a mistake.
Input: A string.
Output: A string."""


def correct_sentence(text: str) -> str:
    """Returns a corrected sentence which starts with a capital letter
    and ends with a dot."""

    # your code here
    text = text[0].upper() + text[1:]
    if text[len(text) - 1] != '.':
        text = text + '.'
    return text
