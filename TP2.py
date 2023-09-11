import math

#1 Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años
#y que el computador es viejo si es mayor a 2 años.
#2 Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
anios = int(input("Ingrese los años de su computadora: ")).lower()

if anios <= 2 and anios >= 0:
    print("Su computadora es nueva")
elif anios > 2:
    print("Su computadora es vieja")
elif anios < 0:
    print("Error")

#3 Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra.
# Si no es así, imprimir ‘no hay coincidencia’.

persona_uno = input("Ingrese el nombre de la persona uno: ").lower()
persona_dos = input("Ingrese el nombre de la persona dos: ").lower()

if persona_uno[0] == persona_dos[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")

#4 Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
# Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’

candidato_A = "rojo"
candidato_B = "verde"
candidato_C = "azul"
candidato = input("Ingrese el candidato que desea votar: \nCandidato A\nCandidato B\nCandidato C").lower()

if candidato == "candidato a":
    print(f"Usted ha votado por el partido {candidato_A}")
elif candidato == "candidato b":
    print(f"Usted ha votado por el partido {candidato_B}")
elif candidato == "candidato c":
    print(f"Usted ha votado por el partido {candidato_C}")
else:
    print("Opcion errónea.")

#5 Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.

letra = input("Ingrese una letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es vocal")
elif len(letra) > 1:
    print("No se puede procesar el dato ingresado")

#6 Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

aniobi = int(input("Ingrese un año: "))

if (aniobi%4 == 0 and aniobi%100 != 0) or (aniobi%400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

#7 Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.

numero_uno = input("Ingrese el primer numero: ")
numero_dos = input("Ingrese el segundo numero: ")
numero_tres = input("Ingrese el tercer numero: ")

if numero_uno < numero_dos and numero_uno < numero_tres:
    print(f"El menor es el primer numero: {numero_uno}")
elif (numero_dos < numero_uno) and (numero_dos < numero_tres):
    print(f"El menor es el segundo numero: {numero_dos}")
elif (numero_tres < numero_uno) and (numero_tres < numero_dos):
    print(f"El menor es el tercer numero: {numero_tres}")

#8 Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos.
#Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

usuario = input("Ingrese su usuario: ").lower()
contraseña = input("Ingrese su contraseña: ").lower()

if (usuario == "Gwenevere") and (contraseña == "excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

#9 Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

sexo_femenino = "femenino"
sexo_masculino = "masculino"

sexo = input("Ingrese su sexo (Femenino/Masculino): ").lower()
nombre = input("Ingrese su nombre: ").lower()

if (sexo == sexo_femenino and nombre[0] < "m"):
    print("Le corresponde el grupo A")
elif (sexo == sexo_femenino):
    print("Le corresponde el grupo B")
elif (sexo == sexo_masculino and nombre[0] > "n"):
    print("Le corresponde el grupo A")
elif (sexo == sexo_masculino):
    print("Le corresponde el grupo B")


#10 Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Puede entrar gratis :D")
elif edad >= 4 and edad <= 18:
    print("El valor de la entrada es de $500")
else:
    print("El valor de la entrada es de $1000")

#11 La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

ingredientes = ["Pimiento","Tofu","Peperoni","Jamon","Salmon"]

pizza = input("Que tipo de pizza desea?:\nVegetariana\nNo vegetariana").lower()


if pizza == "vegetariana":
    ingrediente_veggie = input(f"Que ingrediente desea agregarle?: \n1-{ingredientes[0]}\n2-{ingredientes[1]}").lower()
    if ingrediente_veggie == "pimiento":
        print(f"Eligio la opcion {pizza} y sus ingredientes son:\nMozzarella\nTomate\n{ingredientes[0]}")
    elif ingrediente_veggie == "tofu":
        print(f"Eligio la opcion {pizza} y sus ingredientes son:\nMozzarella\nTomate\n{ingredientes[1]}")
elif pizza == "no vegetariana":
    ingrediente = input(f"Que ingrediente desea agregarle? \n{ingredientes[2]}\n{ingredientes[3]}\n{ingredientes[4]}").lower()
    if ingrediente == "peperoni":
        print(f"Eligio la opcion {pizza} y sus ingredientes son:\nMozzarella\nTomate\n{ingredientes[2]}")
    elif ingrediente == "jamon":
        print(f"Elegio la opcion {pizza} y sus ingredientes son:\nMozzarella\nTomate\n{ingredientes[3]}")
    elif ingrediente == "salmon":
        print(f"Eligio la opcion {pizza} y sus ingredientes son:\nMozzarella\nTomate\n{ingredientes[4]}")

#12 Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

anio_actual = int(input("Ingrese el año actual: "))
anio_x = int(input("Ingrese un año cualquiera:"))
anios = abs(anio_actual - anio_x)

if anio_actual > anio_x:
    print(f"Han pasado {anios} año/años")
else:
    print(f"Faltan {anios} años para llegar a ese año")

#13 Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

if (numero_1 > numero_2) and (numero_1 % numero_2 == 0):
    print(f"{numero_1} es multiplo de {numero_2}")
elif (numero_2 > numero_1) and (numero_2 % numero_1 == 0):
    print(f"{numero_2} es multiplo de {numero_1}")
elif (numero_1 > numero_2) and (numero_1 % numero_2 != 0):
    print(f"El {numero_1} no es multiplo de {numero_2}")
elif (numero_2 > numero_1) and (numero_2 % numero_1 != 0):
    print(f"El {numero_2} no es multiplo de {numero_1}")
elif (numero_1 < 1 or numero_2 < 1):
    print("Uno o los dos numeros ingresados son negativos o nulos")

#14 Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
# x = -b / a

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
x= -b/a
if a == 0:
    if b == 0:
        print("La ecuacion tiene infinitas soluciones")
    else:
        print("La ecuacion no tiene solucion")
else:
    print(f"El valor de x es: {x}")

#15 Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área.
# Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

calcular = input("Desea calcular el area de un triangulo o de un circulo?\nSi desea calcular el area de un triangulo digite t o T\nSi desea calcular el area de un circulo digite c o C").lower()

if calcular == "t":
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    area = (base*altura)/2
    print(f"El area del triangulo es {area}")
elif calcular == "c":
    radio = int(input("Ingrese el radio del circulo: "))
    area = math.pi*(radio**2)
    print(f"El area del circulo es {area}")

#16	Haz una calculadora básica pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# Si operación es 1 entonces debemos ver el resultado de a + b
# Si operación es 2 entonces debemos ver el resultado de a * b
# Si operación es 3 entonces debemos ver el resultado de a - b
# Si operación es 4 entonces debemos ver el resultado de a / b

valor_a = int(input("Ingrese el valor de a: "))
valor_b = int(input("Ingrese el valor de b: "))
opcion = input("Seleccione la opción que desea ingresando el Nº de opcion:\n1 Suma\n2 Multiplicacion\n3 Resta\n4 Division")

if opcion == "1":
    print(f"El resultado de la suma es: {valor_a + valor_b}")
elif opcion == "2":
    print(f"El resultado de la multiplicacion es: {valor_a * valor_b}")
elif opcion == "3":
    print(f"El resultado de la resta es: {valor_a - valor_b}")
elif opcion == "4":
    print(f"El resultado de la division es: {valor_a / valor_b}")

#17 Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo.
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana = input("Ingrese un dia de la semana: ").lower()

if dia_semana == "lunes":
    print("Ingresaste el dia Lunes!")
elif dia_semana == "viernes":
    print("Ingresaste el dia Viernes!")
elif dia_semana == "sabado":
    print("Ingresaste el dia Sabado!")
elif dia_semana == "domingo":
    print("Ingresaste el dia Domingo!")
else:
    print("EL dia ingresado no es correcto")

#18 Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
# La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
# Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.

horas_mes = int(input("Ingrese el total de horas trabajas en el mes: "))
salario_hora = int(input("Ingrese su salario por hora: "))
trabajo_extra = horas_mes - 48
horas_extras = (salario_hora * 0.1) + salario_hora
salario_base = (horas_mes - trabajo_extra) * salario_hora 
salario_extra = ((trabajo_extra * (horas_extras)))

if horas_mes > 48:
    print(f"Trabajo {(trabajo_extra)}hs extras")
    print(f"Su salario total es de: ${salario_base + salario_extra}")

#19 Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60;
# de lo contrario no hay descuento.

lapices = int(input("Cuantos lapices desea llevar?: "))
costo_lapiz = 60
if lapices >= 1000:
    precio_lapiz = costo_lapiz - (costo_lapiz * 0.07)
    print(f"Su total a pagar es de: ${lapices * precio_lapiz}")
elif lapices < 1000:
    print(f"Su total a pagar es de: ${lapices * costo_lapiz}")

#20 Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.

nota_uno = int(input("Ingrese su primer nota: "))
nota_dos = int(input("Ingrese su segunda nota: "))
nota_tres = int(input("Ingrese su tercer nota: "))
nota_cuatro = int(input("Ingrese su cuarta nota: "))
promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4

if promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
