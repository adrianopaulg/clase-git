#lea un numero y muestre un mensaje si su ultimo digito es par o impar
num_1=int(input("Ingrese un numero: "))
ultimo_digito=num_1%10
if ultimo_digito%2==0:
    print("Es par")
else:
    print("No es par")