#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.stem.porter import PorterStemmer
from nltk.stem.isri import ISRIStemmer
from nltk.tokenize import word_tokenize
import nltk.data


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


def stem_tokens(token_list, src_lang):
    """
    Returns the stem of a given word depending on the source language.
    """

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
    """
    Tokenizes a string first into sentences, then into tokens.
    The result is a list of list of tokens.
    """
    sentences = sent_detector.tokenize(sent)
    res = []

    for s in sentences:
        res.append(word_tokenize(s.strip()))

    return res
