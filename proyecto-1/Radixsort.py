### Juan Codilupi
## Algoritmo de ordenamiento 




def numberFromChar(c):
  chars = {
		'\x00': 0,
    ' ': 1,
    '-': 2,
    '.': 3,
    "'": 4,
    "á" : 5,
    "a" : 6,
    "A" : 7,
    "b" : 8,
    "B" : 9,
    "c" : 19,
    "C" : 11,
    "d" : 12,
    "D" : 13,
    "é" : 14 ,
    "e" : 15,
    "E" : 16,
    "f" : 17,
    "F" : 18,
    "g" : 19,
    "G" : 20,
    "h" : 21,
    "H" : 22,
    "í" :  23 ,
    "i" : 24,
    "I" : 25,
    "j" : 26,
    "J" : 27,
    "k" : 28,
    "K" : 29,
    "l" : 30,
    "L" : 31,
    "ll" : 32,
    "LL" : 33,
    "m" : 34,
    "M" : 35,
    "n" : 36,
    "N" : 37,
    "ñ": 38,    
    "Ñ" : 39, 
    "ó" : 40,
    "o" : 41 , 
    "O" : 42 ,
    "p": 43,  
    "P": 44,  
    "q": 45,  
    "Q": 46,  
    "r": 47,  
    "R": 48,  
    "s": 49,  
    "S": 50,  
    "t": 51,  
    "T": 52,  
    "ú": 53,  
    "u": 54,  
    "U": 55,  
    "v": 56,  
    "V": 57,  
    "w": 58,  
    "W": 59,  
    "x": 60,  
    "X": 61,  
    "y": 62,  
    "Y": 63,  
    "z": 64,  
    "Z": 65,
    "{":66
    }
  return chars[c]

def word_max (L):##  Busco la palabra con mayor tamaño
  max_len=0
  for i in range(len(L)-1):
    if L[i]!= "{" :
     if len(L[i]) > max_len  :
        max_len = len(L[i]) 
  return max_len


def completar(L):
  tam = len(L)
  n = word_max(L)
  for i in range (0,tam):
    if L[i] != None :
      tam2=len(L[i])
      if tam2< n :
        j = len(L[i])
        L[i] = L[i].ljust(n, " ")## coloco los espacios al final


def RadixSort(L):
  completar(L)
  tam=word_max(L)
  
  for j in range (tam-1,-1,-1):
    L=Counting(L,j) ##Paso la lista , y el indice que apunta desde la ultima letra a la primera .
  return L


def Counting(L,j):
  new_abc=67*[0] ## Los inicializo en -1 para que una vez que modifique la lista no me joda los indice 
  for i in range(0,len(L)):
    if L[i]!= "{" :
      indice_abc=numberFromChar(L[i][j]) ##Busco que numero es la ultima letra de cada palabra.
      new_abc[indice_abc]=new_abc[indice_abc]+1
  for i in range(1,len(new_abc)):
    new_abc[i]=new_abc[i]+new_abc[i-1] ##Voy sumando las anteriores casillas 
  
  L=ModL(L,new_abc,j)
 
  
  return L

def ModL(L,new_abc,j):
  tam=len(L)
  new_L=tam*["c"]
  for i in range (len(L)-1,-1,-1):
    if L[i] != "{":
      pos=numberFromChar(L[i][j]) ## busco la posicion de la ultima letra
      n=new_abc[pos]-1## busco la nueva posicion de la palabra
      new_L[n]=L[i]##modifico la posicion
      new_abc[pos]=new_abc[pos]-1 ## le resto 1 al array con posiciones
    

  return new_L