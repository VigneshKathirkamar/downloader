#Script to download videos from YouTube

from __future__ import unicode_literals
import youtube_dl

path = str(input("Enter path of the text file containing youtube links: "))

links = open(path,'r') 
linkset = list(set(links.readlines()))

ydl_opts = {'format': 'best',}

for link in linkset:
    print("downloading this...", link) 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

print('Task Complete!') 
