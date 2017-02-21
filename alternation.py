import re

text = "grey gray gr|y"

regex = "gr[ea]y"  # match gray grey
print re.findall(regex, text)

regex = "grey|gray"  # match gray grey
print re.findall(regex, text)

regex = "gr(a|e)y"  # match gray grey
print re.findall(regex, text)

regex = "gr[a|e]y"  # match gray gr|y grey
print re.findall(regex, text)

match = re.search("Espan(a|ol)", "Espana")
print match.group(0)

text = "July fourth Jul 4 "
regex = r'July? (fourth|4)'
# regex = r"July? (?=fourth|4(th)?)"
match = re.finditer(regex, text)
for m in match:
    print m.group(0)

result = re.findall(regex, text)
print result
