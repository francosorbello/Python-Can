from algo1 import *
from libreriafinal import *

def imprimirnew(caracteres,l):
    node=l.head
    while node != None:
        print(caracteres[node.value],end="")
        node=node.nextNode

def dividir(dividendo,base,resto=0):
    if dividendo==0:
        return 
    else:
        nuevodividendo=dividendo//base
        resto=dividendo%base
        addLIST(l,resto)
        return dividir(nuevodividendo,base,resto)
    
    
charhexadecimal=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
charoctal=["0","1","2","3","4","5","6","7"]

class node:
    value=None
    nextNode=None

class LinkedList:
    head=None

l=LinkedList()
dividendo=input_int("Ingrese número en base decimal:")
aux=input_int("1. Cambiar a base hexadecimal. | 2. Cambiar a base octal:")
if aux==1:
    dividir(dividendo,16)
    imprimirnew(charhexadecimal,l)
elif aux==2:
    dividir(dividendo,8)
    imprimirnew(charoctal,l)
else:
    print("Número incorrecto, ingrese 1 o 2.")