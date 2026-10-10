import random

lista = []
suma = 0

while len(lista) < 100:
    num = random.randint(1,100)
    lista.append(num)

for i in range(1,len(lista),2) :
    suma += lista[i]
print(lista)
print(f'la suma de los numeros en las posiciones impares de la lista es: {suma}')