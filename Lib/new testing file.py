


link = ("https://www.youtube.com/watch?v=GWMSvX4Q218&list=PLBnvQD5J8X_X0Sz_SXaF6MLFZrxCtRmeD&t=0s")
from pytube import YouTube
import os
path = r"C:\Users\KDK\Desktop\YTBE DOWNLOAD"
def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

downloadYouTube(link, path)