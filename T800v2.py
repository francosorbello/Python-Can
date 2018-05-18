# -*- coding: utf-8 -*-

global costo
costo = 0

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
    for i in range(1,n):
        for j in range(1,n):
            if lista[i]==lista[j] and i!=j:
                return True
    return False

def suma_elementos(lista,mat_costos):
    #suma elementos de la matriz para calcular el costo del camino ingresado.
    aux=0
    for i in range(0,len(mat_costos)):
        for j in range(0,len(mat_costos)):
            a=i+1
            b=lista[a]
            aux=aux+mat_costos[a][b]
    return aux

def prometedor (A,k,mat_costos):
#Precondición A ya es k-1  prometedor
    for j in range (1,k):
        if repetido(A)==True or suma_elementos(A,mat_costos)>costo:
            return False
    return True


def camino(ciudades,k,n,mat_costos):
    global costo
    costo = costo + 1
    if k == n:
        if prometedor(ciudades,k,mat_costos):
            print (ciudades)
        else: 
            return
    else:
        for j in range (1,n+1):
            if prometedor (ciudades,k,mat_costos):
                ciudades[k+1]=j
                camino(ciudades,k+1,n)

n=4
mat_costos=Array(n,Array(n,0)) #matriz de costos
relleno_matriz(mat_costos,n,20)     
ciudades = 5*[0]
#el primer elemento del array representa la ciudad de donde empiezo. Por ej, si el primer elemento es 
#0 significa que empiezo en la primer ciudad
#El contenido de cada nodo del vector representa la columna de la matriz de costos. La fila está dada
#por la posicion de ese nodo.Ej:[0,0,1,3,2]indica el camino m0,1-m
camino(ciudades,0,4,mat_costos)
print (costo)


    
    