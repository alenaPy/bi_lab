"""Task5."""

import re

# task 1.1
string = 'svetlana_nesenchuk@epam.com bedjhfvuyew ' \
         'kiannet@gmail.com frjhgfru abc@gmail.com'
print(re.findall(r'\w+@\w+\.\w+', string))


# task 1.2
string = 'qwwertyuuio hjdfh bhr byey beby etr'
all_words = re.findall(r'\w+', string)
for word in all_words:
    if len(word) in (3, 4, 5):
        print(word)

# task 1.3
string = 'adwr rug uyrg7548 gfrheg874 487 fneur8'
print(re.findall(r'\d+', string))

# task 1.4
string = 'fdfnds_nfjdr eijfei_jrurbg_jef nbe efheu urgfur'


def replace_char(match_object):
    """Replace ' ' with '_' and '_' with ' '."""
    if match_object[0] == ' ':
        return '_'
    else:
        return ' '


string = re.sub('\s|_', replace_char, string)
print(string)
