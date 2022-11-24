from tkinter import *
from tkinter import ttk

def GUARDAR():
    texto = datos_entrada.get()
    print("Nombre:",texto)
    texto2 = datos_entrada2.get()
    print("Contraseña:",texto2)

#Generar la ventana
ventana = Tk()
ventana.config(background="white")
ventana.title("DATOS USUARIO")
ventana.geometry("500x200")
ventana.resizable(False,False)

#Componentes label y button
label_titulo=ttk.Label(ventana, text="DATOS")
label_titulo.config(background="white", border=5, font=("courier",18))

#Dato nombre
label_nombre=ttk.Label(ventana, text="Nombre de usuario:")
label_nombre.config(background="white", border=5, font=("courier",18))
datos_entrada=ttk.Entry(ventana)

#Dato contraseña
label_contraseña=ttk.Label(ventana, text="Contraseña:")
label_contraseña.config(background="white", border=5, font=("courier",18))
datos_entrada2=ttk.Entry(ventana)

#Dato contraseña2
label_contraseña2=ttk.Label(ventana, text="Confirma la contraseña:")
label_contraseña2.config(background="white", border=5, font=("courier",18))
datos_entrada3=ttk.Entry(ventana)

#Botones
boton_guardar=ttk.Button(ventana, text="GUARDAR", command=GUARDAR)

boton_salir=ttk.Button(ventana, text="SALIR", command=ventana.destroy)

#Pintar en la pantalla los componentes
label_titulo.grid(row=0,column=1)
label_nombre.grid(row=1,column=0)
datos_entrada.grid(row=1,column=1)
label_contraseña.grid(row=2,column=0)
datos_entrada2.grid(row=2,column=1)
label_contraseña2.grid(row=3,column=0)
datos_entrada3.grid(row=3,column=1)
boton_guardar.grid(row=4,column=0)
boton_salir.grid(row=4,column=1)

ventana.mainloop()