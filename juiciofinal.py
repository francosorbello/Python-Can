from algo1 import *
from random import randint

def busco_ocupadas(x,i):
    for a in range(0,len(x)):
        if x[a][i]==1:
            return False
    return True

def asigno_city(b,x,n):
    for i in range(0,n):
        costo=b[i][0] #asigno un costo base
        aux=0 #esta var controla en caso de que la primer ciudad sea la de menor costo
        ciudad_ocupada=busco_ocupadas(x,i)
        for j in range(0,n):
            if b[i][j]<costo and x[i][j]==0 and ciudad_ocupada==True:
                aux=1#si ya tengo una sol cambio el valor de aux para evitar usar la primer ciudad
                x[i][j]=1 #pongo un terminator en esa ciudad
                break 
            if j==(n-1) and aux==0:
                x[i][0]=1  
    return x
    
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
asigno_city(b,x,n)
imprimirMAT(x,n,n)