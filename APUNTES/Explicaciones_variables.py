
'''
nombre = "Jose"
edad = 17
mayor_o_menor_edad = False


#Entrada y salida de datos
#Salida con print()

print("Buenos dias", nombre , "tu edad es", edad)

#Entrada de datos == input()
nombre = input("Dime tu nombre:\n") #\n permite hacer un salto de linea
edad = input("Dime tu edad:\n")

print("Buenos dias", nombre , "tu edad es", edad)


#Bucle while
i=0
bandera=True
while (bandera==True):
    print("No hagas esto nunca", i)
    i=i+1
    if(i==30000):
        bandera=False
print("Terminado")
#Tabla de multiplicar
h=0
num=0
num=int(input("Dime un numero:"))
bandera=True
while  (bandera==True):
    print(num,"x",h,"=",num*h)
    h=h+1
    if(h==11):
        bandera=False
'''
#Juego contraseña
c="chacon"
c1=(input("Dime la contraseña:"))
while (c!=c1):
    c1=input("Contraseña incorrecta, introduzcala de nuevo:")
print("Contraseña correcta")