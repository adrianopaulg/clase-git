edad=int(input("Ingrese su edad: "))
socio=input("¿es socio del club? (si o no)").lower()
tarifa=30
if edad>=18 and socio=="no":
    tarifa=tarifa*1

elif edad<=18 and socio=="si":
    tarifa=tarifa*0.8
    
elif edad>=18 and socio=="si":
    tarifa=tarifa*0.6
else:
    tarifa=tarifa*0.5
print("la tarifa a pagar es: ", tarifa)