import pytube
from pytube import YouTube

link = ("https://www.youtube.com/watch?v=GWMSvX4Q218&list=PLBnvQD5J8X_X0Sz_SXaF6MLFZrxCtRmeD&t=0s")
#yt=YouTube(link)
#t=yt.streams.filter(only_audio=True).all()
t= pytube.YouTube(link).streams.filter(only_audio=True).all()
t[0].download(r"C:\Users\KDK\Desktop\YTBE DOWNLOAD")
