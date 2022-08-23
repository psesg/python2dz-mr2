#!/usr/bin/env python

import sys
import string
import random


def randstr(chars=string.hexdigits, n=5):
    return ''.join(random.choice(chars) for _ in xrange(n))


reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

for line in sys.stdin:
    try:
        article_id = unicode(line.strip("\n"))
    except ValueError as e:
        continue
    print "%s%s" % (randstr(), article_id)
