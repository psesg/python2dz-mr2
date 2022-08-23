#!/usr/bin/env python

import sys
import random

# python mapper_py2.py < part1.txt | sort | python reducer_py2.py | head -10000
# if head < 10000 will be "BrokenPipeError: [Errno 32] Broken pipe" generated
# python mapper_py2.py < test.txt | sort | python reducer_py2.py

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

prev_sortword = ""
voc = {}
count = 0

for line in sys.stdin:
    try:
        #line = unicode(line.strip("\n"))
        sortword, word, one = unicode(line.strip("\n")).split('\t', 2)
    except ValueError as e:
        continue
    else:
        # print "%s\t%s\t%s" % (sortword, word, one)
        if prev_sortword == "":
            prev_sortword = sortword
            count += 1
        else:
            if sortword == prev_sortword:
                count += 1
            else:
                print "%s\t%d" % (prev_sortword, count)
                prev_sortword = sortword
                count = 1
if count > 0:
    print "%s\t%d" % (sortword, count)







