# coding: utf-8
import sys

query = []
s = raw_input('->')
query.append(s)
while s:
    s = raw_input('->')
    query.append(s)
print filter(lambda x: x!='', query)
