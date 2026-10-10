import random
lista = []
while len(lista) < 100 :
    num = random.randint(1,2000)
    if num % 2 == 0 and num % 3 == 0 :
        lista.append(num)
print(lista)