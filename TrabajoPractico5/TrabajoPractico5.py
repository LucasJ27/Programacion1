import math
from FuncionesTP5 import validate_dni
from FuncionesTP5 import last_word
from FuncionesTP5 import ID_club
from FuncionesTP5 import is_multiple
from FuncionesTP5 import temperature
from FuncionesTP5 import text_function
from FuncionesTP5 import get_max_min
from FuncionesTP5 import area_perimeter
from FuncionesTP5 import login
from FuncionesTP5 import apply_function
from FuncionesTP5 import duplicate
from FuncionesTP5 import phrase_dict
from FuncionesTP5 import vector
from FuncionesTP5 import prime_number
from FuncionesTP5 import factorial
from FuncionesTP5 import frequency
from FuncionesTP5 import final_function
from FuncionesTP5 import factorial_max

'''
#--- Punto 1 ---
dni = int(input("Ingrese su numero de dni: "))
print(validate_dni(dni))

#--- Punto 2 ---
word = input("Ingrese una palabra: ")
print(last_word(word))

#--- Punto 3 ---

while True:
    name = input("Ingrese su nombre (ingrese un espacio en blanco para finalizar): ")
    if name == "" or name == " ":
        break
    last_name = input("Ingrese su apellido: ")
    DNI = int(input("Ingrese su numero de DNI: "))
    lenDNI = len(str(DNI))
    if lenDNI != 7 and lenDNI != 8:
        print("Numero de DNI incorrecto")
        continue
    club_member = ID_club(name,last_name,DNI)
    print(f"ID -> {club_member}")   
         

#--- Punto 4 ---
   
number = int(input("Ingresa el primer numero: "))
number_2 = int(input("Ingresa el segundo numero: "))
print(is_multiple(number,number_2))

#--- Punto 5 ---
days = int(input("Ingrese con un numero la cantidad de dias: "))
counter = 0
while (counter < days):
        counter += 1
        temp_max = int(input("Ingrese la temperatura maxima: "))
        temp_min = int(input("Ingrese la temperatura minima: ")) 
        print(f"La temperatura media es: {temperature(temp_max, temp_min)}")

#--- Punto 6 ---      

text = input("Ingresa un texto: ")
print(f"La cadena modificada quedaria de la siguiente manera: {text_function(text)}")

#--- Punto 7 ---
numbers = []
while True:
    number_in = int(input("Ingrese los numeros que desee (ingrese 0 para salir): "))
    if number_in == 0:
        break
    numbers.append(number_in)
print(f"El valor maximo y el valor minimo de la lista son: {get_max_min(numbers)}")

#--- Punto 8 ---
radio = int(input("Ingrese el radio de la circunferencia: "))
print(area_perimeter(radio))

#--- Punto 9 ---

attempts = 0 
while attempts < 3:
    user = input("Ingrese su nombre de usuario: ").lower()
    password = input("Ingrese su contraseña: ").lower()
    if login(user,password):
        print(login(user,password))
        break
    else:
        attempts += 1
    if attempts == 3:
        print("Se han superado los intentos permitidos. Vuelva mas tarde")

#--- Punto 10 ---
#--- Punto 11 ---
numberslist = []
while True:
    numbers = int(input("Ingrese los numeros que desea duplicar(ingrese 0 para salir): "))
    numberslist.append(numbers)
    if numbers == 0:
        break
print(apply_function(duplicate, numberslist))

#--- Punto 12 ---

phrase_1 = input("Ingresa una frase: ")
print(phrase_dict(phrase_1))

#--- Punto 13 ---

component_1 = int(input("Ingresa el primer componente del vector: "))
component_2 = int(input("Ingresa el segundo componente del vector: "))
print(f"El modulo del vector es: {vector(component_1, component_2)}")

#--- Punto 14 ---

number = int(input("Ingresa un numero entero: "))
print(prime_number(number))

#--- Punto 15 ---

multi_numbers = []
while True:
    number = int(input("Ingrese un numero entero (o ingrese 0 para terminar): "))
    if number == 0:
        break
    multi_numbers.append(number)
print(factorial(multi_numbers))
print(f"La cantidad total de numeros ingresados por el usuario es: {len(multi_numbers)}")


#--- Punto 16 ---

number = int(input("Ingrese un numero: "))
digits = int(input("Ingrese un digito (del 0 al 9): "))
print(frequency(number,digits))

'''

#--- Punto 17 ---
numbers = []
while True:
    number = int(input("Ingrese numeros primos(si desea salir ingrese un numero que no sea primo): "))
    if not prime_number(number):
        break
    numbers.append(number)
    digit = int(input("Ingrese un digito (del 0 al 9): "))
    print(f"La suma de los digitos del numero primo ingresado es: {final_function(number, digit)}")
    print(f"En el numero {number}, el digito {digit} aparece {frequency(number,digit)} veces")
print(f"El mayor numero primo ingresado es: {max(numbers)} y su factorial es: {factorial_max(max(numbers))}")
    