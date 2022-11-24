from tkinter import *
from tkinter import ttk
from pytube import YouTube
def DESCARGAR():
    url=datos_entrada.get()
    youtube=YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion=youtube.streams.get_audio_only()
    cancion.download()

#Generar la ventana
ventana = Tk()
ventana.config(background="aquamarine")
ventana.title("DESCARGADOR DE CANCIONES")
ventana.geometry("300x450")
ventana.resizable(False,False)
imagen=PhotoImage(file="music.png")
fondo=Label(ventana,image=imagen).place(x=0,y=120)

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes label y button
label_titulo=ttk.Label(ventana, text="Introduce la url del video:")
label_titulo.config(background="light blue", border=5, font=("courier",13))
label_titulo.place(x=10,y=0)

#Componente cuadro de texto
datos_entrada=ttk.Entry(ventana)
datos_entrada.place(x=60,y=30)

boton_descargar=ttk.Button(ventana, text="DESCARGAR", command=DESCARGAR)
boton_descargar.place(x=100, y=60)

boton_salir=ttk.Button(ventana, text="SALIR", command=ventana.destroy)
boton_salir.place(x=105, y=90)

ventana.mainloop()