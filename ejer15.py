turno=str(input("Ingrese su tipo de turno (diurno/nocturno)")).lower()
horas=float(input("Ingrese la cantidad de horas trabajadas: "))
dia=str(input("Ingrese el dia de la semana: ")).lower()
pago=0
if turno=="diurno":
    if dia=="domingo":
        pago=horas*2.5
    else:
        pago=horas*1.5
else:
    if dia =="domingo":
        pago=horas*3.5
    else:
        pago=horas*2.25
print("El pago es: ", pago)