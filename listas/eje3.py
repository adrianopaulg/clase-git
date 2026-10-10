import random
lista = []
while len(lista) < 100 :
    num = random.randint(100,1000)
    if num % 2 == 0 :
        lista.append(num)
print(lista)