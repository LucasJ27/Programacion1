from FuncionesTP8 import contar_digitos, es_potencia, posicion,par,impar,maxElemento,replicar,calcular_sumatoria,pascal,combinaciones,medidas_hoja_A

#1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
numero1 = 59873
cantidad_digitos = contar_digitos(numero1)
print(f"El número {numero1} tiene {cantidad_digitos} dígitos.")

#2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
numero2 = 64
base = 2

if es_potencia(numero2, base):
    print(f"{numero2} es una potencia de {base}.")
else:
    print(f"{numero2} no es una potencia de {base}.")

#3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a.
cadena = "Pablito clavo un clavito, que clavito clavo Pablito"
palabra = "clavito"

if posicion(cadena, palabra):
    print(f'La palabra "{palabra}" se encuentra en las posiciones: {posicion(cadena, palabra)} dentro de la cadena "{cadena}".')
else:
    print(f'La palabra "{palabra}" no se encontró en la cadena "{cadena}".')

#4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
#•	1 es impar.
#•	Si un número es impar, su antecesor es par; y viceversa.

numero3 = 3
if par(numero3):
    print("El numero es par")
else:
    print("El numero es impar")

#5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.

lista_max = [4, 18, 7, 13, 2]
print(f"El mayor elemento de la lista es: {maxElemento(lista_max)}")

#6. Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

lista_replica = [1, 3, 3, 7]
print(replicar(lista_replica, 2))

#7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
#● El programa debe pedir al usuario que ingrese un número n, y un número d,
#● Luego debe calcular el valor de K(n, p) usando una función recursiva,
#● Debe imprimir el resultado de K(n, p)

n = int(input("Ingrese el valor de n: "))
d = int(input("Ingrese el valor de d: "))

print(f"El resultado de K({n}, {d}) es: {calcular_sumatoria(n, d)}")

#8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo.
# Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos.
# Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

fila = 5
columna = 2
print(f"El valor en la fila {fila} y columna {columna} del Triángulo de Pascal es: {pascal(fila, columna)}")

#9. Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados
# (permitiendo caracteres repetidos).

caracteres = ['a', 'b', 'c']
longitud = 2

print(f"Todas las combinaciones de longitud {longitud} con los caracteres {caracteres} son:")
combinaciones(caracteres, longitud)

#10. La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo).
# Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N).
# Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1),
# usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.

medida = 3 
ancho, largo = medidas_hoja_A(medida)
print(f"Las medidas de la hoja A({medida}) son: Ancho = {ancho} mm, Largo = {largo} mm")