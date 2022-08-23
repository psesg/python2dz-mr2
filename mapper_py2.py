#!/usr/bin/env python


import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

stop_words = set()
with open("stop_words_en.txt") as fd:
    for line in fd:
        stop_words.add(line.strip())


for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    text = re.sub(r'[^A-Za-z\\s]', ' ', text)
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        word = word.lower()
        # print >> sys.stderr, "reporter:counter:Custom stats,All words,{}".format(1)
        if word in stop_words or len(word) < 3:
            # print >> sys.stderr, "reporter:counter:Custom stats,Stop words,{}".format(1)
            continue
        print "%s\t%d" % (word, 1)



