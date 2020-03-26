# Regular expressions

import re

pattern = re.compile(r'abc')    # use raw string

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
