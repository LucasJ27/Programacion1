def get_dna():
    adn = [] #Creamos una lista vacia en donde vamos a guardar las secuencias ingresadas por el usuario para formar el ADN del humano o mutante
    print("Vamos a ingresar el ADN del humano o mutante.")
    print("El ADN de un humano o mutante se forma a partir de 6 secuencias de 6 acrónimos de bases nitrogenadas cada una.")
    print("Las bases nitrogenadas se representan con los acrónimos A, T, C y G.")
    
    for i in range(6):
        while True:
            dna = input(f"Ingrese la {i+1}º secuencia de 6 bases nitrogenadas (A, T, C, G) del ADN: ").upper() #Pedimos por teclado las 6 secuencias de letras para formar la "matriz" 6x6 que representa el ADN
            if dna.isdigit():
                print("No puedes ingresar numeros")
            elif len(dna) > 6: #En esta condicion corroboramos que la secuencia ingresada por el usuario no tenga mas de 6 letras
                print("La secuencia ingresada no puede tener mas de 6 bases nitrogenadas.") 
            elif len(dna) < 6: #En esta condicion que la secuencia ingresada por el usuario no tenga menos de 6 letras
                print("La secuencia ingresada no puede tener menos de 6 bases nitrogenadas")
            else:
                for base in dna: #Con este ciclo for recorremos cada elemento de la secuencia ingresada por el usuario
                    if base not in 'ATCG': #Si alguno de los elementos no coincide con ninguno de los "acronimos" o "bases nitrogenadas" permitidas (A,T,C o G), mostramos por pantalla un mensaje de error
                        print("Secuencia invalida")
                        break
                if base in 'ATCG':#Si la secuencia ingresada esta conformada por los "acronimos" permitidos (A,T,C o G)      
                    adn.append(dna) #Guardamos la secuencia en la lista "adn"
                    break 
    return adn


