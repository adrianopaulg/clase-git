pares = []
impares = []
for i in range(1,101) :
    if i % 2 == 0 :
        pares.append(i)
    else :
        impares.append(i)
print('pares')
for j in pares :
    print(j)
for k in impares :
    print(k)