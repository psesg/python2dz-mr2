#!/usr/bin/env python

import sys
import random

# python mapper_py2.py < part1.txt | sort | python reducer_py2.py | head -10000
# if head < 10000 will be "BrokenPipeError: [Errno 32] Broken pipe" generated

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

i = 1
rnd_num = random.randint(1, 5)
out_str = ""

for line in sys.stdin:
    try:
        line = unicode(line.strip("\n"))
        line = unicode(line.strip("\t"))
    except ValueError as e:
        continue
    else:
        line = line[5:]

        if i == rnd_num:
            out_str = out_str + line
            print "%s" % out_str
            i = 1
            rnd_num = random.randint(1, 5)
            out_str = ""
        else:
            out_str = out_str + line + ","
            i += 1

if len(out_str) > 1:
    if out_str[-1] == ',':
        out_str = out_str[:-1]
    print "%s" % out_str

