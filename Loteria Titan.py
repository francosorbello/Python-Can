from quicksort import *    

def busco_mayor(lista):
    n=len(lista)
    max=lista[0]
    for i in range(1,n):
        if lista[i].repetido >max.repetido:
            max=lista[i]
    return max


def imprimirNRO(lista):
    for i in range(0,len(lista)):
        #print('[',end='')
        print("[",lista[i].nro,",",lista[i].repetido,end=']')
    print("")

def repetidos(A):
    #como tengo la lista ordenada, para contar saco los elementos de la cabeza hasta que este cambia
    #y luego los guardo en otra lista. Repito hasta vaciar la lista.
    lista_repetidos=[]#esta lista contiene los numeros y la cantidad de repeticiones
    aux=numero()
    aux.nro=A[0]
    j=0
    while A[0]<A[len(A)-1]:
        #mientras no esté en el ultimo elemento, itero
        aux.repetido=0
        while A[0]==aux.nro:
            #cada vez que encuentro un repetido, sumo 1 al contador y extraigo el elemento de la lista
            aux.repetido+=1
            A.pop(0)
        #guardo la cant. de repeticiones en una lista
        list.append(lista_repetidos,aux)
        #creo un nuevo "numero"
        aux=numero()
        aux.nro=A[0]#ahora mi nuevo numero es el primero de la lista
    #para evitar errores, busco los repetidos del ultimo numero cuando es el unico que queda en la lista
    aux=numero()
    aux.nro=A[0]
    aux.repetido=len(A)
    list.append(lista_repetidos,aux)    
    return lista_repetidos 

class numero:
    nro=None #acá guardo el numero
    repetido=None #acá guardo la cantidad de veces que se repite

nro1=[15,1,7,2,17,10,1,4,15,3,8,3,4,6,4,11,5,9,5,1,5,9,10,8,2,4,3,1,6,8,8,9,18,4,10,6]
print(nro1)
print("Lista ordenada:")
quick_sort(nro1,0,len(nro1)-1)
print(nro1)
print("Repetidos:")
print("[","numero",",","repeticiones","]")
l=repetidos(nro1)
imprimirNRO(l)
mas_rep=busco_mayor(l)
print("El número que más se repite es:",mas_rep.nro)