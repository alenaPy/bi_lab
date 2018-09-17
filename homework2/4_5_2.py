"""FirstWordTask."""


def first_word(text: str) -> str:
    """Work with text."""
    text = text.replace(',', ' ')

    text = text.replace('.', ' ')

    text = text.strip()

    return text.split(' ')[0]
