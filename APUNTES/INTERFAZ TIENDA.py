from tkinter import *
from tkinter import ttk
from tkinter import messagebox
usuario=""
contraseña=""
vLista=[]
#Generar la ventana
ventana = Tk()
ventana.config(background="white")
ventana.title("DATOS USUARIO")
ventana.geometry("550x300")
ventana.resizable(False,False)
#Componentes label y button
label_titulo=ttk.Label(ventana, text="DATOS")
label_titulo.config(background="white", border=5, font=("courier",18))
#Dato nombre
label_carnes=ttk.Label(ventana, text="Carnes:")
label_carnes.config(background="white", border=5, font=("courier",18))
datos_desplegable_carnes=ttk.Combobox(ventana,state="readonly",values=["Ternera","Pechuga"])
datos_desplegable_carnes.set("Determine la carne")
#Dato contraseña
label_verduras=ttk.Label(ventana, text="Verduras:")
label_verduras.config(background="white", border=5, font=("courier",18))
datos_desplegable_verduras=ttk.Combobox(ventana,state="readonly",values=["Colifror","Esparrago"])
datos_desplegable_verduras.set("Determine la verdura")
#Botones
boton_guardar=ttk.Button(ventana, text="GUARDAR", command=ventana.destroy)
boton_salir=ttk.Button(ventana, text="SALIR", command=ventana.destroy)
#Pintar en la pantalla los componentes
label_titulo.grid(row=0,column=1,pady=3,padx=3)
label_carnes.grid(row=1,column=0,pady=3,padx=3)
datos_desplegable_carnes.grid(row=1,column=1,pady=5)
label_verduras.grid(row=2,column=0,pady=3,padx=3)
datos_desplegable_verduras.grid(row=2,column=1,pady=3,padx=3)
boton_guardar.grid(row=5,column=1,pady=5)
boton_salir.grid(row=5,column=0, pady=5)

ventana.mainloop()