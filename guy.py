import PySimpleGUI as sg
from tkinter.filedialog import askdirectory
from pytube import YouTube
from pytube import Playlist
import tkinter as tk
import os

playlist_lengt = 0
"""
@Name: scaricaVideo
@desc: si occupa di scaricare il video dal link passato e lo mette nella posizione di directory
@parameters: 
    url{String}: URL del video da scaricare
    directory {String}: percorso dove inserire il video
"""
def scaricaVideo(url, directory):
    global size
    try:
        video = YouTube(url)
        video = video.streams.first()
        #video.register_on_complete_callback(window['PROGRESS'].update('Ho finito di scaricare ora puoi guardare il video ' + video.title()))
        size = video.filesize
        video.download(directory)

        return 1
    except Exception:
        return 2
"""
@Name: scaricaPlaylist
@desc: si occupa di scaricare i video presenti nella playlist inviata
@parameters:
    url{String}: URL della playlist da scaricare

"""

def scaricaPlaylist(url, directory):
    try:
        playlist = Playlist(url)
        video_list = playlist.video_urls
        directory = createDirectory(directory, playlist.title)

        #Scarica i video e li inserisce nella directory
        prog = 0

        playlist_lengt = "0 / " + str(playlist.length)
        for link in video_list:
            how_many.insert(0, playlist_lengt)
            res = scaricaVideo(link, directory)
            if res == 2:
                prog = playlist.length
                break
            else:
                playlist_lengt = prog + " / " + playlist.length
                prog = prog + res

           
       
    except Exception as e:
        print(e)
        return "Errore: la playlist non è stata scaricata correttamente"


"""
@Name: scaricaMedia
@desc: Si occupa di controllre se l'url appartiene ad una playlist oppure un video e 
       di conseguenza utilizza la funzione necessaria

"""

def scaricaMedia():
    directory = path_field.get()
    url = url_field.get()

    if "playlist" in url:
       res = scaricaPlaylist(url,directory)
    else:
        scaricaVideo(url,directory)





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
    path_field.insert(0, directory) 


#--------------------------------------------Design Guy------------------------------------------------------------------------------------------------#
# gui
finestra = tk.Tk()
#widget

lbl_download_video = tk.Label(text="Inserisci url da scaricare", width=50, height=3)
lbl_download_video.pack()


url_field = tk.Entry(finestra,width=50)
url_field.pack()

lbl_path_video = tk.Label(text="path dove scaricare video", width=50, height=3)
lbl_path_video.pack()

path_field = tk.Entry(finestra,width=50)
path_field.pack()

path_button = tk.Button(text="...",  width=2,height=1,command=askDirectory)
path_button.pack()
path_button.place(x=445, y=117)

download_btn = tk.Button(text="Avvia download",  width=10,height=4,command=scaricaMedia)
download_btn.pack()

how_many = tk.Label(text=" ", width=50, height=3)
how_many.pack()


#opzioni supplementari
finestra.resizable(False, False)
finestra.geometry("500x300")


finestra.mainloop()
