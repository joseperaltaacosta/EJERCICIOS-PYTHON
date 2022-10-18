vNom=[]
vTlf=[]

#Creamos el menu de la agenda
'''
1-. Insertar contacto
2-. Borrar contacto
3-. Buscar contacto
4-. Ver todos los contactos
5-. Salir
'''
def pintaMenu():
    opc=0
    while (opc < 1 or opc > 5):
        print("1-. Insertar contacto")
        print("2-. Borrar contacto")
        print("3-. Buscar contacto")
        print("4-. Ver todos los contactos")
        print("5-. Salir")
        try:
            opc=int(input("Dime que quieres hacer:"))
        except:
            print("Las opciones son de la 1 a la 5")

    return opc

opc = pintaMenu()
while (opc!=5):
    nom="Juan"
    opc=pintaMenu()