class Triangulo:
    def __init__(self, lado_uno,lado_dos,lado_tres):
        self.__lado_uno = lado_uno
        self.__lado_dos = lado_dos
        self.__lado_tres = lado_tres

    def tipoTriangulo(self):
        if self.__lado_uno == self.__lado_dos and self.__lado_uno == self.__lado_tres:
            print("Es un triangulo equilatero")
        elif self.__lado_uno == self.__lado_dos or self.__lado_uno == self.__lado_tres or self.__lado_dos == self.__lado_tres:
            print("Es un triángulo isósceles")
        else:
            print("Es un triángulo escaleno")
            

    def ladoMayor(self):
        if self.__lado_uno == self.__lado_dos == self.__lado_tres:
            print(f"Al ser un triángulo equilátero, todos sus lados tienen el mismo tamaño: {self.__lado_uno}")
        else:
            if self.__lado_uno >= self.__lado_dos and self.__lado_uno >= self.__lado_tres:
                print(f"El lado de mayor tamaño es: {self.__lado_uno}")
            elif self.__lado_dos >= self.__lado_uno and self.__lado_dos >= self.__lado_tres:
                print(f"El lado de mayor tamaño es: {self.__lado_dos}")
            else:
                print(f"El lado de mayor tamaño es: {self.__lado_tres}")
        
