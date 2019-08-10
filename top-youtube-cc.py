#!/usr/bin/env python

import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input('Search YouTube for: ')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url = "http://www.youtube.com/watch?v=" + search_results[0]
print(url)

from pytube import YouTube
import os

yt = YouTube(url)

print(yt.streams.filter(subtype='mp4', progressive=True).first())
yt.streams.filter(subtype='mp4', progressive=True).first().download()
#yt.streams.first().download()

#YouTube("http://www.youtube.com/watch?v=" + search_results[0]).streams.first().download('~/Downloads/')
