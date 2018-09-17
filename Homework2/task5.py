"""Function which prints string between set markers."""


def between_markers(text, begin, end):
    """Print string between set markers."""
    if text.find(begin) == -1 and text.find(end) != -1:
        return text[:text.find(end)]
    elif text.find(begin) != -1 and text.find(end) == -1:
        return text[text.find(begin) + len(begin):]
    elif text.find(begin) == -1 and text.find(end) == -1:
        return text
    return text[text.find(begin) + len(begin):text.find(end)]
