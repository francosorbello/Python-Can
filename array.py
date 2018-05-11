from algo1 import *

def search(array,element):
  aux=-1
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
      for a in range(len(array)-1,index,-1):
        array[a]=array[a-1]
      array[index]=element
  else:
    return None
  
def delete(array,element):
  pos=search(array,element)
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
    insert(array,element,0)

def dequeue(array):
    count=length(array)
    if count>0:
        aux=array[0]
        delete(array,aux)
        return aux
    else:
        return None
        
def push(array,element):
    index=len(array)-1
    insert(array,element,index)
    
def pop(array):
    count=length(array)
    if count != 0:
        index=len(array)-1
        aux=array[index]
        delete(array,index)
        return aux
    else:
        return None

