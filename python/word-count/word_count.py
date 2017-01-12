# -*- coding: utf-8 -*-

import re

def word_count(words_str):

    words_str = re.sub('[\W_]',' ', words_str)
    words_str = re.sub('\s+', ' ', words_str)

    words = [ w.lower() for w in words_str.split(' ') if w is not '' ]

    d = { }
    for w in words:
        try: d[w] += 1
        except KeyError: d[w] = 1
    return d

