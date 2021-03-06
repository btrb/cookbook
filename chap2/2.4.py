# Matching and Searching for Text Patterns

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
text == 'yeah'

# Match at start or end
text.startswith('yeah')
text.endswith('no')

# Search for the location of the first occurence
text.find('no')


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')


datepat = re.compile(r'\d+/\d+/\d+')

if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')


text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
datepat.findall(text)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
text
datepat.findall(text)

# As a list:
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# Iteratively:
for m in datepat.finditer(text):
    print(m.groups())


# Discussion

m = datepat.match('11/27/2012abcdef')
m
m.group()

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef')
datepat.match('11/27/2012')

re.findall(r'(\d+)/(\d+)/(\d+)', text)