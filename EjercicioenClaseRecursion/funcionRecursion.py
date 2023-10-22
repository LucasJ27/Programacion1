'''

Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma 
probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 
minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. 
La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero 
quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
La función debe devolver el tiempo que tarda la rata en salir de la jaula.

'''

def jaula():
    contador = 0
    while True:
        camino = int(input("Elija el camino para la rata (ingrese 0 para salir): \n1- Camino 1 \n2- Camino 2 \n3- Camino 3 "))
        if camino == 0:
            break  
        elif camino == 1:
            contador += 3
        elif camino == 2:
            contador += 5
        elif camino == 3:
            contador += 7
            break  

    return f"La rata se demoró {contador} minutos en salir de la jaula"
        

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))