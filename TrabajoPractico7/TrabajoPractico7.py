from FuncionesTP7 import ordenamiento_burbuja, ordenamiento_por_seleccion, ordenamiento_por_insercion, ordenamiento_insercion_longitud,ordenamiento_burbuja_descendente, ordenamiento_por_conteo, merge_sort

#1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.
numbers = []
while True:
    entrada = int(input("Ingrese los numeros que desea agregar a la lista(ingrese 0 para salir): "))
    if entrada == 0:
        break
    numbers.append(entrada)
    
print("Lista antes del ordenamiento burbuja:", numbers)
ordenamiento_burbuja(numbers)
print("Lista después del ordenamiento burbuja:", numbers)

#2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.

words = []
while True:
    entrada2 = input("Ingrese las palabras que desea agregar a la lista(ingrese 0 para salir): ")
    if entrada2 == "0":
        break
    words.append(entrada2)
    
print("Lista antes del ordenamiento burbuja:", words)
ordenamiento_por_seleccion(words)
print("Lista después del ordenamiento burbuja:", words)

#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.).
# Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

lista_de_libros = [
    {
        'título': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'año_de_publicación': 1967
    },
    {
        'título': '1984',
        'autor': 'George Orwell',
        'año_de_publicación': 1949
    },
    {
        'título': 'El Gran Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'año_de_publicación': 1925
    },
    {
        'título': 'Don Quijote de la Mancha',
        'autor': 'Miguel de Cervantes',
        'año_de_publicación': 1605
    }
]

# Ordenar por año de publicación
lista_anio = sorted(lista_de_libros, key=lambda x: x['año_de_publicación'])

# Mostrar la lista ordenada
for libro in lista_anio:
    print(f'Título: {libro["título"]}, Autor: {libro["autor"]}, Año de publicación: {libro["año_de_publicación"]}')

#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

words2 = []
while True:
    entrada2 = input("Ingrese las palabras que desea agregar a la lista(ingrese 0 para salir): ")
    if entrada2 == "0":
        break
    words2.append(entrada2)
    
print("Lista antes del ordenamiento por insercion segun la longitud: ", words2)
ordenamiento_insercion_longitud(words2)
print("Lista después del ordenamiento por insercion segun la longitud: ", words2)

#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.
# Escribe un programa que tome una lista de números como entrada y la ordene en orden descendente utilizando el método de ordenamiento de burbuja.
numbers2 = []
while True:
    entrada3 = int(input("Ingrese los numeros que desea agregar a la lista(ingrese 0 para salir): "))
    if entrada3 == 0:
        break
    numbers2.append(entrada3)
    
print("Lista antes del ordenamiento burbuja descendente: ", numbers2)
ordenamiento_burbuja_descendente(numbers2)
print("Lista después del ordenamiento burbuja descendente: ", numbers2)

#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

lista = [10,9,8,7,6,5,4,3,2,1,0]
print("Lista antes del ordenamiento por conteo: ", lista)
ordenamiento_por_conteo(lista)
print("Lista después del ordenamiento por conteo: ", lista)

#7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

num_words= ["Hola", "Mundo", "Python",3,2,1]

# Inicializa listas vacías para los números y las cadenas
numeros = []
cadenas = []

# Separa los números de las cadenas usando bucles for
for elemento in num_words:
    if isinstance(elemento, int):
        numeros.append(elemento)
    elif isinstance(elemento, str):
        cadenas.append(elemento)
#Ordenamos los numeros
numeros.sort()
# Ordenamos las cadenas
cadenas.sort()

# Combina las listas ordenadas, primero los números y luego las cadenas
resultado = numeros + cadenas

# Imprime la lista resultante
print(resultado)

#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

numbers3 = [10,9,8,7,6,5,4,3,2,1]

print("Lista antes del Merge Sort:", numbers3)
merge_sort(numbers3)
print("Lista después del Merge Sort:", numbers3)

