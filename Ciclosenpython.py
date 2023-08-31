#BUCLE FOR

#Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
#La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el contenido de sus mensajes.
#Uno de los equipos decide utilizar un método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje-considerando la posición de cada una en el alfabeto–
#una determinada cantidad de lugares. 
#Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”. 
#Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales. 
#Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se correrán las letras) será dado por el usuario antes de comenzar a encriptar.
#Los 5 mensajes usarán el mismo corrimiento. 
#Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”. 
#Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo
#matemático permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27 
#Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación. 

corrimiento = int(input("Ingrese el valor de desplazamiento: "))
msj_cifrado= ""

for i in range(5):
    mensaje=input ("Ingrese su mensaje: ")
    if mensaje==mensaje.upper () : 

        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:

        abc="abcdefghijklmnñopqrstuvwxyz" 
    for letra in mensaje:
        if letra in abc:
            msj_cifrado += abc[((abc.index(letra)+corrimiento)%27)]
        else:
            msj_cifrado+=letra
print(f"El msj cifrado es: {msj_cifrado}")


# BUCLE WHILE

# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0.
# Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

num=1
digitos_pares=0
digitos_impares=0

while num != 0:
    num=int(input("Ingrese un numero entero positivo: ")) 
    if num != 0:
        if num % 2 == 0:
            digitos_pares+=1
        else:
            digitos_impares+=1
    else:
        break
print(f"La cantidad de dígitos pares son {digitos_pares} y los digitos impares son {digitos_impares}")    