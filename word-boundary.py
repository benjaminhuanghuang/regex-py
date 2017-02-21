#
# ---  Boundaries
#

import re

#  word boundary demo 1: find word "class"
text = 'no class at all. the subclass is. the declassified algorithm'
print re.findall(r"class", text)
print re.findall(r"\bclass\b", text)

test_string = 're great'

print re.findall(r're', test_string)  # ['re', 're']

# \b the boundary of word
print re.findall(r'\bre\b', test_string)  # ['re']
m = re.search(r'\bre\b', test_string)  # ['re']
print m.start(), m.end()  # 0 2

# \B Non-word boundary
print re.findall(r'\Bre\B', test_string)  # return the second ['re']
m = re.search(r'\Bre\B', test_string)  # ['re']
print m.start(), m.end()  # 4 5
