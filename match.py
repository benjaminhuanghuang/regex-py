import re

regex = "hello"
text = "hello hello world!hello"
m = re.match(regex, text)
print m.group()

# Can not match. matching should start from beginning
text = "world!hello"
m = re.match(regex, text)
print m.group()

regex = "sh[abc]*"
result = re.match(regex, "shalom stdents")
if result:
    print "match"
else:
    print "Not match"
