from dimensionadas_funciones import procesar_pasajeros
from dimensionadas_funciones import obtener_pais_destino
from dimensionadas_funciones import comprasClientes
'''
1.	Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). Por ejemplo: 
*('Manuel Juarez', 12345678, 'San Juan'), ('Silvana Paredes', 62258472, 'Mendoza')
 
Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo: 
*('Buenos Aires', 'Argentina'), ('Lisboa', 'Portugal'), ('Mendoza', 'Argentina')+ 
 
Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones: 
-	Agregar pasajeros a la lista de viajeros. 
-	Agregar ciudades a la lista de ciudades. 
-	Dado el DNI de un pasajero, ver a qué ciudad viaja. 
-	Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad. 
-	Dado el DNI de un pasajero, ver a qué país viaja. 
-	Dado un país, mostrar cuántos pasajeros viajan a ese país. 
-	Salir del programa. 

'''
'''
ciudades_destino = {'mendoza':1,'san juan':1}
pais_destino = {'argentina':2}
pasajeros = [
    ('manuel juarez', 12345678, 'san juan'),
    ('silvana paredes', 62258472, 'mendoza'),
]

ciudades = [
    ('buenos aires', 'argentina'),
    ('lisboa', 'portugal'),
    ('mendoza', 'argentina'),
    ('san juan', 'argentina'),
]

while True:
    options = int(input("Que desea hacer?: \n1- Agregar pasajeros \n2- Agregar ciudades \n3- Consultar ciudad de destino del pasajero \n4- Ver cantidad de viajantes a una ciudad \n5- Consultar pais de destino del pasajero \n6- Ver cantidad de viajantes a un pais \n7- Salir "))
    
    if options == 1:
        nombre = input("Nombre del Pasajero: ").lower()
        dni = int(input("Dni del Pasajero: "))
        ciudad = input("Ciudad del Pasajero: ").lower()
        pasajero = (nombre, dni, ciudad)
        pasajeros.append(pasajero)
        ciudades_destino[ciudad] = ciudades_destino.get(ciudad, 0) + 1
        
    elif options == 2:
        ciudad = input("Ingrese el nombre de la ciudad que desea agregar: ").lower()
        paises = input("A que pais pertenece esta ciudad?: ").lower()
        ciudad_pais = (ciudad, paises)
        ciudades.append(ciudad_pais)
        
    elif options == 3:
        destino_pasajero = int(input("Ingrese el DNI del pasajero: "))
        for pasajero in pasajeros:
            if pasajero[1] == destino_pasajero:
                print(f"La ciudad de destino del pasajero {pasajero[0]} es: {pasajero[2]}")
    elif options == 4:
        ciudad_consulta = input("Ingrese el nombre de la ciudad para ver la cantidad de viajantes: ").lower()
        cantidad_viajantes = ciudades_destino.get(ciudad_consulta, 0)
        print(f"La cantidad de viajantes a {ciudad_consulta.title()} es {cantidad_viajantes}")
    elif options == 5:
        destino_pasajero = int(input("Ingrese el DNI del pasajero: "))
        for pasajero in pasajeros:
            if pasajero[1] == destino_pasajero:
                ciudad_destino = pasajero[2]
                pais_destino = obtener_pais_destino(ciudad_destino, ciudades)
                print(f"El pais de destino del pasajero {pasajero[0]} es {pais_destino}")
    elif options == 6:
        pais_consulta = input("Ingrese el nombre del pais para ver la cantidad de viajantes: ").lower()
        cantidad_pais = pais_destino.get(pais_consulta, 0)
        print(f"La cantidad de viajantes a {pais_consulta.title()} es {cantidad_pais}")
    elif options == 7:
        break

resultados = procesar_pasajeros(pasajeros, ciudades)

for resultado in resultados:
    print(f"Nombre: {resultado[0].title()}, DNI: {resultado[1]}, Destino: {resultado[2].title()}, País: {resultado[3].title()}")


Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual 
contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
*('Nuria Costa', 5, 1234.5,'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741')

Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente 
puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que 
contenga cada domicilio una sola vez

'''    

compras = [
    ('Juan Pérez', 5, 120.50, 'Avenida de las Flores 123'),
    ('María Rodríguez', 8, 75.20, 'Calle del Sol 456'),
    ('Roberto Gómez', 12, 200.80, 'Boulevard de la Luna 789'),
    ('Ana García', 3, 150.0, 'Calle del Bosque 101'),
    ('Pedro Martínez', 18, 400.50, 'Avenida del Mar 210'),
]

envio_facturas = comprasClientes(compras)
print(envio_facturas)
