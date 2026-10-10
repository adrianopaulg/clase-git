lista = []
n = int(input('cuantos vas a ingresar? '))
for i in range(n) :
    num = int(input('ingresa el numero: '))
    lista.append(num**2)
for j in lista :
    print(j)