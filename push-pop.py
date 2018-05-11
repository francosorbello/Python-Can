from algo1 import *

def insert(array,element,index):
  count=length(array)
  if count !=0:
    aux=len(array)
    if index>aux:
      return None
    else:
      if array[index]==None:
          array[index]=element
      else:
          for a in range(len(array)-1,index,-1):
            array[a]=array[a-1]
          array[index]=element
  else:
    return None

def length(array):
    aux=len(array)
    count=0
    for a in range(0,aux):
        if array[a] != None:
            count=count+1
    return count

def deletetrucho(array,i):
    array[i]=None

def delete(array,i):
  array[i]=None
  for j in range(i,len(array)-1):
    array[j]=array[j+1]
    array[j+1]=None

def push(array,element):
    index=len(array)-1 #ultima pos del vector
    aux=index #si el vector no está vacio inserta en la ultima pos
    for a in range(0,index):
        if array[a]==None: #busco espacios vacios para insertar
            aux=a
            break
    insert(array,element,aux)
    
def pop(array):
    count=length(array)
    if count != 0:
        index=len(array)-1
        for a in range(index,1,-1):
            if array[a] != None:
                aux=a #guardo primera pos distina de 0
                break
        borro=array[aux]
        delete(array,borro)
        return borro
    else:
        return None

dim=input_int(("Ingrese dimensión: "))
array=Array(dim,0)

for a in range(0,dim):
  array[a]=input_int(("Ingrese valores vector: "))
  
deletetrucho(array,1)
print(array)
print("push:")
push(array,5)
print(array)
push(array,6)
print(array)
print("pop")
eso=pop(array)
print(array)
print("Elemento sacado: ",eso)