horas_trabajadas= int(input("Escriba el número de horas trabajadas: "))
tarifa= float(input("Escriba la tarifa por hora: "))
pension= input("Escriba la modalidad de pension (AFP/ONP): ")


if horas_trabajadas >40:
    hextra= horas_trabajadas-40
    horas_trabajadas= 40
else:
    hextra=0

sueldo_bruto=horas_trabajadas*tarifa + hextra*1.5*tarifa

if pension.upper()== "AFP":
    descuento= (sueldo_bruto*0.10)
elif pension.upper()== "ONP":
    descuento=(sueldo_bruto*0.13)
else:
    print("Ningún sistema de pensión")
    descuento=0

sueldo_neto= sueldo_bruto-descuento
print ("Descuento: ",descuento)
print("Sueldo neto: ",sueldo_neto)