from pytube import YouTube
from sys import argv
import getpass
username = getpass.getuser()
link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
direc = fr"C:\Users\{username}\Videos\YT-Downloader"
yd.download(direc)
print(f"You just downloaded:\nTitle: {yt.title}\nViews: {'{:,}'.format(yt.views)}\nYou can find it on - {direc}")

