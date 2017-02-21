# -*- coding: utf-8 -*-
import re

# Chinese
text = u'北京北|VAP|北京东|BOP|北京|BJP'
result = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
for r in result:
    print r[0]
print result  # Note, python can not display chinese character in object or list

sample = u'I am 北京 from 美国。We should be friends. 朋友。'
res = re.findall(ur'[\u4e00-\u9fff]+', sample)
print res
for n in res:
    print n
