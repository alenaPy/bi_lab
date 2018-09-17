# task4.


def second_index(text: str, symbol: str) -> [int, None]:

    if text.count(symbol) < 2:
        return None

    return text.find(symbol, text.find(symbol) + 1)


if __name__ == '__main__':

    print('Example:')
    print(second_index("sims", "s"))

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
