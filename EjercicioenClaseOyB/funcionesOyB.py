# Elaborar una función que realice cada ordenamiento y búsqueda vistos en la presentación.

def ordenamiento_burbuja(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenamiento_por_seleccion(arr):
    n = len(arr)

    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j

        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

def ordenamiento_por_insercion(arr):
    n = len(arr)

    for i in range(1, n):
        actual = arr[i]

        j = i - 1
        while j >= 0 and actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = actual

def merge_sort(arr):
    if len(arr) > 1:
        mitad = len(arr) // 2
        izquierda = arr[:mitad]
        derecha = arr[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

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
            return i

    return -1

def busqueda_binaria(lista, elemento):
    izquierda, derecha = 0, len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == elemento:
            return medio
        elif lista[medio] > elemento:
            derecha = medio - 1
        else:
            izquierda = medio + 1

    return -1 