#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apiclient.discovery import build


devkey = None

with open('google_translate.key', 'r') as infile:
	devkey = infile.read().strip()


service = build('translate', 'v2', developerKey=devkey)

def translate_to_english(sent):
    return service.translations().list(target='en', q=[sent]).execute()['translations'][0]['translatedText']
