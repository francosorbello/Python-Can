from algo1 import *
from random import randint

def busco_mejor(b,x,i):
    #busco el mejor caso de la fila
    precio=b[i][0]
    aux=0
    for j in range(0,len(x)):
        #ARREGLAR:SI EL PRIMERO ES EL MEJOR LO TOMA AUNQUE LA COLUMNA ESTE OCUPADA
        if b[i][j]<precio and check_columna(x,j)==0:
            #si el precio de esa ciudad es mejor y la columna esta vacía, entro
            precio=b[i][j] #actualizo el mejor caso
            aux=j#guardo la j(ciudad) del mejor caso
    while check_columna(x,aux)==1:
        #chequeo que la solución obtenida es buena. Si no lo es, pruebo con la siguiente ciudad
        #hasta encontrar la primer ciudad vacía
        if aux==len(x):
            aux=0
        aux+=1

    return aux

def costo_camino(b,x):
    #calcula el costo de un camino
    n=len(x)
    costo=0
    for i in range(0,n):
        for j in range(0,n):
            #busco los "1" en la matriz de asignación
            if x[i][j]==1:
                #si encuentro un 1 tomo el "I" y el "j" y los ingreso en la matriz de costo
                #la cual contiene el costo de ir a esa ciudad
                costo=costo+b[i][j]
    return costo

def check_columna(x,j):
    #checkeo si hay otros terminators en la columna
    for i in range(0,len(x)):
        if x[i][j]==1:
            return 1
    return 0

def busco_ocupadas(x,i):
    for a in range(0,len(x)):
        if x[a][i]==1:
            return 1
    return 0

def asigno_city(b,x):
    #asigna las ciudades
    n=len(x)
    for i in range(0,n):
        aux=busco_mejor(b,x,i)
        x[i][aux]=1
    return x

def imprimirMAT(matriz,m,n):
    #imprime una matriz
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
x=asigno_city(b,x)
aux=costo_camino(b,x)
print("Recorrido:")
imprimirMAT(x,n,n)
print("Costo del camino:",aux)