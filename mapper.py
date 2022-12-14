#!/usr/bin/env python


import sys
import re
import itertools

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

stop_words = set()
with open("stop_words_en.txt") as fd:
    for line in fd:
        stop_words.add(line.strip())

mx = 0
mxstr = ''
mxnumline = 0
numline = 0

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip("\n")).split('\t', 1)
    except ValueError as e:
        continue
    numline += 1
    text = re.sub(r'[^A-Za-z\\s]', ' ', text)
    #text = re.sub(r'(.)\1+', r'\1\1', text)  # long cccccccc...
    #text = re.sub(r'^(.+?)\1+$', r'\1', text)  # long abababab...
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        word = word.lower()
        if len(word) < 3 or len(word) > 16: # word in stop_words or
            continue
        if len(word) > mx:
            mx = len(word)
            mxstr = word
            mxnumline = numline
        sortword = ''.join(sorted(word))
        print "%s\t%s\t%d" % (sortword, word, 1)
#print "mxnumline = %d mx = %d %s" % (mxnumline, mx, mxstr)



