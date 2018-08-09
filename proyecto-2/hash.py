def hash_insert(pos,producto,tabla):
  tabla[producto]=pos
  return tabla

def hash_search(producto,tabla):
  if tabla.get(producto)==None:
      print("El producto que busca no se encuentra en el almacén.")
      return None
  return tabla[producto]

def hash_delete(producto,tabla):
  if tabla.get(producto)==None:
      print("El producto que busca no se encuentra en el almacén.")
      return None
  del tabla[producto]
  return tabla