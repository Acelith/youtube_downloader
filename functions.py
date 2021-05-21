from tkinter.filedialog import askdirectory
from pytube import YouTube
from pytube import Playlist
from tkinter import * 
import os
def scaricaVideo(url, directory):
    try:
        video = YouTube(url)
        video = video.streams.first()
    
        video.download(directory)

        return "Il video è stato scaricato correttamente "
    except Exception:
        return "Non è stato possibile scaricare il file, riprovare piu tardi"


def scaricaPlaylist(url):
    try: 
        directory = askDirectory()
        playlist = Playlist(url)
        urls = playlist.video_urls
        directory = createDirectory(directory, playlist.title)
        for link in urls:
            scaricaVideo(link, directory)

        return "La playlist è stata scaricata correttamente nella cartella: " + directory
    except Exception:
        return "Non è stato possibile scaricare la playlist, riprovare piu tardi"

def createDirectory(path, name):
    try:
        finalDirectory = 0
        if os.path.exists(path + "/" + name):
            i = 0
            digit = 1
            while i < 1:
                if os.path.isdir(path + "/" + name + " - " + str(digit)):
                    digit = digit + 1
                else:
                    os.makedirs(path + "/" + name + " - " + str(digit))
                    finalDirectory  = path + "/" + name + " - " + str(digit)
                    break

        else:
            #os.mkdir(path)
            os.makedirs(path + "/" + name)
            finalDirectory  = path + "/" + name

        return finalDirectory
    except Exception:
        return "Errore"


def askDirectory():
    directory = askdirectory()
        
    if directory == '':
        directory = os.getcwd()
    return directory

print(scaricaPlaylist("https://youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"))

