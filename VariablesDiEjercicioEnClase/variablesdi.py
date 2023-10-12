from dimensionadas_funciones import procesar_pasajeros, obtener_pais_destino, comprasClientes, cargar_socio, pagar_cuota, modificar_fecha_ingreso
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
                print(f"El pais de destino del pasajero {pasajero[0].title()} es {pais_destino}")
    elif options == 6:
        pais_consulta = input("Ingrese el nombre del pais para ver la cantidad de viajantes: ").lower()
        cantidad_pais = pais_destino.get(pais_consulta, 0)
        print(f"La cantidad de viajantes a {pais_consulta.title()} es {cantidad_pais}")
    elif options == 7:
        break

resultados = procesar_pasajeros(pasajeros, ciudades)

for resultado in resultados:
    print(f"Nombre: {resultado[0].title()}, DNI: {resultado[1]}, Destino: {resultado[2].title()}, País: {resultado[3].title()}")

'''Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual 
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

 

'''
Crear un programa para gestionar datos de los socios de un club, permitiendo:
- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar 
son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar 
con los datos de los socios fundadores ya cargados:
o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad 
ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
- Imprimir el listado de socios completo

'''

socios = {
    1: {'nombre': 'Amanda Nunez', 'ingreso': '17/03/2009', 'cuota_al_dia': False},
    2: {'nombre': 'Barbara Molina', 'ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'ingreso': '17/03/2009', 'cuota_al_dia': True}
}

while True:
    options = int(input("Que desea hacer?: \n1- Cargar socio \n2- Consular cantidad de socios \n3- Pagar Cuota \n4- Modificar fecha de ingreso \n5- Eliminar Socio \n6- Listado de Socios"))
    
    if options == 1:
        numero = int(input("Ingrese Nº socio: "))
        nombre = input("Nombre del Socio: ")
        fecha = (input("Fecha de ingreso(ddmmaaaa): "))
        fecha = f"{fecha[0:2]}/{fecha[2:4]}/{fecha[4:8]}"
        cuota = input("Cuota al dia? s/n: ").lower()
        if cuota == 's':
            cuota = True                        
        cargar_socio(socios,numero,nombre,fecha,cuota)

                
    elif options == 2:
        print(f"Actualmente tenemos: {len(socios)} socios")
        
    elif options == 3:
        numero = int(input("Ingrese el numero de socio: "))
        print(pagar_cuota(numero,socios))

    elif options == 4:
        modificar_fecha_ingreso(socios,"13/03/2018", "14/03/2018")        

    elif options == 5:
        numero = int(input("Ingrese el numero de socio a eliminar: "))
        del socios[numero]
        print("Socio eliminado")

    elif options == 6:
        for numero in socios.items():
            print(numero)
