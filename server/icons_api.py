#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from googleapiclient.discovery import build
from requests_oauthlib import OAuth1

# EXPECTED: developer_key, cx
def image_query(queryText, secrets):
  
  
  service = build("customsearch", "v1",
            developerKey=secrets['developer_key'])

  res = service.cse().list(
      q=queryText,
      cx=secrets['cx']
      imgSize="medium",
      searchType="image"
    ).execute()

  return res

# parse google image search query response
def parse_query(unparsed):

    links = unparsed['items']
    firstImage = links[0]['image']

    return firstImage['thumbnailLink']

# EXPECTED: public_key, secret_key
def nounproject_query(queryText, secrets):

    public_key = secrets['public_key'] 
    secret_key = secrets['secret_key'] 

    auth = OAuth1(public_key, secret_key)
    endpoint = "http://api.thenounproject.com/icons/"+queryText+"?limit_to_public_domain=1&limit=5"
    res = requests.get(endpoint, auth=auth)
    
    # return type is str
    return res.content

# google image_query, handle with care!
# response = image_query("Ossama", "you")
# print parse_query(response)

# nounproject test, also handle with care!
# response = nounproject_query("danger", "you")
# print response
