'''
Regex Quantifier Tutorial: Greedy, Lazy, Possessive - RexEgg
http://www.rexegg.com/regex-quantifiers.html

Adding ? after the qualifier makes it perform the match in non-greedy or minimal fashion;
'''
import re

str = "1234567890 Greedy Lazy Possessive"

regex = "\d"
result = re.findall(regex, str)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print result

regex = "\d+"
result = re.findall(regex, str)  # ['1234567890']
print result

regex = "\d+?"
result = re.findall(regex, str)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print result

regex = "\d{2,3}"
result = re.findall(regex, str)  # ['123', '456', '789']
print result

regex = "\d{2,3}?"
result = re.findall(regex, str)  # ['12', '34', '56', '78', '90']
print result

regex = "\w{2,10}"
result = re.findall(regex, str)  # ['1234567890', 'Greedy', 'Lazy', 'Possessive']
print result

regex = "\w{5,}"
result = re.findall(regex, str)  # ['1234567890', 'Greedy', 'Possessive']
print result

str = "<a> b <c>"
regex = "<.*>"
result = re.findall(regex, str)  # ['<a> b <c>']
print result

regex = "<.*?>"
result = re.findall(regex, str)  # ['<a>', '<c>']
print result
