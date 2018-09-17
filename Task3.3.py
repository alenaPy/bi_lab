"""DictionaryPractice."""


def generate_numbers(number=20):
    """GenerateNumbers."""
    dict1 = {}
    for key in range(1, number + 1):
        dict1[key] = key * key
    return dict1

    print(generate_numbers())
    print()


count_me_string = input('Enter text: ')


def count_characters(count_me_string):
    """CountCharacters."""
    dict2 = {}
    for i in count_me_string:
        dict2[i] = count_me_string.count(i)
    return dict2

    print(count_characters(count_me_string))
