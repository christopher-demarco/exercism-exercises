#!/usr/bin/env python

import re

def word_count(words_str):
    words_str = re.sub('\s+', ' ', words_str.decode('utf-u')) # clean it

    words_str = re.sub('(\w)[,_](\w)', r'\1 \2', words_str)

    words = map(lambda w: re.sub('\W', '', w),
                map(lambda w: w.lower(), words_str.split(' ')))
    words = [ w for w in words if w is not '']
    d = { }
    for w in words:
        try:
            d[w] += 1
        except KeyError:
            d[w] = 1
    return d

