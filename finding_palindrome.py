"""
Description of script.

It gives you simple usage of regular expressions to find out palindrome line.
Some examples of palindrome:.
# Never odd or even.
# Madam, I'm Adam.
"""

import re
line = re.sub('[ ,&?!\'.;:*/_0132456789\-]', '',
              input('Enter palindrome string: ').lower())
if line != "" and line == ''.join(reversed(line)):
    print("It is palindrome!")
else:
    print("It is not palindrome")
