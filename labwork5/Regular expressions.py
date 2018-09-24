import re

# task 1.1
text = 'gswdhc@epa.com djfbgh fdfivgidebvfu@mail.ru vbdsbvj sonskvn@gmail.com'
print(re.findall(r'\w+@\w+\.\w+', text))


# task 1.2
text = 'wreyru erfh elfjrlfje ldfl nfn fn'
all_words = re.findall(r'\w+', text)
for word in all_words:
    if len(word) in {3,5}:
        print(word)


# task 1.3
text = 'wreyru erfh elfjrlfje ldfl nfn fn6 7 086 340'
print(re.findall(r'\d+', text))

# task 1.4
s = 'wreyru erfh    elf_jrlfje ldfl nfn fn6 7 86 340'


def replace_char(match_object):
    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


s = re.sub('\s|_', replace_char, s)  # что, чем, где
print(s)
