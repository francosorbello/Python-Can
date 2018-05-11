from libreriafinal import *
from algo1 import *

def agregoalista(array,L):
    auxarray=Array(len(array),0)
    for a in range(0,len(array)):
        auxarray[a]=array[a]
    appendLIST(L,auxarray)

def checkmovimiento(array,L):
    for x in range(0,8):
        comparo=array[x]
        for y in range(0,8):
            print(array[y])
            #checkeo en vertical
            if array[y]==comparo and y != x:
                print("Movimiento incorrecto1")
                aux= False #si esta var es distinta de falso luego guarda las posiciones
            #checkeo en vertical hacia abajo
                return
            if abs(comparo-x)==abs(array[y]-y) and y != x:  #dado que el diagonal de aij es a(i+x)(j+k), si los resto y da lo mismo entonces es diagonal
                print("Movimiento incorrecto2")
                aux= False #si esta var es distinta de falso luego guarda las posiciones
                return
            #checkeo en vertical hacia arriba
            if comparo+x==array[y]+y and y != x:  #dado que el diagonal de aij es a(i+x)(j+k), si los resto y da lo mismo entonces es diagonal
                print("Movimiento incorrecto3")
                aux= False #si esta var es distinta de falso luego guarda las posiciones
    if aux != False: #si el array no tuvo problemas, lo agrego a una lista.
        agegoalista(array,L)

class node:
  value=None
  nextNode=None

class linkedList:
  head=None

L=linkedList()

test=Array(8,0)
aux=input_int("1. Vertical | 2. Diagonal hacia abajo | 3.Diagonal hacia arriba: ")
if aux==1:
    test[0]=1
    test[1]=2
    test[2]=2
    test[3]=4
    test[4]=4
    test[5]=3
    test[6]=8
    test[7]=2
    checkmovimiento(test,L)
elif aux==2:
    test[0]=7
    test[1]=1
    test[2]=2
    test[3]=4
    test[4]=6
    test[5]=3
    test[6]=8
    test[7]=5 