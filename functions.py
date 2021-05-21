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

    except Exception:
        return "Errore: Non è stato possibile scaricare il video correttamente"

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
        video_list = playlist.video_urls
        directory = createDirectory(directory, playlist.title)

        #Scarica i video e li inserisce nella directory
        for link in video_list:
            scaricaVideo(link, directory)

    except Exception:
        return "Errore: la playlist non è stata scaricata correttamente"

"""
@Name: createDirectory
@desc: si occupa di creare una directory nella posizione deisderata con il nome desiderata,
       se dovesse già esistere una directory con lo stesso nome aggiunge un numero al nome
@parameters: 
    path{String}: path dove creare la directory
    name {String}: nome della directory

@return: 
    finalDirectory{String}: Path completo dove è stata creata la directory
"""

def createDirectory(path, name):
    try:
        finalDirectory = 0
        #Check esistenza cartella 
        if os.path.exists(path + "/" + name):
            i = 0
            digit = 1
            while i < 1:
                if os.path.isdir(path + "/" + name + " - " + str(digit)):
                    digit = digit + 1
                else:
                    #Crea la cartella nella posizione data e con un nome non usato
                    os.makedirs(path + "/" + name + " - " + str(digit))
                    finalDirectory  = path + "/" + name + " - " + str(digit)
                    break

        else:
            os.makedirs(path + "/" + name)
            finalDirectory  = path + "/" + name

        return finalDirectory
    except Exception:
        return "Errore creazione cartella"

"""
@Name: askDirectory
@desc: si occupa di chiedere all'utente il percorso della cartella, nel caso nulla viene passato
       sceglie come percorso la directory corrente dove sta girando lo script

@return: 
    directory{String}: Path scelto dall'utente oppure path dove lo script sta girando
"""

def askDirectory():
    directory = askdirectory()
        
    if directory == '':
        directory = os.getcwd()
    return directory


#Test per le funzioni
print(scaricaPlaylist("https://youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"))