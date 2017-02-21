#
# ---  Boundaries
#

import re

test_string = 're great'

print re.findall(r're', test_string)  # ['re', 're']

# \b the boundary of word
print re.findall(r'\bre\b', test_string)  # ['re']

# \B Non-word boundary
print re.findall(r'\Bre\B', test_string)  # ['re']

