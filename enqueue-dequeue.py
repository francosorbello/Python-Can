from algo1 import *

def length(array):
    aux=len(array)
    count=0
    for a in range(0,aux):
        if array[a] != None:
            count=count+1
    return count

def delete(array,i):
  array[i]=None
  for j in range(i,len(array)-1):
    array[j]=array[j+1]
    array[j+1]=None

def insert(array,element,index):
  for a in range(len(array)-1,index,-1):
    array[a]=array[a-1]
  array[index]=element

def enqueue(array,element):
    index=len(array)-1 #ultima pos del vector
    aux=0 #si el vector esta lleno entra en la primera posicion
    for a in range(0,index):
        if array[a]==None: #busco espacios vacios para insertar
            aux=a
            break
    insert(array,element,aux)

def dequeue(array):
    count=length(array)
    if count>0:
        aux=array[0]
        delete(array,aux)
        return aux
    else:
        return None

dim=input_int(("Ingrese dimensión: "))
array=Array(dim,0)

for a in range(0,dim):
  array[a]=input_int(("Ingrese valores vector: "))
  
print(array)
print("Enqueue:")
enqueue(array,2)
print(array)
print("Dequeue")
eso=dequeue(array)
enqueue(array,2)
print(eso)


