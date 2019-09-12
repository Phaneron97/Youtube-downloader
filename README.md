# Youtube-downloader

This simple program made in python downloads videos from a custom playlist or channel from youtube. 

For this program to work you will need the following:

- A folder to place the nessecary files in, here will also be the videos be downloaded. 
- 2 .txt files named 'channel_list' and 'downloaded'
- youtube-dl.exe which can be downloaded from [here](https://ytdl-org.github.io/youtube-dl/download.html)
- ffmpeg.exe which can be downloaded from [here](http://ffmpeg.org/download.html?aemtn=tg-on)
- main.py found in the repo

# How it works:

Explaining the arguments from top to bottom:

1. main.py will run the process youtube-dl.exe for the basic process of downloading urls but with some arguments this program will do more then that.
2. All downloaded videos from found list will be added to the archive 'downloaded.txt' so those won't be downloaded twice.
3. Ignores errors videos might give (Skip unavailable/copyrighted/deleted videos)
4. Add information about the video (channelname, uploaddate, title, duration, etc)
5. Find channels/lists to download from 'channel_list.txt'

That's it! Hope you enjoy and feel free to download the repo and edit the files according to your needs.
