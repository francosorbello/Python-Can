#DEFINIR "hash_table={}" EN EL MAIN

def hash_insert(pos,producto,tabla):
  tabla[producto]=pos
  return hash_table

def hash_search(producto,tabla):
  return tabla[producto]

def hash_delete(producto,tabla):
  del tabla[producto]
  return tabla
