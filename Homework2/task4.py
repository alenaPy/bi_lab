"""Function which returns index of the second occurrence of the substring."""


def second_index(text, symbol):
    """Return index of the second occurrence of the input substring."""
    position = text.find(symbol, text.find(symbol) + 1)
    if position == -1:
        return
    else:
        return position
