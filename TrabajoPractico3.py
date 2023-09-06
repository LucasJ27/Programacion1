#1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)

#2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
years = 0
for i in range(age):
    years += 1
    print(f"Usted ha cumplido {years} años")


#3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

number2 = int(input("Ingrese un numero entero positivo: "))
numbers = []
for i in range(1, number2 + 1):
    if i%2 != 0:
        numbers.append(str(i))
print("Los numeros impares de la lista son: " + ", ".join(numbers))

#4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

number3 = int(input("Ingrese un numero entero positivo: "))
countdown = []
for i in range(1, num +1):
    countdown.append(str(i))
countdown.reverse()
print(", ".join(countdown))

#5- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por
#pantalla el capital obtenido en la inversión cada año que dura la inversión.

invest = int(input("Ingrese la cantidad que desea invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
investment_years = int(input("Ingrese la cantidad de años: "))
for i in range(1,investment_years + 1):
    capital = invest * (1 + annual_interest/1)**(i)
    print(f"En el año {i} de inversion obtenemos un capital de: ${capital:.2f}")

#6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

number_int = int(input("Igrese un numero entero: "))

for i in range(1,number_int+1):
    print("*"*i)

#7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

table = int(input("Ingrese la tabla de multiplicar que desea: "))

for i in range(1,11):
    print(str(i) + " X " + str(table) + " = " + str(i*table))

#8- Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

number_int2 = int(input("Ingrese un numero entero: "))
numberlist = []
for i in range(1, number_int2+1):
    if i%2 != 0:
        numberlist.append(str(i))
        numberlist.sort(reverse = True)
        print(numberlist)
#9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = "contraseña"
while True:
    password2 = input("Ingrese una contraseña: ")
    if password2 == password:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Intentelo de nuevo")
        continue

#10- Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# Pedir al usuario un número entero
number4 = int(input("Ingrese un número entero: "))

# Verificar si el número es primo
if number4 <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(number4 ** 0.5) + 1):
        if number4 % i == 0:
            is_prime = False
            break
# Imprimir el resultado
if is_prime:
    print(f"{number4} es un número primo.")
else:
    print(f"{number4} no es un número primo.")

#11- Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Ingrese una palabra: ").lower()
letters = []
for i in word:
    letters.append(i)
    print(letters)
letters.reverse()
print(letters)

#12- Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

prhase = input("Ingrese una frase: ").lower()
letter = input("Ingrese una letra: ").lower()
counter = 0
for i in prhase:
    if i == letter:
        counter+=1
print(f"La letra {letter} aparece {counter} veces")

#13- Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    eco = input("Grite (o escriba 'salir' para terminar): ")
    if eco.lower() == "salir":
        break
    print(eco)

#14- Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

number_int = int(input("Ingrese el primer numero entero: "))
number_int2 = int(input("Ingrese el segundo numero entero: "))
even_number=[]
odd_number=[]

if number_int > number_int2:
    number_int, number_int2 = number_int2, number_int

for i in range(number_int,number_int2+1):
    if i % 2 == 0:
        even_number.append(i)
    elif i % 2 != 0:
        odd_number.append(i)
print(f"Los numeros pares entre {number_int} y {number_int2} son: {even_number} \nLos numeros impares entre {number_int} y {number_int2} son: {odd_number}")

#15- Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

numberint = int(input("Ingrese un numero entero mayor a cero: "))
dividers = []
for i in range(1,numberint+1):
    if numberint%i == 0:
        dividers.append(i)
print(f"Los divisores de {numberint} son {dividers}")

#16- Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

howmany = input("Cuantos numeros se van a introducir?: ")
negative = []
for i in range(1,int(howmany)+1):
    number = int(input(f"Ingrese el {i}º numero: "))
    if number < 0:
        negative.append(number)
print(f"Se han introducido {len(negative)} numeros negativos")

#17- Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).      

prhase = input("Ingrese una frase: ").lower()
vowels = set()
for i in prhase:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u") :
        vowels.add(i)
print(vowels)

#18- Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma
# de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

# Inicializar los primeros dos números de Fibonacci
fibonacci = [0, 1]

# Generar los siguientes 8 números de Fibonacci
for i in range(2, 10):
    next_number = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_number)

# Imprimir los primeros 10 números de Fibonacci
print("Los primeros 10 números de la sucesión de Fibonacci son:")
for number in fibonacci:
    print(number)

#19- Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar.
# A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
# El programa deberá comprobar que las cantidades ingresadas sean positivas.

total_saving = int(input("Ingrese la cantidad que quiere ahorrar: "))
saving = 0.0
while saving < total_saving:
    saving2 = int(input("Ingrese su ahorro: "))
    if saving2 <= 0:
        print("La cantidad a ahorrar debe ser mayor a 0")
        continue
    saving += saving2
    print(f"Total ahorrado hasta ahora: ${saving}")
print(f"Su objetivo de ahorro eran: ${total_saving}, su total ahorrado es de: ${saving}")

#20- Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

counter = 0
while True:
    number = int(input("Ingrese un numero entero (o ingrese un 0 para terminar):"))
    counter += number
    if number == 0:
        break
print(f"La sumatoria total es de: {counter}")

#21- Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

counter = []
while True:
    number = int(input("Ingrese un numero entero (o ingrese un 0 para terminar):"))
    counter.append(number)
    print(counter)
    if number == 0:
        break
print(f"El mayor numero ingresado fue {max(counter)}")

#22- Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen.
# La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pairs = []
while True:
    number = int(input("Ingrese un numero entero (o ingrese -1 para terminar):"))
    number_str = str(number)
    sum_digits = 0
    if number == -1:
        break
    if number%2 == 0:
        pairs.append(number)
    for digits in number_str:
        sum_digits += int(digits)
    print(f"La suma de digitos que componen a {number_str} es: {sum_digits}")
print(f"La cantidad de numeros pares ingresados por el usuario es de : {len(pairs)}")

#23- Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará,
# la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.
#24- Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que,
# si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

amounts = []
while True:
    amount = int(input("Ingrese el monto de la compra(o ingrese 0 para terminar): "))
    amounts.append(amount)
    if amount == 0:
        break
    elif amount < 0:
        continue
    amount_total = sum(amounts)
    if amount_total > 1000:
        amount_total = amount_total - (amount_total * 0.1)
print(f"El total a pagar del cliente es: {amount_total}")

#25- Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

number = int(input("Ingrese un número entero positivo: "))
if number < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    
    for i in range(1, numero + 1):
        factorial *= i

    print(f"El factorial de {number} es {factorial}")