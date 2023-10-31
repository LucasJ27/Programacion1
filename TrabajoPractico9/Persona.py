'''
1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
Construye los siguientes métodos para la clase:
•	Un constructor, donde los datos pueden estar vacíos.
•	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
•	mostrar(): Muestra los datos de la persona.
•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
'''
class Persona:

    def __init__(self, name="",edad=0,dni=""):
        self.__name = name
        self.__edad = edad
        self.__dni = dni
     
    @property
    def name(self):
        return self.__name

    
    @name.setter
    def name(self, value):
        self.__name = value

    
    @property
    def edad(self):
        return self.__edad

   
    @edad.setter
    def edad(self, value):
        self.__edad = value

    
    @property
    def dni(self):
        return self.__dni

    
    @dni.setter
    def dni(self, value):
        self.__dni = value
    
    def mostrar(self):
        print(f"El nombre de la persona es {self.__name} tiene {self.__edad} años y su Nº de DNI es: {self.__dni}")
    def esMayorDeEdad(self):
        return self.__edad > 18
            