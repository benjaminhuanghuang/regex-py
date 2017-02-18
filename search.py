'''
re.search(pattern, string, flags)
return MatchObject

'''

import re

regex = "234"
text = "1234567890"
m = re.search(regex, text)
print m.group()
