from Persona import Persona
from Cuenta import Cuenta
from Triangulo import Triangulo
from Contacto import Contacto
from Agenda import Agenda

'''
1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
•	mostrar(): Muestra los datos de la persona.
•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

persona_uno = Persona("Lucas Cabrera",28,"38756526")
if not isinstance(persona_uno.name, str):
    print("Nombre invalido.")
else:
    persona_uno.mostrar()

if not isinstance(persona_uno.dni, str):
    print("DNI invalido.")
else:
    persona_uno.mostrar()

if not isinstance(persona_uno.edad, int):
    print("Edad invalida.")
else:
    persona_uno.mostrar()


persona_uno.esMayorDeEdad()

'''
2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
•	mostrar(): Muestra los datos de la cuenta.
•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
'''

cuenta_uno = Cuenta(persona_uno,0)
cuenta_uno.ingresar(200000)
cuenta_uno.retirar(100000)
cuenta_uno.mostrar()

'''
3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
'''

lado_uno = int(input("Ingrese la longitud del lado 1: "))
lado_dos = int(input("Ingrese la longitud del lado 2: "))
lado_tres = int(input("Ingrese la longitud del lado 3: "))

triangulo_uno = Triangulo(lado_uno,lado_dos,lado_tres)
triangulo_uno.tipoTriangulo()
triangulo_uno.ladoMayor()

'''
4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
•	Añadir contacto
•	Lista de contactos
•	Buscar contacto
•	Editar contacto
•	Cerrar agenda
'''

agenda = Agenda()
while True:
    options = int(input("Que desea hacer?: \n1- Añadir contacto \n2- Lista de contactos \n3- Buscar contacto \n4- Editar contacto \n5- Cerrar agenda"))
    if options == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono: ")
        email = input("Ingrese el email: ")
        agenda.añadir_contacto(nombre, telefono, email)
    elif options == 2:
        agenda.lista_contactos()
    elif options == 3:
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        agenda.buscar_contacto(nombre)
    elif options == 4:
        nombre = input("Ingrese el nombre del contacto que desea editar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_telefono = input("Ingrese el nuevo teléfono: ")
        nuevo_email = input("Ingrese el nuevo email: ")
        agenda.editar_contacto(nombre, nuevo_nombre, nuevo_telefono, nuevo_email)
    elif options == 5:
        print("Agenda cerrada.")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        