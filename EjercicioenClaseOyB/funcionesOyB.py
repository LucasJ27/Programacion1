# Elaborar una función que realice cada ordenamiento y búsqueda vistos en la presentación.

def ordenamiento_burbuja(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(n):
        # Últimos i elementos ya están ordenados, no necesitamos compararlos
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es más grande que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenamiento_por_seleccion(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(n):
        # Encontrar el índice del elemento mínimo en el subarray no ordenado
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        # Intercambiar el elemento mínimo encontrado con el primer elemento no ordenado
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

def ordenamiento_por_insercion(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(1, n):
        # Guardar el elemento actual para su inserción
        actual = arr[i]

        # Mover los elementos del subarray ordenado que son mayores que el actual
        j = i - 1
        while j >= 0 and actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insertar el elemento actual en la posición correcta
        arr[j + 1] = actual

def merge_sort(arr):
    if len(arr) > 1:
        # Dividir el array en dos mitades
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        # Llamadas recursivas para ordenar ambas mitades
        merge_sort(izquierda)
        merge_sort(derecha)

        # Combinar las dos mitades ordenadas
        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                arr[k] = izquierda[i]
                i += 1
            else:
                arr[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            arr[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            arr[k] = derecha[j]
            j += 1
            k += 1

def busqueda_lineal(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i  # Devolver el índice si se encuentra el elemento

    return -1  # Devolver -1 si el elemento no se encuentra en la lista

def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        # Verificar si el elemento está en la mitad
        if lista[medio] == elemento:
            return medio
        # Si el elemento es menor, buscar en la mitad izquierda
        elif lista[medio] > elemento:
            derecha = medio - 1
        # Si el elemento es mayor, buscar en la mitad derecha
        else:
            izquierda = medio + 1

    return -1  # Devolver -1 si el elemento no se encuentra en la lista