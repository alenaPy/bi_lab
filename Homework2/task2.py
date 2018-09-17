"""Function which corrects input sentence."""


def correct_sentence(text):
    """Correct input sentence."""
    if text[-1] != '.':
        text += "."
    return text[0].upper() + text[1:]
