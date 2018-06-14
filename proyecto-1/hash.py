def hash_insert(pos,producto,tabla):
  tabla[producto]=pos
  return hash_table

def hash_search(producto,tabla):
  if tabla.get(producto)==None:
      print("El producto que busca no se encuentra en el almacén.")
      return
  return tabla[producto]

def hash_delete(producto,tabla):
  if tabla.get(producto)==None:
      print("El producto que busca no se encuentra en el almacén.")
      return
  del tabla[producto]
  return tabla
