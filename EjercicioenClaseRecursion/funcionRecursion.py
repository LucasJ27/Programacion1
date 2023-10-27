import random
'''

Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma 
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. 
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero 
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
La función debe devolver el tiempo que tarda la rata en salir de la jaula.

'''

def jaula(contador = 0):
    camino = random.randint(1, 3)
    if camino == 1:
        print("La rata tomó el camino 1 y luego de 3 minutos volvió al mismo lugar donde empezó.")
        contador += 3
    elif camino == 2:
        print("La rata tomó el camino 2 y luego de 5 minutos volvió al mismo lugar donde empezó.")
        contador += 5
    elif camino == 3:
        contador += 7
        return print(f"La rata tomó el camino 3 y luego de 7 minutos salió de la jaula. Se tardo {contador} minutos en salir de la jaula.")
    return jaula(contador)
       
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))