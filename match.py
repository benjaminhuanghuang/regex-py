import re

regex = "hello"
text = "hello hello world!hello"
m = re.match(regex, text)
print m.group()

# Can not match. matching should start from beginning
text = "world!hello"
m = re.match(regex, text)
print m.group()
