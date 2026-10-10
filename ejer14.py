a=int(input("Ingrese el precio de venta: "))
if a <80:
    a=a*0
elif a>=80 and a<=600:
    a=a*0.1
else:
    a=30+(a*0.2)
print("Su comisión es de: ", a, "soles")