import re

#  case sensitive demo 1: find word "class"
text = 'no class at all. the subclass is. the declassified algorithm. Class is over. CLASS is starting'

print re.findall(r"class", text)
print re.findall(r"class", text, re.IGNORECASE)
print re.findall(r"\bclass\b", text, re.IGNORECASE)

print re.search(r'(?i)class', text).group()      #only return the first math

matchs = re.finditer(r'(?i)class', text)         # return all matches
for m in matchs:
    print m.group()
