# task5.


def between_markers(text: str, begin: str, end: str) -> str:

    if begin not in text:
        first_symb = 0
    else:
        first_symb = text.find(begin) + len(begin)

    if end in text:
        second_symb = text.find(end)
    else:
        second_symb = len(text)

    return text[first_symb:second_symb]


if __name__ == '__main__':

    print('Example:')

print(between_markers('What is >apple<', '>', '<'))


assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
assert between_markers("<head><title>My new site</title></head>",
                       "<title>", "</title>") == "My new site", "HTML"
assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
print('Wow, you are doing pretty good. Time to check it!')
