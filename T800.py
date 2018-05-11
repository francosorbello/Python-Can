from algo1 import *
from random import randint
from libreriafinal import *

global costo

def prometedor(matriz,costo,i,j):
    if matriz[i][j]>costo:
        return False
    return True

def camino(matriz,n):
    costo=0
    for i in range(0,n):
        for j in range(0,n):
            if prometedor(matriz,costo,i,j):
                costo=costo+matriz[i][j]

def imprimirMAT(matriz,m,n):
    for i in range(0,m):
        for j in range(0,n):
            #print('[',end='')
            print("[",matriz[i][j],end=']')
        print("")
def relleno_matriz(matriz,n,rand):
    #genero una matriz diagonal. Viajar de 0 a 1 es lo mismo que de 1 a 0
    for a in range(0,n):
        for b in range(0,n):
            if b==a:
                matriz[a][b]=0
            else:
                aux=randint(0,rand)
                matriz[a][b]=aux
                matriz[b][a]=aux

n=4
ciudades=Array(n,Array(n,0)) #matriz de costos
relleno_matriz(ciudades,n,20)
imprimirMAT(ciudades,n,n)

