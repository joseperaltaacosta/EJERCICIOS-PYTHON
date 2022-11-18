from tkinter import *
from tkinter import ttk
#Generar la ventana
ventana = Tk()
ventana.config(background="aquamarine")
ventana.title("TU_PAPI_XHULO")
ventana.geometry("300x500")
ventana.resizable(width=False,height=False)
imagen=PhotoImage(file=("índice.png"))
fondo=Label(ventana,image=imagen).place(x=10,y=20)

#Genera el lienzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes label y button
labelTexto=ttk.Label(frm, text="hello papi :)")
labelTexto.config(background="light blue", border=5, font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()