from FuncionesParcial2 import get_dna, is_mutant
print()
print("BIENVENIDO AL DETECTOR DE MUTANTES")
print()
while True:
    options = int(input("Que desea hacer? (seleccione ingresando el numero de la opcion):\n1- Introducir ADN\n2- Analizar ADN introducido\n3- Ver ADN \n4- Salir"))
    print()
    if options == 1:
        dna = get_dna()
    elif options == 2:
        if is_mutant(dna):
            print(f"RESULTADO DEL ANALISIS: {is_mutant(dna)}")
            print("El ADN analizado corresponde a un MUTANTE. ")
            print()
        else:
            print(f"RESULTADO DEL ANALISIS: {is_mutant(dna)}")
            print("El ADN analizado corresponde a un HUMANO.")
            print()
    elif options == 3:
        print("GRAFICO DEL ADN INTRODUCIDO:")
        print()
        for row in dna:
            for element in row:
                print(element, end=" ")
            print()
        print()
    elif options == 4:
        print("GRACIAS POR UTILIZAR NUESTRO DETECTOR DE MUTANTES")
        break