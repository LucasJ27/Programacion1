class Motorcycle:
    state = "New"
    engine = False
    def __init__(self, color,license_plate,fuel_tank,wheels,brand, model,manufacturing_date,top_speed,weight):
        self.color = color
        self.license_plate = license_plate
        self.fuel_tank = fuel_tank
        self.wheels = wheels
        self.brand = brand
        self.model = model
        self.manufacturing_date = manufacturing_date
        self.top_speed = top_speed
        self.weight = weight

    def start_engine(self):
        if self.engine == False:
            print("El motor se ha puesto en marcha")
            self.engine = True
        elif self.engine == True:
            print("El motor ya esta en marcha")

    def stop_engine(self):
        if self.engine == True:
            print("El motor se ha detenido")
            self.engine = False
        elif self.engine == False:
            print("El motor no esta en marcha")

    def check_price(self):
        print(f"El precio de la motocicleta {self.brand} {self.model} es de {self.price}$.")


    




