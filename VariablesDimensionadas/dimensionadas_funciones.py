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




