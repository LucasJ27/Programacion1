from Persona import Persona

'''
2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
•	mostrar(): Muestra los datos de la cuenta.
•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

'''

class Cuenta:

    def __init__(self, titular=Persona(),cantidad=None):
        self.__titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular
        
    @titular.setter
    def titular(self, value):
        self.__titular = value

    @property
    def cantidad(self):
        return self.__cantidad
        
    @cantidad.setter
    def cantidad(self, value):
        self.__cantidad = value

    def mostrar(self):
        titular_info = f"Titular: {self.__titular.name} - DNI: {self.__titular.dni}"
        return print(f"{titular_info}\nSaldo disponible en la cuenta: {self.__cantidad}$")
        
    def ingresar(self, deposito):
        if deposito > 0:
            self.__cantidad += deposito
            print(f"Se depositaron {deposito}$ en la cuenta.")
            
    
    def retirar(self, retiro):
        if retiro > 0:
            self.__cantidad -= retiro
            print(f"Se retiraron {retiro}$ de la cuenta.")
            
            