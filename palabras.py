from algo1 import *
from libreriafinal import *

def imprimir(L):
    node=L.head
    while node!=None:
        imprimirLIST(node.value)
        node=node.nextNode

def comparoyordeno(pal1,pal2,bigL):
    if pal1.value>pal2.value:
        aux=bigL.value
        bigL.value=bigL.nextNode.value
        bigL.nextNode.value=aux
        return 
    if pal1.value==pal2.value and pal1.nextNode != None and pal2.nextNode != None:#pal1/2.nextNode != None se asegura que no haya problemas si las palabras son iguales.
        comparoyordeno(pal1.nextNode,pal2.nextNode,bigL)#si son la misma letra, vuelvo a llamar a la funcion con los siguientes nodos
    return
            
def ordeno(Lwords):
    wordnodeaux=Lwords.head
    while wordnodeaux !=None:
        wordnode=Lwords.head
        while wordnode.nextNode != None:
            l1=wordnode.value#accedo a la lista del nodo
            l2=wordnode.nextNode.value#accedo a la lista del nodo siguiente
            pal1=l1.head
            pal2=l2.head
            comparoyordeno(pal1,pal2,wordnode)
            wordnode=wordnode.nextNode
        wordnodeaux=wordnodeaux.nextNode
            
class node:
    value=None
    nextNode=None
class LinkedList:
    head=None
   
Lwords=LinkedList()#esta lista guarda las otras listas   
   
word1=LinkedList()
appendLIST(word1,"h")
appendLIST(word1,"o")
appendLIST(word1,"l")
appendLIST(word1,"a")
appendLIST(word1,"a")
imprimirLIST(word1)
#--#
word2=LinkedList()
appendLIST(word2,"p")
appendLIST(word2,"e")
appendLIST(word2,"d")
appendLIST(word2,"r")
appendLIST(word2,"o")
imprimirLIST(word2)
#--#
word3=LinkedList()
appendLIST(word3,"h")
appendLIST(word3,"e")
appendLIST(word3,"l")
appendLIST(word3,"l")
appendLIST(word3,"o")
imprimirLIST(word3)
#--#
word4=LinkedList()
appendLIST(word4,"c")
appendLIST(word4,"o")
appendLIST(word4,"m")
appendLIST(word4,"o")
imprimirLIST(word4)
#--#
word5=LinkedList()
appendLIST(word5,"e")
appendLIST(word5,"s")
appendLIST(word5,"t")
appendLIST(word5,"a")
appendLIST(word5,"s")
imprimirLIST(word5)
#--#
word6=LinkedList()
appendLIST(word6,"h")
appendLIST(word6,"a")
appendLIST(word6,"r")
appendLIST(word6,"p")
appendLIST(word6,"o")
imprimirLIST(word6)

#--#
word7=LinkedList()
appendLIST(word7,"a")
appendLIST(word7,"l")
appendLIST(word7,"g")
appendLIST(word7,"o")
imprimirLIST(word7)
#--#
word8=LinkedList()
appendLIST(word8,"l")
appendLIST(word8,"c")
appendLIST(word8,"c")
imprimirLIST(word8)
#--#
word9=LinkedList()
appendLIST(word9,"h")
appendLIST(word9,"o")
appendLIST(word9,"l")
appendLIST(word9,"i")
appendLIST(word9,"t")
appendLIST(word9,"a")
imprimirLIST(word9)
#--#
word10=LinkedList()
appendLIST(word10,"h")
appendLIST(word10,"o")
appendLIST(word10,"l")
appendLIST(word10,"o")
appendLIST(word10,"t")
appendLIST(word10,"i")
appendLIST(word10,"t")
appendLIST(word10,"a")
imprimirLIST(word10)
#--#
word11=LinkedList()
appendLIST(word11,"h")
appendLIST(word11,"o")
appendLIST(word11,"l")
appendLIST(word11,"a")
imprimirLIST(word11)

#Agrego las listas a otra lista
appendLIST(Lwords,word1)
appendLIST(Lwords,word2)
appendLIST(Lwords,word3)
appendLIST(Lwords,word4)
appendLIST(Lwords,word5)
appendLIST(Lwords,word6)
appendLIST(Lwords,word7)
appendLIST(Lwords,word8)
appendLIST(Lwords,word9)
appendLIST(Lwords,word10)
appendLIST(Lwords,word11)
print("----")
ordeno(Lwords)
print("Lista ordenada:")
imprimir(Lwords)