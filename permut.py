#!/usr/bin/env python

import itertools
import datetime as dt

def permutations(s):
    if not s:
        return []
    partial = []
    partial.append(s[0])
    for i in range(1, len(s)):
        for j in reversed(range(len(partial))):
            curr = partial.pop(j)
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])
    return partial

test = "eerw"
print dt.datetime.now().isoformat()
pm = permutations(test)
print len(pm), pm
print dt.datetime.now().isoformat()
per = itertools.permutations(test)
i = 0
for val in per:
    i += 1
print i
print dt.datetime.now().isoformat()