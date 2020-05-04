# Check regex_snippets.txt
# /d /D /w /W /s /S
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

mat
hat
cat
bat
'''


sentence = 'Start a sentence and then bring it to an end'

# search pattern
# pattern = re.compile(r'\W')

# find matches
# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 1. Match phone number
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 2. Match in another file
# with open('regex_data.txt', 'r') as f:
#     contents = f.read()

# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# matches = pattern.finditer(contents)

# for match in matches:
#     print(match)


# 3. Match character set
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 4. Match detailed character set
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 5. Ranged characters using '-'
# pattern = re.compile(r'[a-zA-Z0-9]')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 6. Negates single character using '^'
# pattern = re.compile(r'[^b]at')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 7. Fixed number quantifier
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 8. Suffix quantifier using '*'
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 9. Group of patterns
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# 10. Email address exercise
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-z0-9.-]+@[a-z-]+\.(com|edu|net)')

# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)


# 11. url address exercise
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))  # 0 for entire pattern

# reformat with only group 2 and 3
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# print all matches
all_matches = pattern.findall(urls)
print(all_matches)

# print first match
match = pattern.search(urls)
print(match)


# 12. Flags
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'start', re.I)  # IGNORECASE

matches = pattern.search(sentence)

print(matches)