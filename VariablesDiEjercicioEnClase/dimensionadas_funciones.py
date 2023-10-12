def procesar_pasajeros(pasajeros, ciudades):
    resultado = []

    for nombre, dni, destino in pasajeros:
        pais_destino = obtener_pais_destino(destino, ciudades)
        resultado.append((nombre, dni, destino, pais_destino))

    return resultado

def obtener_pais_destino(destino, ciudades):
    for ciudad, pais in ciudades:
        if ciudad == destino:
            return pais

    return "Desconocido"


'''
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente 
puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que 
contenga cada domicilio una sola vez
(cliente, día del mes, monto, domicilio del cliente)
'''    

def comprasClientes(compras):
    facturas = set()

    for compra in compras:
        facturas.add(compra[3])
    return list(facturas)

def cargar_socio(socios,numero, nombre, ingreso, cuota_al_dia):
    socios[numero] = {'nombre': nombre, 'ingreso': ingreso, 'cuota_al_dia': cuota_al_dia}

def pagar_cuota(socio_numero,socios):
    if socio_numero in socios:
        socios[socio_numero]["cuota_al_dia"] = True
        print(f"El socio Nº{socio_numero} ha pagado todas las cuotas adeudadas.")
    else:
        print("Número de socio no válido.")

def modificar_fecha_ingreso(socios,fecha_antigua, nueva_fecha):
    for numero, datos in socios.items():
        if datos["ingreso"] == fecha_antigua:
            socios[numero]["ingreso"] = nueva_fecha





