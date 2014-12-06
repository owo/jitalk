#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def gen_emoji_lookup_table(dump_path):
	emoji_table = {}
	emoji = None
	annot_blacklist = ['fitz-optional', 'face', 'human', 'open', 'closed',
					   'fantasy', 'fairy_tale', 'gesture', 'body',
					   'emotion', 'flag', 'nature', 'island', 'islands']

	with open(dump_path, 'r') as infile:
		emoji = json.loads(infile.read())

	for e in emoji:
		keywords = []
		for a in e['annotations']:
			if a not in annot_blacklist:
				keywords.append(a.replace(u'_', u' '))
		for k in keywords:
			if k in emoji_table:
				emoji_table[k].append(e)
			else:
				emoji_table[k] = [e]

	return emoji_table
