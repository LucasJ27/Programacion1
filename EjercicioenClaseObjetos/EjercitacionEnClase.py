from Motorcycle import Motorcycle
moto1 = Motorcycle(color="Rojo",license_plate=123,brand="Yamaha",model="FZ",manufacturing_date="24/10/2023",top_speed=110,
weight=200,fuel_tank=10,wheels=2)
moto2 = Motorcycle(color="Azul",license_plate=456,brand="Yamaha",model="FZ",manufacturing_date="20/10/2023",top_speed=110,
weight=200,fuel_tank=10,wheels=2)

moto1.start_engine()
moto1.stop_engine()
moto1.price = 10000
print(f"El precio de la motocicleta {moto1.brand} {moto1.model} es de {moto1.price}$.")
moto1.check_price()
moto2.check_price()