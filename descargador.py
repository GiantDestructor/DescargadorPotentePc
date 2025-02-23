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
        'format': 'bestvideo+m4a/best', 
        'merge_output_format' : 'mp4',
        'paths' : {"home" : directorio},
         'postprocessors':
           [{
                'key': 'FFmpegVideoConvertor',  #asegurar video en mp4
                'preferedformat': 'mp4'
                
            }
            
            ]
    }
    return ydl_opts
    
def bienvenida():
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
    
    
    # 1
    URLS = input("--> URL ") 
    print("--> ¿Video o Audio? ")
    print("v/a")
    opcion = input("")

    if (opcion =="v"):
        print("Si quiere descargar videos de alta calidad, requiere tener descargado Ffmpeg ¿Lo tiene?\n s/n")
        ffm = input("")
    

    ydl_opts = sinFf(opcion, directorio)

    if(ffm == "s"):
        #si
        ydl_opts = conFf(opcion,directorio)
    
         
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS) 
        print("Continuar? s/n")
        continuar = input("")
        if continuar == "s":
            pass
        else:
            programa = False
    
