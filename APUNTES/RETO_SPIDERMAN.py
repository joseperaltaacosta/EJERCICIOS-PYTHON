#Hallar el camino más rápido para las emergencias de spiderman
Punto_spiderman=0
Camino1=0
Camino2=0

Camino1=(int)(input("A que distancia se encuentra el primer problema"))
Camino2=(int)(input("A que distancia se encuentra el segundo problema"))

if ((Camino1 > 0) and (Camino2 > 0)):
    if (Camino1<Camino2):
        print("El camino más eficaz es de: ", Camino2,"km")
    else:
        print("El camino más eficaz es de: ", Camino1, "km")
if (Camino1 and Camino2 <0):
    if (Camino1<Camino2):
        print("El camino más eficaz es de: ", Camino2,"km")
    else:
        print("El camino más eficaz es de: ", Camino1, "km")
if (Camino1>0) and (Camino2<0):
    if (Camino1 > abs(Camino2)):
        print("El camino más eficaz es de: ", abs(Camino2*2)+Camino1)
    else:
        print("El camino más eficaz es de: ", (Camino1*2)+abs(Camino2))