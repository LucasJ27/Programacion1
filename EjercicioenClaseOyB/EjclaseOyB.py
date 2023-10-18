from funcionesOyB import ordenamiento_burbuja, ordenamiento_por_seleccion, ordenamiento_por_insercion, merge_sort, busqueda_lineal, busqueda_binaria


#---------------------- ORDENAMIENTO BURBUJA ----------------------#

mi_array = [64, 34, 25, 12, 22, 11, 90]
print("Array antes del ordenamiento burbuja:", mi_array)
ordenamiento_burbuja(mi_array)
print("Array después del ordenamiento burbuja:", mi_array)

#---------------------- ORDENAMIENTO POR SELECCION ----------------------#

mi_array = [64, 34, 25, 12, 22, 11, 90]
print("Array antes del ordenamiento por selección:", mi_array)

ordenamiento_por_seleccion(mi_array)

print("Array después del ordenamiento por selección:", mi_array)

#---------------------- ORDENAMIENTO POR INSERCION ----------------------#

mi_array = [64, 34, 25, 12, 22, 11, 90]
print("Array antes del ordenamiento por inserción:", mi_array)

ordenamiento_por_insercion(mi_array)

print("Array después del ordenamiento por inserción:", mi_array)

#---------------------- ORDENAMIENTO POR MEZCLA (MERGE SORT) ----------------------#

mi_array = [64, 34, 25, 12, 22, 11, 90]
print("Array antes del Merge Sort:", mi_array)

merge_sort(mi_array)

print("Array después del Merge Sort:", mi_array)

#---------------------- BUSQUEDA LINEAL ----------------------#

mi_lista = [64, 34, 25, 12, 22, 11, 90]
elemento_buscado = 22

resultado = busqueda_lineal(mi_lista, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")

#---------------------- BUSQUEDA BINARIA ----------------------#

mi_lista_ordenada = [11, 12, 22, 25, 34, 64, 90]
elemento_buscado = 22

resultado = busqueda_binaria(mi_lista_ordenada, elemento_buscado)

if resultado != -1:
    print(f"El elemento {elemento_buscado} se encuentra en el índice {resultado}.")
else:
    print(f"El elemento {elemento_buscado} no se encuentra en la lista.")