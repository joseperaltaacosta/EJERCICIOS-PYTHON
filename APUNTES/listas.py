#Listas en python
#Definicion e identificacion
vNombres = []

#Insertar un dato
vNombres.insert(0,"Bochana")
vNombres.insert(1,"Moro gritón")
vNombres.insert(2,"Alba fea")
vNombres.append("Laura chupitos")
vNombres.insert(0,"El hermano del concejal")

#Eliminar un elemento
vNombres.remove("Bochana")
vNombres.pop(1)
print("El nombre borrado es ",vNombres.pop(1))

#Ordenar una lista
#Con reverse puedo ordenar en orden inverso
vNombres.sort(reverse=True)

#Contar el número de elementos de la lista
print("Alba fea aparece ",vNombres.count("Alba fea"),"veces")
print("La lista tiene ",len(vNombres))

print(vNombres)