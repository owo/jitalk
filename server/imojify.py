#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

from bottle import request, Bottle
import nlp_utils
import emoji_dict


re.LOCALE
re.UNICODE

punct_re = re.compile("^\W+$")
lutable = emoji_dict.gen_emoji_lookup_table('data/emoji_dump.json')

imojify_app = Bottle()


def imojify_sentence(sent):
	imojified = []
	for s in sent:
		if s in lutable:
			imojified.append(lutable[s][0]['image'])
		elif s == '?':
			imojified.append(lutable['question'][0]['image'])
		elif s == '!':
			imojified.append(lutable['exclamation'][0]['image'])
		elif punct_re.match(s) is None:
			imojified.append('link!')

	return imojified


def imojify_input(line):
	line = line.lower()
	sents = nlp_utils.tokenize(line)
	imojified = []

	for s in sents:
		imojified.append(imojify_sentence(s))

	return imojified


@imojify_app.get('/<src_lang>')
def api_imojify(src_lang='en'):
    sentence = request.query['sentence']

    return "Sentence: %s\n<br/>\nSource Language: %s" % (sentence, src_lang)
