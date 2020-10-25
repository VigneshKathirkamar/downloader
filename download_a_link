#script to download video from youtube

import youtube_dl

link = str(input("Enter link:"))

ydl_opts = {'format': 'best'}
print("downloading this...", link) 
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print('Task Completed!') 
