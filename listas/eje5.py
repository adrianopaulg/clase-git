import random
pares = []
impares = []

while len(pares) < 50 or len(impares) < 50 :
    num = random.randint(1,1000)
    if num % 2 == 0 :
        if len(pares) != 50 :
            pares.append(num)
    elif num % 2 != 0 :
        if len(impares) != 50 :
            impares.append(num)
print(pares)
print(impares)
print(len(pares))
print(len(impares))