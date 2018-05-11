from libreriafinal import *
from algo1 import *

def checkprimos(aux,n):
    if aux==n: #aux es el ultimo primo que encuentro y n es el numero ingresado
        print("El número ingresado es primo.")
        return
    else:
        print("El número ingresado no es primo. El más cercano es:",aux,".")
        return

def buscoprimos(l,n):
    primo=2 #el primer primo es el 2
    aux=0 #esta variable controla que la matriz sea dif de 0
    largo=lengthLIST(l)
    while largo>1: #el ultimo elemento en quedar va a ser el último primo,por eso el bucle es hasta 1
        node=l.head
        while node != None:
            if node.value%primo==0: 
                deleteLIST(l,node.value) #borro los múltiplos del primo actual
            node=node.nextNode
        primo=l.head.value #el siguiente primo queda en la cabeza
        largo=lengthLIST(l)
    return l.head.value #retorno el ultimo primo que queda
    
def rellenolista(l,n):
    #relleno la lista con todos los números que hay hasta el ingresado. Ej: si n=5, la lista= 1,2,3,4,5
    for a in range(1,n+1):
        appendLIST(l,a)
    l.head.value=0 #cambio el primer valor a 0 para evitar problemas

class node:
  value=None
  nextNode=None

class LinkedList:
  head=None

L=LinkedList()

n=input_int("Inserte número:")
rellenolista(L,n)
imprimirLIST(L)
print("--")
aux=buscoprimos(L,n)#usando la criba de eratostenes, busco todos los primos hasta el numero ingresado
checkprimos(aux,n) #busco el n ingresado en la lista. Si está, es primo.

