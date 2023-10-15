
import random as rnd

#1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

numbers = []
while True:
    number = int(input("Ingrese los numeros que desea guardar.(Ingrese 0 para finalizar) "))
    if number == 0:
        break
    numbers.append(number)
print(numbers)

#2. A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
number2 = int(input("Ingrese el numero a eliminar: "))
if number2 in numbers:
        numbers.remove(number2)
else:
     print("No fue posible eliminar el numero")

#3.	Imprimir la sumatoria de todos los números de la lista.
print(numbers)
print(f"La sumatoria de los numeros en la lista es: {sum(numbers)}")

#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
number3 = int(input("Ingrese un nuevo numero: "))
numbers2 = []
for elemento in numbers:
     if elemento < number3:
          numbers2.append(elemento)
for num in numbers2:
     print(num)
   

#5. Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
#Por ejemplo, si la lista original es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]

occurrences = {}
for number in numbers:
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1

new_tupla = list(occurrences.items())

print(new_tupla)

'''
6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar 'x'.
A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar 'x'.
a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
'''

primary_level = []
secondary_level = []
while True:
    name_primary = input("Ingrese el nombre del alumno de nivel primario: ")
    if name_primary == 'x':
        break
    if name_primary not in primary_level:
        primary_level.append(name_primary)
while True:
    name_secondary = input("Ingrese el nombre del alumno de nivel secundario: ")
    if name_secondary == 'x':
        break
    if name_secondary not in secondary_level:
        secondary_level.append(name_secondary)

repeated_names = set(primary_level) & set(secondary_level)
not_repeated = set(primary_level) - set(secondary_level)

print(f"Los nombres de los alumnos de nivel primario son: {primary_level}")
print(f"Los nombres de los alumnos de nivel secundario son: {secondary_level}")
print(f"Los nombres que se repiten entre nivel primario y secundario son: {list(repeated_names)}")
print(f"Los nombres de nivel primario que no se repiten en el nivel secundario son: {list(not_repeated)}")    

'''
7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings.
Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
'r':5
'%':3
'a':8
'9':1
'''

ocurrencias_caracteres = {}

for element in range(50):
    inputString = input("Ingrese un string: ")
    
    for caracter in inputString:
        if caracter in ocurrencias_caracteres:
            ocurrencias_caracteres[caracter] += 1
        else:
            ocurrencias_caracteres[caracter] = 1

for caracter, cantidad in ocurrencias_caracteres.items():
    print(f"'{caracter}': {cantidad}")


''' 
8. Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
Escriba un programa que:
o	Lea el cuadro de goles en un arreglo de dos dimensiones.
o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
o	Determine la cantidad de puntos obtenidos por cada equipo.

''' 

goles = [[0,4,2,1],
         [5,0,3,2],
         [0,2,0,1],
         [1,0,2,0]
        ]

# PROCEDIMIENTO
n = len(goles)
m = len(goles[0])

# Calcular los triunfos
triunfos = [[0 for elemnto in range(m)] for element in range(n)]
ttriunfos = [0] * n

for i in range(n):
    for j in range(m):
        if goles[i][j] > goles[j][i]:
            triunfos[i][j] = 1
            triunfos[j][i] = 0

# Calcular total de triunfos
for i in range(n):
    ttriunfos[i] = sum(triunfos[i])

# Calcular empates
empates = [[0 for _ in range(m)] for _ in range(n)]
tempates = [0] * n

for i in range(n):
    for j in range(m):
        if goles[i][j] == goles[j][i] and i != j:
            empates[i][j] = 1
            empates[j][i] = 1

# Calcular total de empates
for i in range(n):
    tempates[i] = sum(empates[i])

# Derrotas
derrotas = [(n - 1) - t + e for t, e in zip(ttriunfos, tempates)]

print("Triunfos por equipo:")
for i in range(n):
    print(f"Equipo {i + 1}: {ttriunfos[i]} triunfos")

print("\nEmpates por equipo:")
for i in range(n):
    print(f"Equipo {i + 1}: {tempates[i]} empates")

print("\nDerrotas por equipo:")
for i in range(n):
    print(f"Equipo {i + 1}: {derrotas[i]} derrotas")

'''
9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices.
El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.
'''

