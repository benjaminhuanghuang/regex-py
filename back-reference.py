import re

# find repeating word
text = "the1 the ory math math "

regex = r"\bthe\b"  # match ['the', 'the']
regex = r"\b([A-Za-z]+) +\1\b"

result = re.findall(regex, text)
print result