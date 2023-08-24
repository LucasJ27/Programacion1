#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input("Ingrese la base del rectangulo: "))
altura = int(input("Ingrese la altura del rectangulo: "))

print(f"El perimetro es: {(base+altura)*2}")
print(f"El area es: {(base*altura)}")

#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto = int(input("Ingrese un lado: "))
cateto_dos = int(input("Ingrese un segundo lado: "))
hipotenusa = (cateto**2 + cateto_dos**2)**(1/2)
print(f"La hipotenusa del triangulo es: {hipotenusa}")

#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

numero_uno = int(input("Ingrese un numero: "))
numero_dos = int(input("Ingrese un  numero: "))

suma = numero_uno + numero_dos
resta = numero_uno - numero_dos
division = numero_uno / numero_dos
multiplicacion = numero_uno * numero_dos
print(suma, resta, division, multiplicacion)

#4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
# Recordar que la fórmula para la conversión es: C = (F-32) * 5/9

gradoF = int(input("Ingrese la temperatura en grados Fahrenheit: "))
gradoC = print(f"La temperatura ingresada en grados Celsius es: {(gradoF-32)*(5/9)}")

#5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

# a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# El problema es que la variable "nombre" no puede estar dentro del input de la manera en la que esta.

# Solucion:

nombre = input("Ingrese su nombre: ")
A = input(f"{nombre} cual es tu cancion favorita?: ")
print(A)

# b) precio = input(“Precio: “)
# total = precio + (precio * 0.1)
# El problema en esta instruccion es que estamos ingresando el precio en una variable de tipo String, de esta forma no vamos a poder calcular el total.

# Solucion:

precio = int(input("Precio: "))
total = precio + (precio * 0.1)
print(total)

# c) edad = int(input(“Edad: “))
# print(tu edad es, edad)
# El problema en esta instruccion es que al momento de imprimir por pantalla la variable edad, no se estan usando las comillas ("") correspondientes.

# Solucion:

edad = int(input("Edad: "))
print(f"Tu edad es: {edad}")

# d) edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)
# El problema en esta instruccion es que no estamos comprobando si la edad ingresada es 18, simplemente estamos asignandole el valor 18 a la variable edad.
# Aparte en el print tampoco estamos invocando bien la variable edad.

# Solucion:

edad = int(input("Edad: "))
if edad == 18:
      print(f"Tu edad es: {edad}")
else:
      print("La edad no es 18")

#6.	Calcular la media de tres números pedidos por teclado

num_uno = int(input("Ingrese el primer numero: "))
num_dos = int(input("Ingrese el segundo numero: "))
num_tres = int(input("Ingrese el tercer numero: "))
media = (num_uno + num_dos + num_tres) / 3
print(f"La media de los 3 numeros ingresados es: {media}")

#7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

total_minutos = int(input("Ingrese la cantidad de minutos: "))
horas = total_minutos // 60
minutos = total_minutos % 60
print(f"{total_minutos} minutos son {horas} horas y {minutos} minutos.")

