# Unittest sobre Arrays
# Algoritmos y estructuras de datos I
import unittest
from algo1 import *
from why import search, insert, delete, length, enqueue, dequeue, push, pop
class TestArray(unittest.TestCase):
    def setUp(self):
        pass
    
    #asumo que insert devuelve el indice insertado o None en error.
    
    def test_length_bidi(self):
        """ verifica el numero de elementos del array bidimensional
        """
        vector=Array(3,Array(2,0))
        res=len(vector[0])
        self.assertEqual(res,2)
    def test_length_array_tri(self):
        """ verifica el numero de elementos de un array tridimensional
        """
        L=Array(10,Array(5,Array(3,0)))
        res=len(L[0][0])
        #print(res)
        self.assertEqual(res,3)
    def test_insert_element_empty_array(self):
        """ Insertar un elemento en un array vacio y se verifica que insert() devuelva None (error)
        """
        #arr=array(0,0)
        arr=[]
        res=insert(arr,1,2)
        #print('devuelve:',res)
        self.assertEqual(res,None)
        
    def test_insert_element_out_of_range(self):
        """ Insertar un elemento en la ultima posición de un array y se verifica que insert() devuelva None (error)
        """
        arr=Array(20,0)
        res=insert(arr,5,20)
        #print('devuelve:',res)
        self.assertEqual(res,None)
        
    def test_length_array(self):
        """ verifica el numero de elementos del array
        """
        vector=Array(10,0)
        res=len(vector)
        self.assertEqual(res,10)
        
    def test_insert_array1(self):
        """ verifico la funcion insert
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        insert(arr,15,2)
        res=arr[4]
        #print(res)
        self.assertEqual(res,40)
    def test__array_swap(self):
        """ verifico la funcion swap
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        #swap(arr,1,2)
        #print(arr)
        #res=arr[2]
        #print(res)
        #self.assertEqual(res,20)
        
    def test_array_delete_element_inexistent(self):
        """ Borrar un elemento inexistente de un array y se verifica que delete devuelva None
        """
        arr=Array(10,0)
        res=delete(arr,1)
        self.assertEqual(res,None)
    def test__array_delete(self):
        """ verifico la funcion delete
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        delete(arr,20)
        #print(arr)
        res=arr[1]
        #print(res)
        self.assertEqual(res,30)
    def test__array_delete_last_element(self):
        """ Borrar el ultimo elemento del array
        """
        arr=Array(10,0)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        delete(arr,40)
        #print(arr)
        res=arr[3]
        #print(res)
        self.assertEqual(res,None)
    def test__array_search(self):
        """ verifico la funcion search
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        res=search(arr,30)
        #print(res)
        self.assertEqual(res,2) 
    def test__array_search_inexistent(self):
        """ verifico la funcion search de un elemento inexistente
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        #print(arr)
        res=search(arr,50)
        #print(res)
        self.assertEqual(res,None)  
        
    def test_length(self):
        """ -- Verifica el numero de elementos del array cuando no son None
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        res=length(arr)
        self.assertEqual(res,4)
    def test_length_list_empty(self):
        """ -- Verifica el numero de elementos del array vacio
        """
        arr=Array(10)
        res=length(arr)
        self.assertEqual(res,0)
        
    def test_enqueue(self):
        """ -- Verifica función enqueue
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        enqueue(arr,5)
        res=arr[4]
        self.assertEqual(res,5)
    def test_dequeue(self):
        """ -- Verifica función enqueue
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        res=dequeue(arr)
        self.assertEqual(res,10)
        
    def test_push(self):
        """ -- Verifica función push
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        push(arr,5)
        res=arr[4]
        self.assertEqual(res,5)
    def test_pop(self):
        """ -- Verifica función pop
        """
        arr=Array(10)
        arr[0]=10
        arr[1]=20
        arr[2]=30
        arr[3]=40
        res=pop(arr)
        self.assertEqual(res,40)
        
    def test_push_desde_vacio(self):
        """ -- Verifica función push vacio
        """
        arr=Array(10)
        push(arr,5)
        res=arr[0]
        print(arr)
        self.assertEqual(res,5)
        
    def test_pop_vacio(self):
        """ -- Verifica función pop desde un array vacio
        """
        arr=Array(10)
        res=pop(arr)
        self.assertEqual(res,None)
if __name__ == '__main__':
    unittest.main(verbosity=2)