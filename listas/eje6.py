import random

pares = 0
impares = 0

lista = []
n = int(input('cuantos numeros quieres que se generen: '))

for i in range(n) :
    num = random.randint(100,1000)
    lista.append(num)
for j in lista :
    if j % 2 == 0 :
        pares += 1
    else :
        impares = impares + j
print(f'hay {pares} numeros pares en la lista')
print(f'la suma de todos los impares es {impares}')