#8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
# y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldo_base = float(input("Ingrese su sueldo base: "))
venta1 = float(input("Ingrese el monto de la primera venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))
comision = (venta1 + venta2 + venta3) * 0.1
print(f"En concepto de comision vas a recibir un total de {comision}")
sueldo_total = sueldo_base + comision
print(f"Tu sueldo total sumando las comisiones por ventas realizadas en el mes sera de: {sueldo_total}")

#9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

total = int(input("Ingrese el total de su compra: "))
descuento = total * 0.15
print(f"El total de su compra con el descuento aplicado es de: ${total - descuento}")

#10. Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial_uno = int(input("Ingresa tu calificacion en el primer parcial: "))
parcial_dos = int(input("Ingresa tu calificacion en el segundo parcial: "))
parcial_tres = int(input("Ingresa tu calificacion en el tercer parcial: "))
examen_final = int(input("Ingresa tu calificacion en el examen final: "))
trabajo_final = int(input("Ingresa tu calificacion en el trabajo final: "))
promedio_parcial = (parcial_uno + parcial_dos + parcial_tres) / 3
calificacion_final = (promedio_parcial * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"Su calificacion final en la materia de Algoritmos es: {calificacion_final}")

#11. Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

num_1 = int(input("Ingresa el primer numero: "))
num_2 = int(input("Ingresa el segundo numero: "))

distancia = abs(num_1 - num_2)
print(f"La distancia que existe entre el numero 1 y el numero 2 es: {distancia}")

#12. Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero = float(input("Ingrese un numero: "))
raiz_cuadrada = (numero ** 0.5)
raiz_cubica = (numero ** (1/3))
print(f"La raiz cuadrada del numero ingresado es {raiz_cuadrada} y la raiz cubica es {raiz_cubica}")

#13. Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

dos_cifras = int(input("Ingresa un número de dos cifras: "))

if 10 <= dos_cifras <= 99:  # Asegurarnos de que el número tiene dos cifras
    unidades = dos_cifras % 10
    decenas = dos_cifras // 10
    print(unidades)
    print(decenas)

    numero_invertido = unidades * 10 + decenas

    print(f"El número invertido es: {numero_invertido}" )
else:
    print("El número ingresado no tiene dos cifras.")

#14. Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

variable_A = int(input("Ingrese la variable A: "))
variable_B = int(input("Ingrese la variable B: "))

variable_C = variable_A
variable_A = variable_B
variable_B = variable_C

print(f"El valor final de la variable A es {variable_A} y el valor final de la variable B es {variable_B}")

#15. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

# Solicitar al usuario que ingrese los datos
HH = int(input("Ingresa la hora de partida (HH): "))
MM = int(input("Ingresa los minutos de partida (MM): "))
SS = int(input("Ingresa los segundos de partida (SS): "))
T = int(input("Ingresa el tiempo de viaje en segundos (T): "))

# Convertir todo a segundos
tiempo_partida = HH * 3600 + MM * 60 + SS
tiempo_llegada = tiempo_partida + T

# Calcular la hora de llegada
horas_llegada = (tiempo_llegada // 3600) % 24
minutos_llegada = (tiempo_llegada % 3600) // 60
segundos_llegada = tiempo_llegada % 60

# Mostrar la hora de llegada
print(f"Hora de llegada a la ciudad B:{horas_llegada:02d}:{minutos_llegada:02d}:{segundos_llegada:02d}")

#16 Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombreuno = input("Ingresa tu nombre: ")
apellido_uno = input("Ingresa tu primer apellido: ")
apellido_dos = input("Ingresa tu segundo apellido: ")
print(nombreuno[0], apellido_uno[0], apellido_dos[0])

#17 Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario = input("Ingrese su nombre: ")
print(f"Ahora estas en la matrix {usuario}")

#18 Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar.

costo_cena = float(input("Cuanto costo la cena?: "))
servicio = costo_cena *0.062
propina = costo_cena * 0.1
costo_total = costo_cena + servicio + propina
print(f"El costo total de la cena es de: {costo_total}")

#19 Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes).
# Finalmente, mostrar la fecha en formato dd/mm/aaaa.
dia = int(input("Ingresa el dia de tu nacimiento: "))
mes = int(input("Ingresa el mes de tu nacimiento: "))
anio = int(input("Ingresa el año de tu nacimiento: "))

print(f"La fecha de nacimiento del usuario es: {dia}/{mes}/{anio}")

#20 Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
fecha_nacimiento = input("Ingresa tu fecha de nacimiento en formato DDMMAAA: ")
dia = fecha_nacimiento[0:2]
mes = fecha_nacimiento[2:4]
anio2 = fecha_nacimiento[4:8]
print(f"La fecha de nacimiento del usuario es: {dia}/{mes}/{anio2}")

#21 Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
# Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
# Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.

km_x_litro = int(input("Ingrese la cantidad de km x litro: "))
capacidad_tanque = int(input("Ingrese la capacidad en litros del tanque: "))
kilometrosarecorrer = int(input("Ingrese la cantidad de kilometros a recorrer: "))
litros_nafta = kilometrosarecorrer / km_x_litro #Aca tenemos la cantidad de litros que necesitamos para recorrer la cantidad de km necesarios
tanques_totales = litros_nafta / capacidad_tanque #Aca tenemos la cantidad de tanques que necesitamos para recorrer la cantidad de km ingresada
tanques_totales = round(tanques_totales, 2)

print(f"Para recorrer la cantidad de kilometros ingresados vamos a necesitar {tanques_totales} tanques de nafta")
