from algo1 import *

def search(array,element):
  aux=None
  for i in range(0,len(array)):
    if array[i]==element:
      aux=i
      break
  return aux
  
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
  
def delete(array,element):
  pos=search(array,element)
  if pos == None:
      return pos
  else:
      array[pos]=None
      for j in range(pos,len(array)-1):
        array[j]=array[j+1]
        array[j+1]=None

def length(array):
    aux=len(array)
    count=0
    for a in range(0,aux):
        if array[a] != None:
            count=count+1
    return count
    
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
        
def push(array,element):
    count=length(array)
    if count !=0:
        index=len(array)-1 #ultima pos del vector
        aux=index #si el vector no está vacio inserta en la ultima pos
        for a in range(0,index):
            if array[a]==None: #busco espacios vacios para insertar
                aux=a
                break
        insert(array,element,aux)
    else:
        array[0]=element
    
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



