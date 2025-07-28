import os
import yt_dlp
#from tkinter import*
#from tkinter import ttk

#raiz = Tk()
#raiz.title("Descarador!")
#raiz.mainloop()
#mainframe = ttk.Frame(raiz, padding="3 3 12 12")
def descargar_audio(directorio):
        nombre_del_artista = ""
        nombre_del_album = ""
        albumSN = input("¿Quiere descargar un album? \n (s/n)")
        if (albumSN == "s"):
            nombre_del_album= input("---> Nombre del Album ")
            nombre_del_artista= input("---> Nombre del Artista ")
        else: pass
        ydl_opts = {
        'ignoreerrors': {True},
        'format': 'm4a/bestaudio/best', 'paths': {"home": directorio},
        'postprocessors': 
        [{  
            'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3'
        },
        
        {
            'key': 'FFmpegMetadata',
        
        },
        {
            'key': 'EmbedThumbnail'
        }
        ],
        'postprocessor_args': [  
            '-metadata', f'artist={nombre_del_artista}',
            '-metadata', f'album={nombre_del_album}',
        ],
        
        "writethumbnail" : True
        
    }
        return ydl_opts
def descargar_video_sinFfmpeg(directorio):

    ydl_opts = {
    'ignoreerrors': {True},
    'format': 'mp4/best',
    'paths': {"home": directorio}
         }
    
    return ydl_opts

def conFf(directorio):
    ydl_opts= {
        'ignoreerrors': True,
        'format': 'bv*[vcodec^=avc1][height<=1080]+m4a/best', #una forma de descargar solo la versión de 1080 o mejor pero no en Av01 o Av1 y descargar el mejor audio y convertirlo en wav y luego los juntamos.
        'merge_output_format' : 'mp4',
        'paths' : {"home" : directorio},
         'postprocessors':
           [                
            {                
                'key': 'FFmpegVideoConvertor',  #asegurar video en mp4
                'preferedformat': 'mp4'
            }
            
            ],
            
    
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
    opcion = input("--> ¿Video o Audio? \n (v/a) ")

    if(opcion == "a"):
        ydl_opts = descargar_audio(directorio)
    # que pasa cuando queremos video
    elif (opcion =="v"):
        ffm = input("Si quiere descargar videos de alta calidad, requiere tener descargado Ffmpeg ¿Lo tiene?\n s/n")
        if(ffm == "s"):
         #si
            ydl_opts = conFf(directorio)
        else:
            ydl_opts = descargar_video_sinFfmpeg(directorio)

    # Que pasa cuando queremos audio
    

   
    
         
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(URLS) 
        print("Continuar? s/n")
        continuar = input("")
        if continuar == "s":
            pass
        else:
            programa = False
