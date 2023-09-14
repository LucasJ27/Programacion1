option = ""
while True: 
    text = input("Ingresa la oracion que desea analizar: ")
    if not text.isalpha(): #..Validacion del correcto formato del texto(solo letras)
        print("Por favor, ingresa solo letras")
        continue
    while True: #..Estructura principal
        vowels_in_text = set()

        print("-----------------")
        print("Que desea hacer \n 1 - Invertir la oración \n 2 - Consultar cantidad de vocales \n 3 - Consultar cant. de  una letra \n 4 - Ingresar otra oracion diferente \n 5 - Salir")
        
        option = input(": ")

        if option == "1": #..Opciones
            print(f"\n La oracion invertida es :{text[::-1]}\n")

        elif option == "2":
            vowels = "aeiou"
            counter = 0
            for letra in text:
                if letra.lower() in vowels:
                    counter +=1
                    vowels_in_text.add(letra.lower())
            resultado = ", ".join(str(item) for item in vowels_in_text)        
            print(f"\n La cantidad de vocales es {counter}, las vocales son {resultado} \n")

        elif option == "3":
            letter = input("Que letra desea contar: ").lower()
            counter = 0
            for x in text.lower():
                if x == letter:
                    counter +=1
            print(f"\n La cantidad de veces que aparece {letter} en {text} es: {counter} \n")

        elif option == "4":
            break

        elif option == "5":
            break
        
    if option == "5":
        break