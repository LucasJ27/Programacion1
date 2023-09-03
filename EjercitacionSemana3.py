dia = input("Ingrese el dia (dia,DD/MM)").lower()
dia_semana = dia.split(",")[0].strip()
dia_numero = int(dia.split(",")[1].strip().split("/")[0])
mes_numero = int(dia.split(",")[1].strip().split("/")[1])

if (dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "miercoles") and (dia_numero >= 1 and dia_numero <= 31) and (mes_numero >= 1 and mes_numero <= 12):
    print("Se tomaron examenes")
    alumnos = int(input("Cuantos alumnos rindieron?: "))
    aprobados = int(input("Cuantos alumnos aprobaron?:"))
    porcentaje_aprobados = aprobados / alumnos
    print(f"El porcentaje de alumnos aprobados es {porcentaje_aprobados*100}%")
elif dia_semana == "jueves":
        asistencia = int(input("Ingrese su porcentaje de asistencia: "))
        if asistencia >= 50:
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
elif dia_semana == "viernes" and (dia_numero == 1 and (mes_numero == 1 or mes_numero == 7)):        
        print("Comienzo de nuevo ciclo")
        cantidad_alumnos = int(input("Ingrese la cantidad de nuevos alumnos: ")) 
        arancel_alumno = int(input("Ingrese el arancel por cada alumno: "))
        total_arancel = cantidad_alumnos * arancel_alumno
        print(f"El ingreso total sera de: ${total_arancel} ")
else:
    print("Se produjo un error")
        
        



   
        


