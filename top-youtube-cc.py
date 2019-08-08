#!/usr/bin/env python

import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input('Search YouTube for: ')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
print("http://www.youtube.com/watch?v=" + search_results[0])

from pytube import YouTube

yt = YouTube("http://www.youtube.com/watch?v=" + search_results[0])
yt = yt.get('mp4', '720p')
yt.download('./')
