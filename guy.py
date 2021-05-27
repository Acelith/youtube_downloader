import PySimpleGUI as sg
from tkinter.filedialog import askdirectory
from pytube import YouTube
from pytube import Playlist
from tkinter import * 
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
    try:
        video = YouTube(url)
        video = video.streams.first()
        #video.register_on_complete_callback(window['PROGRESS'].update('Ho finito di scaricare ora puoi guardare il video ' + video.title()))

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
        #directory = askDirectory()
        playlist = Playlist(url)
        video_list = playlist.video_urls
        directory = createDirectory(directory, playlist.title)

        #Scarica i video e li inserisce nella directory
        prog = 0
        playlist_lengt = playlist.length
        for link in video_list:
            res = scaricaVideo(link, directory)
            if res == 2:
                prog = playlist.length
                break
            else:
                prog = prog + res

            window['PROGRESS'].update_bar(prog)

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


# Define the window's contents
layout = [[sg.Text("Url")],
          [sg.Input(key='-URL-')], [sg.Image(size=(100,100),filename='logo.gif')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text("Percorso di download"), sg.Input(key='-PERCORSO-'), sg.Button('...') ],
          [sg.Button('Scarica'), sg.Button('Esci'), sg.ProgressBar(max_value=playlist_lengt,size=(40,20), key='PROGRESS')]]
#[[sg.Radio('Video', 'choose', key='c_video', default=True) , sg.Radio('Playlist', 'choose' , key='c_playlist')]],

# Create the window
window = sg.Window('Scarica video e playlist da youtube', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    url = values['-URL-']
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    elif event == '...':
        cartella = askDirectory()
        window['-PERCORSO-'].update(cartella)
    #Scarica media
    elif event == 'Scarica':
        try:
            if "playlist" in url:
                scaricaPlaylist(url, values['-PERCORSO-'])
                window['-OUTPUT-'].update('la tua playlist sta venendo scaricata, per favore aspetta')
            else:
                scaricaVideo(url, values['-PERCORSO-'])
            window['-OUTPUT-'].update('il tuo video sta venendo scaricato, per favore aspetta')
        except Exception:
            window['-OUTPUT-'].update('Non funziona niente cribbio')
    
   

# Finish up by removing from the screen
window.close()

#TODO Controllare i radio button se selezionata playlist oppure video, ultima cosa in cantiere, il progetto e da finire
