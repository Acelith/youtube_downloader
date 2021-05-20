from tkinter.filedialog import askdirectory
from pytube import YouTube
from tkinter import * 
import os
def scaricaVideo(url):
    try:
        video = YouTube(url)
        video = video.streams.first()
        directory = askdirectory()
        
        if directory == '':
            directory = os.getcwd()

        video.download(directory)

        return "Il video è stato scaricato correttamente "
    except Exception as e:
        return "Non è stato possibile scaricare il file, riprovare piu tardi"
