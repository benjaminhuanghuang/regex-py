import re

text = ""

file = open('poem.txt')
for line in file:
    text += line
file.close()

print text

#
#  How many "to"
#
result = re.findall('to', text)
print result
print len(result)

#
#  Find words A??
#
reg_pattern = "a.."  # will match "a b"
reg_pattern = "a[a-z][a-z]"  # will match "part"
reg_pattern = " a[a-z][a-z] "  # will match " abc "
reg_pattern = " (a[a-z][a-z]) "  # will match "abc" int " abc "
reg_pattern = " ([Aa][a-z][a-z]) "  # will match "abc" or "Abc" int " abc "
reg_pattern = " +([Aa][a-z][a-z]) "  # will match "abc" or "Abc" does not follow " "

result = re.findall(reg_pattern, text)
print result
print len(result)
result = set(result)
print list(result)

reg_group_pattern = " (a[a-z][a-z]) |(A[a-z][a-z]) "  # will match "abc" or "Abc" without " "
result = re.findall(reg_group_pattern, text)  # get [('', 'And'), ('all', ''), ('', 'All'), ('and', '')]
final_res = set()
for pair in result:
    if pair[0]:
        final_res.add(pair[0])
    if pair[1]:
        final_res.add(pair[1])
print list(final_res)
