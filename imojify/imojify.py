#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, get, request


@get('/imojify')
def api_imogify():
    sentence = request.query['sentence']
    src_lang = request.query['src_lang']

    return "Sentence: %s\n<br/>\nSource Language: %s" % (sentence, src_lang)


run(host='0.0.0.0', port=8080, debug=True)
