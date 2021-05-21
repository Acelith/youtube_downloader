from tkinter.filedialog import askdirectory
from pytube import YouTube
from pytube import Playlist
from tkinter import * 
import os


"""
@Name: scaricaVideo
@desc: si occupa di scaricare il video dal link passato e lo mette nella posizione di directory
@parameters: 
    url{String}: URL del video da scaricare
    directory {String}: percorso dove inserire il video
"""
def scaricaVideo(url, directory):
    try:
        video = YouTube(url)
        video = video.streams.first()
    
        video.download(directory)

        return "Il video è stato scaricato correttamente "
    except Exception:
        return "Non è stato possibile scaricare il file, riprovare piu tardi"

"""
@Name: scaricaPlaylist
@desc: si occupa di scaricare i video presenti nella playlist inviata
@parameters: 
    url{String}: URL della playlist da scaricare
"""
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

"""
@Name: createDirectory
@desc: si occupa di creare una directory nella posizione deisderata con il nome desiderata,
       se dovesse già esistere una directory con lo stesso nome aggiunge un numero al nome
@parameters: 
    path{String}: path dove creare la directory
    name {String}: nome della directory
"""

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
            os.makedirs(path + "/" + name)
            finalDirectory  = path + "/" + name

        return finalDirectory
    except Exception:
        return "Errore"

"""
@Name: askDirectory
@desc: si occupa di chiedere all'utente il percorso della cartella, nel caso nulla viene passato
       sceglie come percorso la directory corrente dove sta girando lo script
"""

def askDirectory():
    directory = askdirectory()
        
    if directory == '':
        directory = os.getcwd()
    return directory




print(scaricaPlaylist("https://youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"))

