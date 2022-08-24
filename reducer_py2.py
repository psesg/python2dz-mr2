#!/usr/bin/env python

import sys
import operator
from collections import OrderedDict

# python mapper_py2.py < part1.txt | sort | python reducer_py2.py | head -10000
# if head < 10000 will be "BrokenPipeError: [Errno 32] Broken pipe" generated
# python mapper_py2.py < articles-part.txt | sort | python reducer_py2.py | sort -k2,2nr -k1

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
            voc[word] = voc.get(word, 0) + 1
        else:
            if sortword == prev_sortword:
                count += 1
                voc[word] = voc.get(word, 0) + 1
            else:
                sort_voc_str = ""
                sort_voc = OrderedDict(sorted(voc.items(), key=operator.itemgetter(1), reverse=True))
                for i, (k, v) in enumerate(sort_voc.items()):
                    #print(i, k, v)
                    if i < 5:
                        sort_voc_str = sort_voc_str + k + ":" + str(v) + ";"  # + "[" + str(i) + "]"
                print "%s\t%d\t%s" % (prev_sortword, count, sort_voc_str)
                prev_sortword = sortword
                count = 1
                voc = {}
                voc[word] = voc.get(word, 0) + 1
if count > 0:
    sort_voc_str = ""
    sort_voc = OrderedDict(sorted(voc.items(), key=operator.itemgetter(1), reverse=True))
    for i, (k, v) in enumerate(sort_voc.items()):
        # print(i, k, v)
        if i < 5:
            sort_voc_str = sort_voc_str + k + ":" + str(v) + ";"  # + "[" + str(i) + "]"
    print "%s\t%d\t%s" % (prev_sortword, count, sort_voc_str)







