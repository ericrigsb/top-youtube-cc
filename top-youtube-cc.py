#!/usr/bin/env python

import urllib.request
import urllib.parse
import re
from pytube import YouTube

# Search YouTube for videos filtered by CC license and view count

query_string = urllib.parse.urlencode({"search_query" : input('Search YouTube for: ')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string + "&sp=CAMSAjAB")
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

# Remove duplicates and limit to first three results

search_results = list(dict.fromkeys(search_results))[:3]

# Grab information regarding the videos and download the progressive stream, mp4 versions

for result in search_results:
    url = "http://www.youtube.com/watch?v=" + result
    yt = YouTube(url)
    print(yt.streams.filter(subtype='mp4', progressive=True).first())
    print(yt.title)
    print(yt.views)
    # yt.streams.filter(subtype='mp4', progressive=True).first().download()
