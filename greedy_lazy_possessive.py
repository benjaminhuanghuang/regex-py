# coding=utf-8

#
# ---  Greedy, Lazy and Possessive）
# http://icejoywoo.github.io/2015/09/12/python-regex.html#greedylazypossessive


import re

print re.match(r'\d{3}', '123456').group()  # 123
print re.match(r'\d{3,6}', '123456').group()  # 123456
print re.match(r'\d{3,6}678', '12345678').group()  # 12345678

# Lazy, as less as possible
print re.match(r'\d{3,6}?', '123456').group()  # 123
print re.match(r'\d{3,6}?678', '12345678').group()  # 12345678

# 占用量词，python不支持，可以在regex101使用pcre(php)来测试
# print re.match(r'\d{3,6}+678', '12345678')  # None
# 无法匹配成功，因为\d{3,6}+会直接匹配123456，后面只剩下78，并且不回溯，无法匹配剩下的678
