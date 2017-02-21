import re

test_string = ('A regular expression is a pattern which specifies a set of strings of characters; '
               'it is said to match certain strings.')

print re.findall(r'regular', test_string)  # ['regular']
# metachar
print re.findall(r'strings\.', test_string)  # ['strings.']

test_string = '''! " # $ % & ' ( ) * + , - . /
0 1 2 3 4 5 6 7 8 9
: ; < = > ? @
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
[ \ ] ^ _ `
a b c d e f g h i j k l m n o p q r s t u v w x y z
{ | } ~
'''

print re.findall(r'[0-9]', test_string)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print re.findall(r'\d', test_string)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print re.findall(r'[0-3]', test_string)  # ['0', '1', '2', '3']
