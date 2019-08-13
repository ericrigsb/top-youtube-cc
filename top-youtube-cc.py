#!/usr/bin/env python

import urllib.request
import urllib.parse
import re
from pytube import YouTube
import os
import json

# Search YouTube for videos filtered by CC license and view count

query_string = urllib.parse.urlencode({"search_query" : input('Search YouTube for: ')})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string + "&sp=CAMSAjAB")
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

# Remove duplicates and limit to first three results

search_results = list(dict.fromkeys(search_results))[:3]

# Download the progressive stream, mp4 versions and write inforamtion about the videos to downloadInfo.json

json_file = "downloadInfo.json"
json_arr = []

if os.path.isfile(json_file):
    os.remove(json_file)

for result in search_results:
    url = "http://www.youtube.com/watch?v=" + result
    yt = YouTube(url)
    yt.streams.filter(subtype='mp4', progressive=True).first().download(filename=result)
    downloadInfo = {
        "Title": yt.title,
        "Location": result + ".mp4",
        "Views": yt.views,
        "Descr": yt.description
    }
    json_arr.append(downloadInfo)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_arr, f, ensure_ascii = False, indent = 4)
