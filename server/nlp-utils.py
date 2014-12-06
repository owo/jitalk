#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import word_tokenize

def stem_tokens(token_list, src_lang):
    stemmed = []

    if src_lang == 'en':
        ps = PorterStemmer()
        for token in token_list:
            stemmed.append(ps.stem(token))
    
    if src_lang == 'ar':
        isri = ISRIStemmer()
        for token in token_list:
            stemmed.append(isri.stem(token))

    return stemmed


def tokenize(sent):
    return word_tokenize(sent)
