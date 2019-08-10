#!/usr/bin/env python

import urllib.request
import urllib.parse
import re

# Search YouTube for a video

query_string = urllib.parse.urlencode({"search_query" : input('Search YouTube for: ')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]
print(url)

from pytube import YouTube

# Grab information regarding the video and download the progressive stream, mp4 version

yt = YouTube(url)

print(yt.streams.filter(subtype='mp4', progressive=True).first())
print(yt.title)
yt.streams.filter(subtype='mp4', progressive=True).first().download()
