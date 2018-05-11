from libreriafinal import *
def subList(L,startpos,endpos):
    newL=LinkedList()
    cn=L.head
    for i in range(0,startpos):
        cn=cn.nextNode
    addLIST(newL,cn.value)
        
    for i in range(startpos+1,endpos+1):
        cn=cn.nextNode
        insertLIST(newL,cn.value,lengthLIST(newL))
    return newL

def mergeSort(L):
    print("Splitting:")
    imprimirLIST(L)
    if lengthLIST(L)>1:
        mid = lengthLIST(L)//2
        lefthalf = subList(L,0,mid-1)
        righthalf = subList(L,mid,lengthLIST(L)-1)
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(L,lefthalf,righthalf)
    print("Merging:")
    print("--")
    imprimirLIST(L)

def merge(L,lefthalf,righthalf):
        """ Mezcla dos listas de a un elemento de la cada lista a la vez.
        """
        i=0 #indice de elementos para la lista lefthalf
        j=0 #indice de elementos para la lista righthalf
        Lindex=0 #indice de elementos de la lista a ordenar
        while i < lengthLIST(lefthalf) and j < lengthLIST(righthalf):
            if accessLIST(lefthalf,i) < accessLIST(righthalf,j):
                updateLIST(L,accessLIST(lefthalf,i),Lindex)
                i=i+1
            else:
                updateLIST(L,accessLIST(righthalf,j),Lindex)
                j=j+1
            Lindex=Lindex+1

        while i < lengthLIST(lefthalf):
            updateLIST(L,accessLIST(lefthalf,i),Lindex)
            i=i+1
            Lindex=Lindex+1

        while j < lengthLIST(righthalf):
            updateLIST(L,accessLIST(righthalf,j),Lindex)
            j=j+1
            Lindex=Lindex+1

class node:
    value=None
    nextNode=None

class LinkedList:
    head=None

L=LinkedList()
bt=Btree()

appendLIST(L,38)
appendLIST(L,27)
appendLIST(L,43)
appendLIST(L,3)
appendLIST(L,9)
appendLIST(L,82)
appendLIST(L,10)
appendLIST(L,12)
mergeSort(L)