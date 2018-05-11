from algo1 import *
from random import randint

def busco_ocupadas(x,i):
    for a in range(0,len(x)):
        if x[a][i]==1:
            return 1
    return 0

def asigno_city(x):
    n=len(x)
    for i in range(0,n):
        #aux=busco_ocupadas(x,i)
        for j in range(0,n):
            if busco_ocupadas(x,i)==0:
                x[i][j]=1
                break
    imprimirMAT(x,n,n)

def imprimirMAT(matriz,m,n):
    for i in range(0,m):
        for j in range(0,n):
            #print('[',end='')
            print("[",matriz[i][j],end=']')
        print("")

def relleno_random(matriz,n,rand):
    #esta funcion rellena una matriz con numeros aleatorios entre 0 y rand
    for a in range(0,n):
        for b in range(0,n):
            matriz[a][b]=randint(0,rand)

n=4
#una fila "i" representa las ciudades "j" a las que el terminator "i" puede ir
b=Array(n,Array(n,0)) #matriz de costos
x=Array(n,Array(n,0)) #matriz de asignación
#relleno las matrices aleatoriamente
relleno_random(b,n,20)
relleno_random(x,n,0)
print("Matriz de costos:")
imprimirMAT(b,n,n)
print("----------------")
asigno_city(x)
