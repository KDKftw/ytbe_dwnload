import pytube
from pytube import YouTube
path = executable_path=r"C:\Users\KDK\Desktop\ytbe_dnwload"
import pandas as pd
from openpyxl import load_workbook





YouTube('https://www.youtube.com/watch?v=UncaiC2XDbQ').streams[0].download()