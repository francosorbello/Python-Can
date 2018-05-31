from quicksort import *    

def mejores(lista):
    lista_mejores=[]
    for a in range(0,6):
        #busco el mejor de la lista 6 veces
        lista_mejores.append(busco_mayor(lista))
    return lista_mejores

def busco_mayor(lista):
    n=len(lista)
    max=lista[0]
    for i in range(1,n):
        if lista[i].repetido >max.repetido:
            max=lista[i]
            aux=i#guardo la posicion del elemento maximo
    lista.pop(aux)#quito el elemento maximo de la lista
    return max

def imprimirNRO(lista):
    print("[","numero",",","repeticiones","]")
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

num_loteria=[15,19,24,27,42,51,1,2,16,27,36,38,7,12,13,30,33,38,2,5,12,26,31,43,17,20,24,28,49,53,10,14,27,32,45,49,1,2,5,29,35,36,4,16,24,35,49,53,15,18,28,31,33,51,3,11,12,34,40,51,8,16,26,27,44,51,3,13,15,22,27,38,4,6,16,34,38,39,6,9,19,37,39,51,4,25,26,38,48,49,11,15,16,30,31,50,5,15,27,32,36,46,9,16,25,32,41,44,5,14,23,32,42,52,1,5,18,39,45,52,5,9,32,35,51,54,9,15,17,35,39,44,10,11,13,22,26,46,8,19,22,29,50,52,2,3,15,22,34,39,4,15,35,40,44,50,3,12,24,29,38,50,1,12,17,31,34,40,6,9,12,17,20,23,8,16,34,43,45,53,8,12,24,25,47,54,9,16,19,33,40,46,18,19,34,37,40,49,4,5,15,17,28,54,10,11,30,32,38,44,6,8,21,33,34,47]
print(num_loteria)
print("Lista ordenada:")
quick_sort(num_loteria,0,len(num_loteria)-1)
print(num_loteria)
print("Repetidos:")
l=repetidos(num_loteria)
imprimirNRO(l)
print("Los que más se repiten son:")
mejores_nros=mejores(l)
imprimirNRO(mejores_nros)




#MEJORA:BUCKETSORT