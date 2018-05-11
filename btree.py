# Unittest sobre Btree
# Algoritmos y estructuras de datos I

import unittest
from algo1 import *
from arboless import Btree, insert, search, access, delete

class TestBtree(unittest.TestCase):
	def setUp(self):
		pass

	def test_insert_first_element(self):
		""" Insertar un solo elemento en un arbol vacio y verificar su valor
		"""
		bt=Btree()
		insert(bt,1,'comienzo')
		#print()
		#print('valor root',bt.root.key,'contenido:',access(bt,bt.root.key))
		#print()
		
		self.assertEqual(access(bt,bt.root.key),"comienzo")

	def test_insert_element_check_order(self):
		""" Insertar un elemento en un arbol y verificar su posicion
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	
		keys=[10,5,20,8,13,18,22,2,9,40,21,11,7,3,1]
		bt=Btree()
		for a in range(0,15):
		    insert(bt,keys[a],strings[a])
		#print()
		#print(bt.root.rightnode.rightnode.leftnode.key,access(bt,bt.root.rightnode.rightnode.leftnode.key))
		self.assertEqual(access(bt,bt.root.rightnode.rightnode.leftnode.key),"b")

	def test_delete_leaf_check_order(self):
		""" Borrar una rama de un arbol y verificar la posicion del elemento eliminado
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20,8,13,22]
		bt=Btree()
		for a in range(0,6):
		    insert(bt,keys[a],strings[a])
		delete(bt,5)
		#print()
		#print(bt.root.leftnode.key,access(bt,bt.root.leftnode.key))
		#print()
		self.assertEqual(bt.root.leftnode.key,8)

	def test_delete_element(self):
		""" Borrar una hoja de un arbol y verificar la posicion inexistente
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20,8,13,22]
		bt=Btree()
		for a in range(0,6):
		    insert(bt,keys[a],strings[a])
		delete(bt,5)
		#print()
		#print(bt.root.leftnode.key,access(bt,bt.root.leftnode.key))
		#print()
		res=access(bt,5)
		self.assertEqual(res,None)

	def test_delete_inexistent_element(self):
		""" Borrar una hoja inexistente de un arbol y verificar el error
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20,8,13,22]
		bt=Btree()
		for a in range(0,6):
		    insert(bt,keys[a],strings[a])
		res=delete(bt,54)
		self.assertEqual(res,None)

	def test_delete_root(self):
		""" Borrar el root de un arbol y verificar el nuevo root
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20]
		bt=Btree()
		for a in range(0,3):
		    insert(bt,keys[a],strings[a])
		#print()
		#print(bt.root.key,access(bt,bt.root.key))
		#print()
		delete(bt,10)
		#print()
		#print(bt.root.key,access(bt,bt.root.key))
		#print()
		res=access(bt,5)
		self.assertEqual(res,"2")


	def test_search(self):
		""" Busqueda de un elemento en un arbol y verificar su posicion y contenido
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20,8,13,18,22,2,9,40,21,11,7,3,1]
		bt=Btree()
		for a in range(0,15):
		    insert(bt,keys[a],strings[a])
		res=search(bt,"8")    
		self.assertEqual(res,2)

	def test_search_inexistent(self):
		""" Busqueda de un elemento inexistente en un arbol y verificar None
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	
		keys=[10,5,20,8,13,18,22,2,9,40,21,11,7,3,1]
		bt=Btree()
		for a in range(0,15):
		    insert(bt,keys[a],strings[a])
		res=search(bt,"g")    
		self.assertEqual(res,None)

	def test_access_inexistent_element(self):
		""" Acceder un elemento inexistente un arbol y verificar el error
		"""
		strings=["1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
		keys=[10,5,20,8,13,22]
		bt=Btree()
		for a in range(0,6):
		    insert(bt,keys[a],strings[a])
		res=access(bt,55)
		self.assertEqual(res,None)

if __name__ == '__main__':
	unittest.main(verbosity=2)