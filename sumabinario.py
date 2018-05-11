from algo1 import *
from libreriafinal import *

def invierto(l):
    #esta función invierte un lista. Ej: [1,2,3,4] pasa a ser [4,3,2,1]
    largo=lengthLIST(l)
    lswap=LinkedList() #guardo la lista invertida en una nueva lista
    node=l.head
    for a in range(0,largo):
        aux=pop(l)
        appendLIST(lswap,aux)
    return lswap

def imprimirnew(caracteres,l):
    node=l.head
    while node != None:
        print(caracteres[node.value],end="")
        node=node.nextNode
    print("")

def dividir(dividendo,l,resto=0):
    if dividendo==0:
        return 
    else:
        nuevodividendo=dividendo//2
        resto=dividendo%2
        addLIST(l,resto)
        return dividir(nuevodividendo,l,resto)
    
class node:
    value=None
    nextNode=None

class LinkedList:
    head=None

charbinario=[0,1]

L1=LinkedList()
#ingreso los valores a sumar y los cambio a binario
dividendo=input_int("Ingrese número en base decimal:")
dividir(dividendo,L1)
imprimirnew(charbinario,L1)
L1inv=invierto(L1) #invierto la lista y la guardo en una nueva para facilitar la suma
print("Lista invertida")
imprimirLIST(L1inv)

L2=LinkedList()
#ingreso los valores a sumar y los cambio a binario
dividendo=input_int("Ingrese segundo número en base decimal:")
dividir(dividendo,L2)
imprimirnew(charbinario,L2)
L2inv=invierto(L2) #invierto la lista y la guardo en una nueva para facilitar la suma
print("Lista 2 invertida:")
imprimirLIST(L2inv)

