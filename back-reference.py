import re

# find repeating word
text = "the the ory math math2"
regex = "\<([A-Za-z]+) +\1\>"
regex = "\b([A-Za-z]+)\b"
result = re.findall(regex, text)
print result