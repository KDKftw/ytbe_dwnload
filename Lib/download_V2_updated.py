
##playlist link
link = ("https://www.youtube.com/playlist?list=PLBnvQD5J8X_W2VTJm4MllLrmeYCtU5HI5")



from youtube_dl import YoutubeDL
# or for yt_dlp:
# from yt_dlp import YoutubeDL
with YoutubeDL() as ydl:
    ydl.download(["https://www.youtube.com/watch?v=Q7fDfGSP_WM&list=PLBnvQD5J8X_W2VTJm4MllLrmeYCtU5HI5&index=1"])