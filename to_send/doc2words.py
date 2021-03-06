# encoding: utf-8 

import re

SPLIT_RGX = re.compile(r'\w+', re.U)

def extract_words(text):
    words = re.findall(SPLIT_RGX, text)
    return set(map(lambda s: s.lower(), words))
