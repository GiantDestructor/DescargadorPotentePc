import os
import yt_dlp
#from tkinter import*
#from tkinter import ttk

#raiz = Tk()
#raiz.title("Descarador!")
#raiz.mainloop()
#mainframe = ttk.Frame(raiz, padding="3 3 12 12")
def sinFf(opcion, directorio):
    if (opcion == "a"):
        ydl_opts = {
        'ignoreerrors': {True},
        'format': 'm4a/bestaudio/best', 'paths': {"home": directorio},
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio',
         'preferredcodec': 'm4a',
        }]
    }
    else:
         ydl_opts = {
        'ignoreerrors': {True},
        'format': 'mp4/best',
        'paths': {"home": directorio}
         }
    
    return ydl_opts

def conFf(opcion, directorio):
    ydl_opts= {
        'ignoreerrors': {True},
    }
    
def bienvenida():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print(r'  _____  ______  _____  _____          _____   _____          _____   ____  _____  ')
    print(r' |  __ \|  ____|/ ____|/ ____|   /\   |  __ \ / ____|   /\   |  __ \ / __ \|  __ \ ')
    print(r' | |  | | |__  | (___ | |       /  \  | |__) | |  __   /  \  | |  | | |  | | |__) |')
    print(r' | |  | |  __|  \___ \| |      / /\ \ |  _  /| | |_ | / /\ \ | |  | | |  | |  _  / ')
    print(r' | |__| | |____ ____) | |____ / ____ \| | \ \| |__| |/ ____ \| |__| | |__| | | \ \ ')
    print(r' |_____/|______|_____/ \_____/_/    \_\_|  \_\\_____/_/    \_\_____/ \____/|_|  \_/')
    print(r'                                                                                   ')

programa = True;
bienvenida()
directorio = input(r"Directorio: ")
while programa == True:
    
    
    URLS = input("--> URL ") 
    print("Si quiere descargar videos de alta calidad con audio, requiere tener descargado Ffmpeg ¿Lo tiene?")
    print("No es necesario Ffmpeg para el uso del programa. s/n")
    ffm = input("")

    print("--> ¿Video o Audio? ")
    print("v/a")
    opcion = input("")

    # hacer que con ffmpeg se extraiga el mejor audio y el mejor video y se junten
    if (ffm == "n"):
        ydl_opts = sinFf(opcion, directorio)
    elif(ffm == "s"):
        #si
        print("si")
    
         
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS) 
        print("Continuar? s/n")
        continuar = input("")
        if continuar == "s":
            pass
        else:
            programa = False
    
