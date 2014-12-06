#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2


def extract_emoji():
	"""
	Extracts emoji from the Unicode emoji page including unicode codepoints,
	image data, labels, and annotations.
	"""

	url = "http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html"
	content = urllib2.urlopen(url).read()
	soup = BeautifulSoup(content)

	rows = soup.find_all('tr')
	emoji = []

	for r in rows[1:]:
		columns = r.find_all('td')
		
		code = columns[1].a.string.strip()
		img = columns[3].img['src']
		label = columns[12].string.strip()
		annotations = [x.string for x in columns[15].find_all('a')]

		emoji.append({'code': code,
					  'image': img,
					  'label': label,
					  'annotations': annotations})

	return emoji
