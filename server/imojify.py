#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import json

from bottle import request, Bottle
import nlp_utils
import emoji_dict
from icons_api import nounproject_query


re.LOCALE
re.UNICODE

punct_re = re.compile("^\W+$")
lutable = emoji_dict.gen_emoji_lookup_table('data/emoji_dump.json')
np_keys = None
imojify_app = Bottle()


with open('nounproject.key', 'r') as infile:
	np_keys = json.loads(infile.read())


def imojify_sentence(sent, src_lang="en"):
	imojified = []

	for s in sent:
		if s in lutable:
			imojified.append(lutable[s][0]['image'])
		elif s == '?':
			imojified.append(lutable['question'][0]['image'])
		elif s == '!':
			imojified.append(lutable['exclamation'][0]['image'])
		elif punct_re.match(s) is None:
			link = nounproject_query(s, np_keys)
			if link is not None:
				imojified.append(link)
			else:
				# imojified.append('link!')
				pass

	return imojified


def imojify_input(line, src_lang="en"):
	line = line.lower()
	sents = nlp_utils.tokenize(line)
	imojified = []

	for s in sents:
		imojified.append(imojify_sentence(nlp_utils.stem_tokens(s, src_lang),
						 src_lang))
	return imojified


@imojify_app.get('/<src_lang>')
def api_imojify(src_lang='en'):
    sentence = request.query['sentence']

    return "Sentence: %s\n<br/>\nSource Language: %s" % (sentence, src_lang)