def tablero_parejas(n):
    fichas_unicas = (n * n) // 2
    tablero = [[0] * n for _ in range(n)]

    i = 1
    while i <= fichas_unicas:
        f1, c1 = rnd.randint(0, n - 1), rnd.randint(0, n - 1)
        while tablero[f1][c1] != 0:
            f1, c1 = rnd.randint(0, n - 1), rnd.randint(0, n - 1)
        tablero[f1][c1] = i

        f2, c2 = rnd.randint(0, n - 1), rnd.randint(0, n - 1)
        while tablero[f2][c2] != 0:
            f2, c2 = rnd.randint(0, n - 1), rnd.randint(0, n - 1)
        tablero[f2][c2] = i

        i += 1
    return tablero

# PROGRAMA
# INGRESO
n = 4

# PROCEDIMIENTO
tablero = tablero_parejas(n)
descubiertas = [[0] * n for _ in range(n)]
equivocado = 0
encontrado = 0

while equivocado < 3 and encontrado < (n * n):
    print('Estado del juego:')
    for fila in descubiertas:
        print(fila)

    f1 = int(input('Fila ficha 1: '))
    c1 = int(input('Columna ficha 1: '))
    while descubiertas[f1][c1] != 0:
        f1 = int(input('Fila ficha 1: '))
        c1 = int(input('Columna ficha 1: '))

    f2 = int(input('Fila ficha 2: '))
    c2 = int(input('Columna ficha 2: '))
    while descubiertas[f2][c2] != 0:
        f2 = int(input('Fila ficha 2: '))
        c2 = int(input('Columna ficha 2: '))

    ficha1, ficha2 = tablero[f1][c1], tablero[f2][c2]

    if ficha1 == ficha2:
        descubiertas[f1][c1] = ficha1
        descubiertas[f2][c2] = ficha2
        encontrado += 2
        print('¡ENCONTRÓ una pareja..!', ficha1, ficha2)
    else:
        equivocado += 1
        print('Las fichas son diferentes: ', ficha1, ficha2)

# SALIDA
print('Solución del tablero:')
for fila in tablero:
    print(fila)
print('Estado del juego:')
for fila in descubiertas:
    print(fila)

if encontrado == (n * n):
    print('¡Muy bien..!! todas las fichas encontradas')
else:
    print('Perdió... se equivocó el máximo de veces...')
    print('Fichas descubiertas:', encontrado)


'''
10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
a.	la diagonal principal.
b.	la diagonal inversa.
'''

def obtener_diagonales(matriz):
    if len(matriz) != len(matriz[0]):
        print("La matriz no es cuadrada.")
        return None, None

    # Diagonal principal
    diagonal_principal = [matriz[i][i] for i in range(len(matriz))]

    # Diagonal inversa
    diagonal_inversa = [matriz[i][len(matriz) - 1 - i] for i in range(len(matriz))]

    return diagonal_principal, diagonal_inversa

# Ejemplo de uso
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal, diagonal_inversa = obtener_diagonales(matriz_ejemplo)

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_inversa)

'''
11.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso
si la divisa no está en el diccionario.
'''

divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
consulta = input("Ingrese la divisa que desea consultar: ")
if consulta in divisas:
    print(f"El símbolo de {consulta} es: {divisas[consulta]}")
else:
    print(f"La divisa {consulta} no está en el diccionario.")

'''
12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje '<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>'.
'''

datos = {}
name = input("Ingrese su nombre: ")
age = int(input("Ingrese su edad: "))
ubi = input("Ingrese su direcccion: ")
phone = input("Ingrese su telefono: ")
datos.update({"Nombre":name, "Edad":age, "Direccion":ubi, "Telefono":phone})
print(f'{datos["Nombre"]} tiene {datos["Edad"]} años, vive en {datos["Direccion"]} y su número de teléfono es {datos["Telefono"]}')

'''
13.	Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
'''

frutas ={"banana": 150,"manzana":200,"naranja":250}

fruta = input("Que fruta desea llevar?").lower()
kg = int(input("Cuantos kilos desea?"))

if fruta not in frutas:
    print("Fruta no valida")
if fruta == "banana":
    precio = frutas["banana"]*kg
    print(f"Su total es: ${precio}")
elif fruta == "manzana":
    precio = frutas["manzana"]*kg
    print(f"Su total es: ${precio}")
elif fruta == "naranja":
    precio = frutas["naranja"]*kg
    print(f"Su total es: ${precio}")
