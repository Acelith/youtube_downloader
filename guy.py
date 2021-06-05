import PySimpleGUI as sg
from tkinter.filedialog import askdirectory
from pytube import YouTube
from pytube import Playlist
import tkinter as tk
import os


"""
@Name: scaricaMedia
@desc: Si occupa di controllre se l'url appartiene ad una playlist oppure un video e 
       di conseguenza utilizza la funzione necessaria

"""

def scaricaMedia():
    directory = path_field.get()
    url = url_field.get()
    
    if url == "":
        tk.messagebox.showerror(title="Link", message="Nessun link inserito. ")
    elif "playlist" in url:
        tk.messagebox.showinfo(title="Download in corso", message="Download in corso, attendere")
        scaricaPlaylist(url,directory)
    else:
        tk.messagebox.showinfo(title="Download in corso", message="Download in corso, attendere")
        scaricaVideo(url,directory)


"""
@Name: scaricaVideo
@desc: si occupa di scaricare il video dal link passato e lo mette nella posizione di directory
@parameters: 
    url{String}: URL del video da scaricare
    directory {String}: percorso dove inserire il video

@return {int}
"""
def scaricaVideo(url, directory):
    try:
        video = YouTube(url)
        video = video.streams.first()
        video.download(directory)

        return 1
    except Exception:
        tk.messagebox.showerror(title="Errore scaricamento video", message="Errore nello scaricamento del video. ")
        return -1


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

        for link in video_list:
            res = scaricaVideo(link, directory)
            if res == -1:
                break
            
        tk.messagebox.showinfo(title="Download completato", message="Download playlist conclus :)")
        return 1
    except Exception as e:
        print(e)
        tk.messagebox.showerror(title="Errore playlist", message="Errore nello scaricamento della playlist. ")
        return -1


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
        tk.messagebox.showerror(title="Errore cartella", message="Impossibile creare la cartella di destinazione.")

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


#-------------------------------------------Guy---------------------------------------------------------#
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

path_button = tk.Button(text="...",  width=4,height=1,command=askDirectory)
path_button.pack()
path_button.place(x=445, y=117)

download_btn = tk.Button(text="Avvia download",  width=10,height=4,command=scaricaMedia)
download_btn.pack()



#opzioni supplementari
finestra.resizable(False, False)
finestra.geometry("500x300")


finestra.mainloop()
