from algo1 import *

def length(array):
    aux=len(array)
    count=0
    for a in range(0,aux):
        if array[a] != None:
            count=count+1
    return count

dim=input_int("Ingrese dimensión: ")
array=Array(dim,None)

for a in range(0,dim):
  array[a]=input_int("Ingrese valores vector: ")

print(array)

dfad=length(array)
print("largo:",dfad)