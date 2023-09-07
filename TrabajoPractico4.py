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
        D = int(input(""))
        print(f"D {D}")
        deposit += D
    elif consult == "r":
        R = int(input(""))
        print(f"R {R}")
        deposit -= R
print(deposit)   

#3. Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
#Imprimir la cantidad total de números primos ingresados.
#Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.


