'''
Positive look ahead: This mechanism is represented as an expression preceded by a question mark and an equals sign,
        ?=, inside a parenthesis block.
        For example, (?=regex) will match if the passed regex do match against the forthcoming input.
'''
import re

# match any word that is followed by a comma (,)
pattern = re.compile(r'\w+,')
print pattern.findall("They were three: Felix, Victor, and Carlos.")  # ['Felix,', 'Victor,']

pattern = re.compile(r'\w+(?=,)')
print pattern.findall("They were three: Felix, Victor, and Carlos.")  # ['Felix', 'Victor']

pattern = re.compile(r'\w+(?=,|\.)')
print pattern.findall("They were three: Felix, Victor, and Carlos.")  # ['Felix', 'Victor', 'Carlos']

text = "The quick brown fox jumps over the lazy dog"
pattern = re.compile(r'fox')
result = pattern.search(text)
print text.index("fox")
print result.group(0)
print result.start(), result.end()  # 16 19

pattern = re.compile(r'(?=fox)')
result = pattern.search(text)
print result.group(0)
print result.start(), result.end()  # 16 16
