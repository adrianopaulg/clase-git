import math


num=int(input("Ingresar un  umero: "))
letra=input("Ingrese una letra: ").upper()
if letra=="P":
    c=num**2
    print(c)
elif letra=="R":
   c= math.sqr(num)
   print(c)
else:
    print("error")

