from libreriafinal import *
from algo1 import *

def checkprimos(primo,naux):
    if primo==naux:
        print("El número ingresado es primo.")
        return
    else:
        print("El número ingresado no es primo. El más cercano es:",primo,".")
        return

def buscocero(matriz,m,colum):
    #cuento la cantidad de 0 en la matriz y devuelvo ese numero. Esto sirve para asegurarse que matriz !=0
    aux=0
    for a in range(0,m):
        for b in range(0,colum):
            if matriz[a][b]==0:
                aux=aux+1
    return aux

def imprimirmat(m,n,naux):
	for i in range(0,n):
		print('[ ',end='')
		for j in range(0,naux):
			print(m[i][j],'',end='')
		print(']')

def sigprimo(matriz,n,colum,comparo):
    for i in range(0,n):
        for j in range(0,colum):
            if matriz[i][j]==comparo:
                matriz[i][j]=0
            if matriz[i][j] !=0:
                comparo=matriz[i][j]
                return comparo
    return comparo

def buscoprimos(matriz,n,colum):
    comparo=2
    aux=0 #esta variable controla que la matriz sea dif de 0
    while aux<n*colum: #se loopea mientras la matriz sea != de 0
        for i in range(0,n):
            for j in range(0,colum):
                if matriz[i][j] != comparo and matriz[i][j]%comparo==0: #cambio los múltiplos de cada primo por 0.
                    matriz[i][j]=0 #cambio los multiplos del primo por 0
        comparo=sigprimo(matriz,n,colum,comparo)
        aux=buscocero(matriz,n,colum)
    return comparo
            
def rellenomatriz(matriz,n,colum,naux):
    #esta función rellena la matriz con los números de 1 a n
    aux=0
    for i in range(0,n):
        for j in range(0,colum):
            aux=aux+1
            if aux>naux:
                matriz[i][j]=0
            else:
                matriz[i][j]=aux
    matriz[0][0]=0 #cambio el 1 por un 0 para evitar problemas

#defino el tamaño de la matriz
n=input_int("Inserte número:")
if n==1 or n==0:
    print("El número no es primo.")
else:
    if n<10:
        naux=n
        colum=n #colum son las columnas de la matriz
        n=1 #n son las filas de la matriz
    else:
        naux=n
        if n%2!=0: #si el
            n=n//10+1
        else:
            n=n//10
        colum=10
    matriz=Array(n,Array(colum,0))
    rellenomatriz(matriz,n,colum,naux)
    #imprimirmat(matriz,n,colum)
    print("--")
    primo=buscoprimos(matriz,n,colum)#usando la criba de eratostenes, busco todos los primos hasta el numero ingresado
    checkprimos(primo,naux) #busco el n ingresado en la lista. Si está, es primo.
