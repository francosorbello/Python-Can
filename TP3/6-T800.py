from algo1 import *
from random import randint

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

def repetido(lista):
    #busca elementos repetidos en una lista
    n=len(lista)
    for i in range(0,n):
        for j in range(0,n):
            if lista[i]==lista[j] and i!=j:
                return True
            if lista[j]==(j+1):
                #tambien busca volver a ciudades anteriores. 
                #Ej:si A=[0,2,1,3], la pos 1,2 es igual a la 2,1.
                return True
    return False

def suma_elementos(lista,mat_costos):
    #suma elementos de la matriz para calcular el costo del camino ingresado.
    aux=0
    for i in range(0,len(mat_costos)):
        a=i
        b=lista[a]
        aux=aux+mat_costos[a][b]
    return aux

def prometedor (A,k,mat_costos,costo):
#Precondición A ya es k-1  prometedor
    for j in range (0,k):
        if repetido(A)==True or suma_elementos(A,mat_costos)>costo or suma_elementos(A,mat_costos)==0:
            return False
    return True

def camino(ciudades,k,n,mat_costos,costo):
    costo=suma_elementos(ciudades,mat_costos)
    #print(ciudades)
    if k == n:
        if prometedor(ciudades,k,mat_costos,costo):
            print (ciudades)
            print("costo:",costo)
        else: 
            return
    else:     
        for j in range (0,n):
            ciudades[k]=j
            camino(ciudades,k+1,n,mat_costos,costo)

n=4
mat_costos=Array(n,Array(n,0)) #matriz de costos
relleno_matriz(mat_costos,n,20)
imprimirMAT(mat_costos,4,4)
ciudades = 4*[0]
#El contenido de cada nodo del vector representa la columna de la matriz de costos. La fila está daad
#por la posicion de ese nodo.Ej:[0,1,3,2]indica el camino m0,0 - m1,1 - m2,3 - m3,2
camino(ciudades,0,4,mat_costos,costo=0)



    
    