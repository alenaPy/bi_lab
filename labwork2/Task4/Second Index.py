"""You are given two strings and you have to find an index of the second
occurrence of the second string in the first one.
Let's go through the first example where you need to find the second
occurrence of "s" in a word "sims". It’s easy to find
its first occurrence with a function index or find which will point out that
"s" is the first symbol in a word "sims" and
therefore the index of the first occurrence is 0. But we have to find the
second "s" which is 4th in a row and that means
that the index of the second occurrence (and the answer to a question) is 3.
Input: Two strings.
Output: Int or None"""


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """

    # your code here
    def found_index(text, symbol):
        if text.count(symbol) < 2:
            return None
        else:
            return text.find(symbol, text.find(symbol) + 1)

    return found_index(text, symbol)
