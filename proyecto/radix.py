def numberFromChar(c):
  
  chars = {
    '\x00': 0,
    ' ': 1,
    '-': 2,
    '.': 3,
    "'": 4,
    'a': 5,
    'á': 6,
    "A":6.5,
    'b': 7,
    "B":7.5,
    'c': 8,
    "C":8.5,
    'd': 9,
    "D":9.5,
    'e': 10,
    'é': 11,
    "E":11.5,
    'f': 12,
    "F":12.5,
    'g': 13,
    "G":13.5,
    'h': 14,
    "H":14.5,
    'i': 15,
    'í': 16,
    "I":16.5,
    'j': 17,
    "J":17.5,
    'k': 18,
    "K":18.5,
    'l': 19,
    "L":19.5,
    'm': 20,
    "M":20.5,
    'n': 21,
    "N":21.5,
    'o': 22,
    'ó': 23,
    "O":23.5,
    'p': 24,
    "P":24.5,
    'q': 25,
    "Q":25.5,
    'r': 26,
    "R":26.5,
    's': 27,
    "S":27.5,
    't': 28,
    "T":28.5,
    'u': 29,
    'ú': 30,
    "U":30.5,
    'v': 31,
    "V":31.5,
    'w': 32,
    "W":32.5,
    'x': 33,
    "X":33.5,
    'y': 34,
    "Y":34.5,
    'z': 35,
    "Z":35.5
  }
  return chars[c]
def radixsort(mylist):
  
  if len(mylist) == 0:
      return
  digits = len(mylist[0])

  # busco las letras que decodificadas son el entero mas grande y
  # el mas chico, para saber cuantos buckets armar
  first_char = numberFromChar(mylist[0][0])
  last_char = numberFromChar(mylist[0][0])
  for word in mylist:
      for letter in word:
          if numberFromChar(letter) < first_char:
              first_char = numberFromChar(letter)
          if numberFromChar(letter) > last_char:
              last_char = numberFromChar(letter)
  # relleno con una letra de relleno
  fill_char = chr(0)
  
  # busco la palabra mas grande, para saber cuantas iteraciones hacer
  for w in mylist:
      if len(w) > digits:
          digits = len(w)

  # agrego la letra de relleno a las palabras cortas
  for index, w in enumerate(mylist):
      mylist[index] = w.ljust(digits, fill_char)

  # itero en forma reversa, una vez por cada posición
  for d in range(digits - 1, -1, -1):
      # creo un bucket
      bucket = {}
      for i in range(numberFromChar(fill_char), last_char + 1):
          bucket[i] = []
      # agrego los elementos al bucket según el digito
      for el in mylist:
          digit = numberFromChar(el[d])
          bucket[digit].append(el)
      
      # limpio la lista
      mylist = []
      # y agrego los elementos conservando el orden, dado por el bucket
      for key in bucket:
          for el in bucket[key]:
              mylist.append(el)
  for index, w in enumerate(mylist):
      mylist[index] = mylist[index].replace(fill_char, "")
  return mylist