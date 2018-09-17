"""Function which returns first word of input string."""


def first_word(text):
    """Return first word of input string."""
    split_text = text.replace(',', ' ').replace('.', ' ').strip(' ').split(' ')
    return split_text[0].rstrip(',')
