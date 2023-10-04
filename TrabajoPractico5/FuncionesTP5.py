import math
#1. Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
def validate_dni(number_dni):
    
    dni_str = str(number_dni)
    
    
    if 7 <= len(dni_str) <= 8:
        return True
    else:
        return False
    
#2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. 
# También podría haber espacios al principio o al final del string pasado por parámetro.

def last_word(word):
    word_split = word.split()
    if not word_split:
        return 0
    return len(word_split[-1])

#3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. Para eso ingresará nombre completo y número de DNI de cada socio,
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido.
# Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y los 3 primeros dígitos de su DNI. Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254

def ID_club(name, last_name, DNI):
    name_lastN = name.split()
    DNI_str = str(DNI)
    if len(name_lastN) >= 2:
        name1 = name_lastN[0]
        name2 = name_lastN[1]
        ID = name1 + str(len(last_name)) + DNI_str[0:3]
    else:
        ID = name + str(len(last_name)) + DNI_str[0:3]
    return ID

#4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo. 
def is_multiple(number, number2):
    if number2 == 0:
        return False
    if number % number2 == 0:
        return True 
    else:
        return False
    
#5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
# El programa pedirá el número de días que se van a introducir.

def temperature(temp_max, temp_min):
    temp_med = (temp_max + temp_min) / 2
    return temp_med

#6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

def text_function(text):
    letters = []
    for letter in text:
        # Agregar un espacio solo después de las letras
        if letter.isalpha() or letter.isdigit():
            letters.append(letter + " ")
        else:
            # Mantener los símbolos sin espacio adicional
            letters.append(letter)

    return "".join(letters)

#7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

def get_max_min(numbers):
    if not numbers:
        return None, None

    max_number = max(numbers)
    min_number = min(numbers)

    return max_number, min_number

#8. Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

def area_perimeter(radio):
    area = math.pi*(radio**2)
    perimeter = math.pi * (radio*2)
    return f"El area de la circunferencia es: {area} y el perimetro: {perimeter}"

#9. Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
def login(user,password):
    if user == "usuario1" and password == "asdasd":
        return True
    else:
        return False
    
#10. Escribir una función que aplique un descuento a un precio.
# Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito y devolver el precio final de la compra.
 
#def discount():        

#11. Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
def apply_function(function, list_1):
    results = []
    for elemento in list_1:
        result = function(elemento)
        results.append(result)
    return results

def duplicate(number):
    return number * 2

#12 Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

def phrase_dict(phrase):
    phrase_split = phrase.split()
    phrase_dict = {}
    for word in phrase_split:
        phrase_dict[word] = len(word)
    return phrase_dict

#13 Escribir una función que calcule el módulo de un vector.

def vector(componente1, componente2):
    return math.sqrt((componente1**2) + (componente2**2))

#14 Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

def prime_number(number):
    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    return is_prime

#15. Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total.
# Utilizar una o más funciones, según sea necesario.
   
def factorial(multi_numbers):
    for facto in multi_numbers:
        factorial = 1
        for element in range(1, facto + 1):
            factorial *= element
        print(f"El factorial de {facto} es: {factorial}")
    
                
#16. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia.
def frequency(number,digits):
    str_number = str(number)
    frequency_count = 0
    for char_digit in str_number:
        if char_digit == str(digits):
            frequency_count += 1
    return frequency_count

#17. Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos.
# También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia).
# Al finalizar el programa, mostrar el factorial del mayor número ingresado.

def final_function(number, digits):
    number_str = str(number)
    sum_digits = 0
    for digits in number_str:
        sum_digits += int(digits)
    return sum_digits

def factorial_max(number):
    factorial = 1
    for element in range(1, number + 1):
            factorial *= element
    return factorial