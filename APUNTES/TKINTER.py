from tkinter import *
from tkinter import ttk
def saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)

#Generar la ventana
ventana = Tk()
ventana.config(background="aquamarine")
ventana.title("TU_PAPI_XHULO")
ventana.geometry("300x400")
ventana.resizable(width=False,height=False)
imagen=PhotoImage(file="FOTO4.png")
fondo=Label(ventana,image=imagen).place(x=20,y=120)

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes label y button
textoLabel=StringVar()
textoLabel.set("iSHOWSPEED")
labelTexto=ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="light blue", border=5, font=("courier",30))
labelTexto.pack()

#Componente cuadro de texto
campoTexto=ttk.Entry(frm)
campoTexto.pack()

ttk.Button(frm, text="Saludo", command=saludar).pack()

ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()