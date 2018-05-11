from algo1 import *
n=input_int("Ingrese número:")
aux=0
for a in range(1,n+1):
    if n%a==0:
        aux=aux+1
if aux!=2:
    print("El número no es primo.")
else:
    print("El número es primo.")
    