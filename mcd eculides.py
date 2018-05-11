from algo1 import *
from libreriafinal import *

def mcd(r0,r1,aux=0):
    if r1==0:
        return aux
    else:
        aux=r1
        return mcd((r0//r1)*r1,(r0%r1),aux)

"""r0=input_int("Ingrese a:") 
r1=input_int("Ingrese b:")
if r0 >= r1:
    prueba=mcd(r0,r1)
    print("MCD:",prueba)"""
for a in range(1,4):
    print(mcd(4,a))