def is_mutant(dna):
    total_secuencias = 0 # En esta variable vamos a guardar la suma total de secuencias que encontremos en el ADN del individuo

                        ########################################                BUCLE PARA RECORRER FILAS           ########################################
                            
    secuencias = 0  # En la variable secuencias guardamos cuantas secuencias encontramos en cada uno de los recorridos, ya sea recorrido de filas, columnas, diagonales.. Por ejemplo si recorremos las filas y encontramos 2 secuencias, esas 2 secuencias las guardamos en esta variable
    for row in dna: # Con este for itero por cada secuencia del "ADN" 
        for i in range(len(row) - 3): # Con este ciclo itero hasta los ultimos 4 elementos de la secuencia actual(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
            if (row[i] == row[i + 1]) and (row[i + 1] == row[i + 2]) and (row[i + 2] == row[i + 3]): # Comprobamos si en alguna de las secuencias/filas se cumple la condicion de 4 elementos iguales
                if i == 0 or row[i] != row[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la misma fila. Asi evito contar secuencias que se superpongan en la fila
                    secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1
    
    total_secuencias += secuencias #Sumamos las secuencias encontradas al contador de secuencias totales encontradas
                           
                        ########################################                BUCLE PARA RECORRER COLUMNAS           ########################################
     
    columns = []  # Creamos una lista vacia en donde vamos a almacenar las columnas para luego poder verificar si existe alguna secuencia de 4 letras iguales

    secuencias = 0 # La variable la reiniciamos para poder ir contando las secuencias que encontremos en cada uno de los bucles

    for i in range(len(dna[0])):
        column = []  # En esta lista vamos a almacenar cada elemento de la columna
        for row in dna: # Con este ciclo recorremos cada fila del "ADN" o "matriz"
            column.append(row[i])  # Agregamos el elemento en la posicion i de la fila a la lista columna
        columns.append(column)  # Una vez que tenemos la columna completa, la agregamos a la lista de columnas

    # Recorremos cada columna para verificar en que columnas se encuenta una secuencia de 4 letras iguales consecutivas
    for columna in columns:
        for i in range(len(columna) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la columna(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
            if (columna[i] == columna[i + 1]) and (columna[i + 1] == columna[i + 2]) and (columna[i + 2] == columna[i + 3]): # Comprobamos si en alguna columna se cumple la condicion de 4 elementos iguales
                if i == 0 or columna[i] != columna[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la misma columna. Asi evito contar secuencias que se superpongan en la columna
                    secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL PRINCIPAL            ########################################

    main_diag = [] # En esta lista vamos a almacenar los elementos de la diagonal principal
    secuencias = 0

    for i in range(6):
        main_diag.append(dna[i][i])  # Agregamos los elementos de la diagonal principal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(main_diag) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (main_diag[i] == main_diag[i + 1]) and (main_diag[i + 1] == main_diag[i + 2]) and (main_diag[i + 2] == main_diag[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or main_diag[i] != main_diag[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1     

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL SUPERIOR            ########################################    

    upper_diag= [] # En esta lista vamos a almacenar los elementos de la diagonal superior, la diagonal superior se encuentra por encima de la diagonal pricipal (esta diagonal contiene 5 letras).
    secuencias = 0

    for i in range(5):
        upper_diag.append(dna[i][i+1])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
        # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(upper_diag) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (upper_diag[i] == upper_diag[i + 1]) and (upper_diag[i + 1] == upper_diag[i + 2]) and (upper_diag[i + 2] == upper_diag[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or upper_diag[i] != upper_diag[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL POSTERIOR SUPERIOR             ########################################

    post_diag = [] # En esta lista vamos a almacenar los elementos de la diagonal posterior superior, esta diagonal se encuentra por encima de la diagonal superior (esta diagonal contiene 4 letras)
    secuencias = 0 

    for i in range(4):
        post_diag.append(dna[i][i+2])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal
        
    for i in range(len(post_diag) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (post_diag[i] == post_diag[i + 1]) and (post_diag[i + 1] == post_diag[i + 2]) and (post_diag[i + 2] == post_diag[i + 3]): # Si encontramos una secuencia de 4 elementos iguales en la diagonal posterior superior, aumentamos el contador de secuencias en 1
            secuencias += 1 # En este caso al ser una diagonal que solo contiene 4 letras, no hace falta que verifiquemos que no se superpongan secuencias

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INFERIOR             ########################################
 
    lower_diag = [] # En esta lista vamos a almacenar los elementos de la diagonal inferior, esta diagonal se encuentra por debajo de la diagonal principal
    secuencias = 0

    for i in range(5):
        lower_diag.append(dna[i+1][i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(lower_diag) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (lower_diag[i] == lower_diag[i + 1]) and (lower_diag[i + 1] == lower_diag[i + 2]) and (lower_diag[i + 2] == lower_diag[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or lower_diag[i] != lower_diag[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL POSTERIOR INFERIOR             ######################################## 

    lower_post = [] # En esta lista vamos a almacenar los elementos de la diagonal posterior inferior, esta diagonal se encuentra por debajo de la diagonal inferior(esta diagonal contiene 4 letras)
    secuencias = 0

    for i in range(4):
        lower_post.append(dna[i+2][i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
        # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(lower_post) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (lower_post[i] == lower_post[i + 1]) and (lower_post[i + 1] == lower_post[i + 2]) and (lower_post[i + 2] == lower_post[i + 3]): # Si encontramos una secuencia de 4 elementos iguales en la diagonal, aumentamos en uno la variable secuencia
            secuencias += 1 # En este caso al ser una diagonal que solo contiene 4 letras, no hace falta que verifiquemos que no se superpongan secuencias

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INVERSA              ########################################

    reverse_diag = []  # En esta lista vamos a almacenar los elementos de la diagonal inversa
    secuencias = 0

    for i in range(6):
        reverse_diag.append(dna[i][5-i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(reverse_diag) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (reverse_diag[i] == reverse_diag[i + 1]) and (reverse_diag[i + 1] == reverse_diag[i + 2]) and (reverse_diag[i + 2] == reverse_diag[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or reverse_diag[i] != reverse_diag[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INVERSA SUPERIOR               ######################################## 
    
    upper_reverse = []  # En esta lista vamos a almacenar los elementos de la diagonal inversa superior, esta diagonal se encuentra encima de la diagonal inversa (esta diagonal contiene 5 letras)
    secuencias = 0

    for i in range(5):
        upper_reverse.append(dna[i][4-i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
        # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(upper_reverse) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (upper_reverse[i] == upper_reverse[i + 1]) and (upper_reverse[i + 1] == upper_reverse[i + 2]) and (upper_reverse[i + 2] == upper_reverse[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or upper_reverse[i] != upper_reverse[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INVERSA POSTERIOR SUPERIOR               ########################################

    post_reverse = []  # En esta lista vamos a almacenar los elementos de la diagonal inversa posterior superior, esta diagonal se encuentra por encima de la diagonal inversa superior (esta diagonal contiene 4 letras)
    secuencias = 0

    for i in range(4):
        post_reverse.append(dna[i][3-i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal

    for i in range(len(post_reverse) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal (para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (post_reverse[i] == post_reverse[i + 1]) and (post_reverse[i + 1] == post_reverse[i + 2]) and (post_reverse[i + 2] == post_reverse[i + 3]): # Si encontramos una secuencia de 4 elementos iguales en la diagonal, aumentamos en uno la variable secuencia 
            secuencias += 1 # En este caso al ser una diagonal que solo contiene 4 letras, no hace falta que verifiquemos que no se superpongan secuencias

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INVERSA INFERIOR               ########################################

    lower_reverse = [] # En esta lista vamos a almacenar los elementos de la diagonal inversa inferior, esta diagonal se encuentra por debajo de la diagonal inversa (esta diagonal tiene 5 letras)
    secuencias = 0

    for i in range(5):
        lower_reverse.append(dna[i+1][5-i])  # Agregamos los elementos de la diagonal a la lista creada anteriormente
        # Este print lo hago para ir viendo el recorrido de la diagonal 

    for i in range(len(lower_reverse) - 3):  # Con este ciclo itero hasta los ultimos 4 elementos de la diagonal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (lower_reverse[i] == lower_reverse[i + 1]) and (lower_reverse[i + 1] == lower_reverse[i + 2]) and (lower_reverse[i + 2] == lower_reverse[i + 3]): # Comprobamos si en la diagonal se cumple la condicion de 4 elementos iguales
            if i == 0 or lower_reverse[i] != lower_reverse[i - 1]: # Verificamos que la secuencia actual no empiece justo despues de otra secuencia identica en la diagonal. Asi evito contar secuencias que se superpongan en la diagonal
                secuencias += 1 # Si se cumple la condicion, aumentamos el contador de secuencias en 1

    total_secuencias += secuencias

                        ########################################                BUCLE PARA RECORRER LA DIAGONAL INVERSA POSTERIOR INFERIOR                ########################################

    lower_Post = [] # En esta lista vamos a almacenar los elementos de la diagonal inversa posterior inferior, esta diagonal se encuentra por debajo de la diagonal inversa inferior (esta diagonal tiene 4 letras)
    secuencias = 0

    for i in range(4):
        lower_Post.append(dna[i+2][5-i])  # Agregamos los elementos de la diagonal principal a la lista creada anteriormente
         # Este print lo hago para ir viendo el recorrido de la diagonal
    for i in range(len(lower_Post) - 3):  # Con este ciclo itero hasta los últimos 4 elementos de la diagonal principal(para no pasarnos del rango). Indico un limite "-3" para asegurarme que siempre queden por lo menos 4 elementos restantes por recorrer
        if (lower_Post[i] == lower_Post[i + 1]) and (lower_Post[i + 1] == lower_Post[i + 2]) and (lower_Post[i + 2] == lower_Post[i + 3]): # Si encontramos una secuencia de 4 elementos iguales en la diagonal, aumentamos en uno la variable secuencia 
            secuencias += 1 # En este caso al ser una diagonal que solo contiene 4 letras, no hace falta que verifiquemos que no se superpongan secuencias

    total_secuencias += secuencias
    
    #Si el total de secuencias encontradas es mayor a 1
    if total_secuencias > 1:
        return True #Significa que el adn analizado corresponde a un Mutante, retornamos True
    else:
        return False #Si no se encontraron mas de una secuencia en el adn, retornamos False

