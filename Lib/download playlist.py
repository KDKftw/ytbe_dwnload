import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse
import pandas as pd
from openpyxl import load_workbook

#extract playlist id from url
url = 'https://www.youtube.com/watch?v=GWMSvX4Q218&list=PLBnvQD5J8X_X0Sz_SXaF6MLFZrxCtRmeD'
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]

print(f'get all playlist items links from {playlist_id}')
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyAGVSAYIvxdbyUKPTpc2ICukbMJD5Y3S4s")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 500
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

print(f"total: {len(playlist_items)}")
link=([
    f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
    for t in playlist_items
])
print(link)

path = executable_path=r"C:\Users\KDK\Desktop\ytbe_dnwload"

y=2
x=0
while y < 442:  ## length playlistu (440) + variable 2  ##2 could be done better but for now I need to insert length of playlist + 2
    df = pd.read_excel(r"C:\Users\KDK\Desktop\YTBE DOWNLOAD\links_liked_videos_V2.xlsx")    ##toedit
    wb = load_workbook(r"C:\Users\KDK\Desktop\YTBE DOWNLOAD\links_liked_videos_V2.xlsx")     ##toedit
    ws = wb.worksheets[0]

    ws.cell(row=y, column=3).value = link[x]
    x+=1
    y += 1
    wb.save(r"C:\Users\KDK\Desktop\YTBE DOWNLOAD\links_liked_videos_V2.xlsx")        ##toedit
    print(y)


