from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usuario=""
contraseña=""
contraseña2=""
vLista=[]

def GUARDAR():
    usuario = datos_entrada.get()
    contraseña = datos_entrada2.get()
    contraseña2 = datos_entrada3.get()
    if contraseña==contraseña2:
        print("Nombre de usuario:",usuario)
        print("Contraseña:",contraseña)
        vLista.append(usuario)
        vLista.append(contraseña)
        datos_entrada.delete(0,len(usuario))
        datos_entrada2.delete(0,len(contraseña))
        datos_entrada3.delete(0,len(contraseña2))
        messagebox.showinfo("Usuario guardado", f"Usuario {usuario} guardado correctamente")
    else: print("Las contraseñas no coinciden") 
    print("***********")

#Generar la ventana
ventana = Tk()
ventana.config(background="white")
ventana.title("DATOS USUARIO")
ventana.geometry("550x200")
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
datos_entrada2=ttk.Entry(ventana, show="*")

#Dato contraseña2
label_contraseña2=ttk.Label(ventana, text="Confirma la contraseña:")
label_contraseña2.config(background="white", border=5, font=("courier",18))
datos_entrada3=ttk.Entry(ventana, show="*")

#Botones
boton_guardar=ttk.Button(ventana, text="GUARDAR", command=GUARDAR)

boton_salir=ttk.Button(ventana, text="SALIR", command=ventana.destroy)

#Pintar en la pantalla los componentes
label_titulo.grid(row=0,column=1,pady=3,padx=3)
label_nombre.grid(row=1,column=0,pady=3,padx=3)
datos_entrada.grid(row=1,column=1,pady=3,padx=3)
label_contraseña.grid(row=2,column=0,pady=3,padx=3)
datos_entrada2.grid(row=2,column=1,pady=3,padx=3)
label_contraseña2.grid(row=3,column=0,pady=3,padx=3)
datos_entrada3.grid(row=3,column=1,pady=3,padx=3)
boton_guardar.grid(row=4,column=1,pady=5)
boton_salir.grid(row=4,column=0, pady=5)

ventana.mainloop()