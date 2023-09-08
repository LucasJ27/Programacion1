#1. Create a while loop with the following characteristics:

#• The initial value of the variable x will be 0.
#• The increment value will be 1.
#• The exit condition of the loop will be greater than or equal to 30.
#• The execution must be broken when x is equal to 15.
#• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
#• You must skip the executions with the value of x in 4, 6 and 10.
#• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
#• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.

x = 0
while x < 30:
    x+=1
    if x == 4 or x == 6 or x == 10:
        print(f"Se salto el valor {x} de x")
        continue
    if x == 15:
        print(f"La ejecucion del bucle se rompio cuando X valia {x}")    
        break
    print(f"El valor del bucle es: {x}")


#1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas.
# Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

list_lines = []
while True:
    lines = input("Ingrese una oracion(o deje una linea en blanco para terminar): ").upper()
    if lines == "":
        print("Ha finalizado la entrada de lineas")
        break
    list_lines.append(lines)
print(list_lines)

#2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
#La bitácora de operaciones tiene la siguiente forma:
#D 100
#R 50

#D 100 significa que depositó 100 pesos
#R 50 significa que retiró 50 pesos

#Ejemplo de una entrada:
#D 200
#D 200
#R 100
#D 50
#Introducir una línea vacía indica que ha finalizado la bitácora.
#La salida de éste programa sería:
#350

deposit = 0
while True:
    consult = input("Desea retirar o depositar (R / D)? \nDeje una linea en blanco para terminar:  ").lower()
    if (consult == ""):
        break
    if consult == "d":
        D = int(input("Cuanto desea depositar?"))
        print(f"D {D}")
        deposit += D
    elif consult == "r":
        R = int(input("Cuanto desea retirar?"))
        print(f"R {R}")
        deposit -= R
print(f"Su saldo es: ${deposit}")   

#3. Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
#Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

number_list = []
while True:
    number = int(input("Introduzca un numero mayor a 1 (si desea salir ingrese 0): "))
    if number == 0:
        break
    if number <= 1:
        is_prime = False
    else:
        is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break 
    if is_prime:
        number_list.append(number)
print(f"La cantidad de numeros primos ingresados es: {len(number_list)} ")

#4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos
# y múltiplos de 10.
#Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year1 = int(input("Ingrese un año: "))
year2 = int(input("Ingrese un segundo año: "))
years = []
for i in range(year1, year2+1):
    if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)) and (i % 10 == 0) :
        years.append(i)
print(f"En el rango de años ingresados los años que son bisiestos y multiplos de 10 a la vez son: {years}")

#5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
# Utiliza la declaración continue para omitir los números impares.
even_number = []
for i in range(1,21):
    if i % 2 == 0:
        even_number.append(i)
    else:
        continue
print(f"Los numeros pares del 1 al 20 son:{even_number}")

#6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico.
# Cuando encuentres el número, usa break para salir del bucle.

list_number = [1,2,3,4,5,6,7,8,9,10]
for i in list_number:
    if 10 == i:
        print("El numero se encuentra en la lista")
        break

#7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
# Utiliza un bucle while para permitir al usuario seleccionar una opción.
# Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

while True:
    option = int(input("Seleccione una opcion (ingresando 1,2 o 3. Ingrese 0 para terminar): \nOpcion 1\nOpcion 2 \nOpcion 3 "))
    if option == 0:
        print("Saliendo del programa")
        break
    elif option == 1:
        print("Selecciono la opcion 1")
        
    elif option == 2:
        print("Selecciono la opcion 2")
        
    else:
        print("Selecciono la opcion 3")