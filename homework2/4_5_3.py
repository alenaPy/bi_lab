"""PopularWordsTask."""


def popular_words(text, words):
    """Work with text."""
    text = text.lower()

    text = text.replace('\n', ' ')

    words_list = text.split(' ')

    return {word: words_list.count(word) for word in words}
