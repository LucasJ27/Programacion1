def ordenamiento_burbuja(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(n):
        # Últimos i elementos ya están ordenados, no necesitamos compararlos
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es más grande que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenamiento_burbuja_descendente(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(n):
        # Últimos i elementos ya están ordenados, no necesitamos compararlos
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es más chico que el siguiente elemento
            if arr[j] < arr[j + 1]:
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

def ordenamiento_insercion_longitud(arr):
    n = len(arr)

    # Iterar a través de todos los elementos del array
    for i in range(1, n):
        # Guardar el elemento actual para su inserción
        actual = arr[i]

        # Mover los elementos del subarray ordenado que son mayores que el actual
        j = i - 1
        while j >= 0 and len(actual) < len(arr[j]):
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
            
def ordenamiento_por_conteo(arr):
    # Encuentra el valor máximo en el array
    max_valor = max(arr)
    # Encuentra el valor mínimo en el array
    min_valor = min(arr)

    # Calcula el rango de valores en el array
    rango = max_valor - min_valor + 1

    # Inicializa un arreglo de conteo con ceros
    conteo = [0] * rango

    # Llena el arreglo de conteo con la frecuencia de cada valor
    for elemento in arr:
        conteo[elemento - min_valor] += 1

    # Reconstruye el arreglo original a partir del arreglo de conteo
    arreglo_ordenado = []
    for i in range(rango):
        arreglo_ordenado.extend([i + min_valor] * conteo[i])

    return arreglo_ordenado