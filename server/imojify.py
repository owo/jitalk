#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import request, Bottle

imojify_app = Bottle()

@imojify_app.get('/<src_lang>')
def api_imojify(src_lang='en'):
    sentence = request.query['sentence']

    return "Sentence: %s\n<br/>\nSource Language: %s" % (sentence, src_lang)
