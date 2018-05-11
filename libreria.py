#vim: set tabstop=4 shiftwidth=4 expandtab   
import unittest
from linkedlist import LinkedList,insert,length,access,delete,search,add,update,enqueue,dequeue,pop,push
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        pass

    def test_insert_first_element(self):
        """ -- Inserta un solo elemento en una lista vacia y verificar su valor
        """
        L=LinkedList()
        insert(L,"hola",0)
        self.assertEqual(L.head.value,"hola")       

    def test_insert_element_out_of_range(self):
        """ -- Inserta un elemento fuera de rango en una lista vacia y verificar su valor
        """
        L=LinkedList()
        insert(L,"hola",1)
        self.assertEqual(L.head,None)       

    def test_insert_element_out_of_range(self):
        """ -- Inserta un elemento fuera de rango en una lista vacia y se verifica que insert() devuelva None
        """
        L=LinkedList()
        res=insert(L,"hola",1)
        self.assertEqual(res,None)       

    def test_insert_check_position_empty_list(self):
        """ -- Inserta un solo elemento en una lista vacia y verificar que insert devuelva la posicion correcta
        """
        L=LinkedList()
        res=insert(L,"hola",0)
        self.assertEqual(res,0)       

    def test_insert_check_position_full_list(self):
        """ -- Inserta un solo elemento en una lista llena y verificar que insert() devuelva la posicion correcta
        """
        L=LinkedList()
        insert(L,"hola",0)
        insert(L,"pepe",1)
        res=insert(L,"soy",2)
        self.assertEqual(res,2)

    def test_insert_elements(self):
        """ -- Inserta varios elementos en differentes posiciones en una lista vacia y verificar su valores
        """
        L=LinkedList()
        insert(L,"hola",0)
        insert(L,"soy",1)
        insert(L,"harpo",2)
        insert(L,"uds",2)
        insert(L,"quienes",1)
        self.assertEqual([L.head.value,
                L.head.nextNode.value,
                L.head.nextNode.nextNode.value,
                L.head.nextNode.nextNode.nextNode.value,
                L.head.nextNode.nextNode.nextNode.nextNode.value],["hola","quienes","soy","uds","harpo"])


    def test_delete_elements(self):
        """ -- Elimina varios elementos de una lista y verificar que la lista contenga los elementos restantes
        """
        L=LinkedList()
        insert(L,"hola",0)
        insert(L,"soy",1)
        insert(L,"harpo",2)
        insert(L,"uds",2)
        insert(L,"quienes",1)

        delete(L,"quienes")
        delete(L,"uds")
        self.assertEqual([L.head.value,
                L.head.nextNode.value,
                L.head.nextNode.nextNode.value,
                ],["hola","soy","harpo"])

    def test_delete_last_element(self):
        """ -- Elimina el ultimo elemento de una lista y verificar que la lista contenga los elementos restantes
        """
        L=LinkedList()
        insert(L,"hola",0)
        insert(L,"soy",1)
        insert(L,"harpo",2)
        insert(L,"vos?",3)

        delete(L,"vos?")
        self.assertEqual([L.head.value,
                L.head.nextNode.value,
                L.head.nextNode.nextNode.value,
                ],["hola","soy","harpo"])


    def test_delete_first_element(self):
        """ -- Elimina el primer elemento de una lista y verificar que la lista contenga los elementos restantes
        """
        L=LinkedList()
        insert(L,"hola",0)
        insert(L,"soy",1)
        insert(L,"harpo",2)
        insert(L,"vos?",3)

        delete(L,"hola")
        self.assertEqual([L.head.value,
                L.head.nextNode.value,
                L.head.nextNode.nextNode.value,
                ],["soy","harpo","vos?"])
        
    def test_delete_element_from_empty_list(self):
         """ -- Elimina  elemento de una lista vaciat y verificar que delete() devuelva None
         """
         L=LinkedList()
         res=delete(L,"hola")
         self.assertEqual(res,None)
                
    def test_search_element_from_empty_list(self):
         """ -- Busca  elemento de una lista vacia y verificar que search() devuelva None
         """
         L=LinkedList()
         res=search(L,"hola")
         self.assertEqual(res,None)
        
    def test_search_element_from_list(self):
        """ -- Busca  elemento en una lista con un unico elemento y verificar que encuentre la posicion
        """
        L=LinkedList()
        add(L,"hola")
        add(L,"jorge")
        add(L,"como")
        res=search(L,"hola")
        self.assertEqual(res,2)

    def test_access_from_list(self):
        """ -- Accede a un elemento en una lista y verifica que acces() devuelva el valor correcto
        """
        L=LinkedList()
        add(L,"hola")
        add(L,"jorge")
        res=access(L,1)
        self.assertEqual(res,"hola")

    def test_access_from_empty_list(self):
        """ -- Accede a un elemento que no se encuentra en la lista y verifica que access() devuelve None
        """
        L=LinkedList()
        res=access(L,1)
        self.assertEqual(res,None)

    def test_update_from_list(self):
        """ -- Accede a un elemento de la lista y modifica su valor y luego verifica que sea se haya actualizado con dicho valor
        """
        l=LinkedList()
        add(l,"hola")
        add(l,"jorge")
        update(l,"pepe",1)
        self.assertEqual(l.head.nextNode.value,"pepe")

    def test_update_from_list(self):
        """ -- Accede a un elemento de la lista, modifica su valor y verifica que devuelva True
        """
        l=LinkedList()
        add(l,"hola")
        add(l,"jorge")
        res=update(l,"pepe",1)
        self.assertEqual(res,1)
   
    
    def test_update_from_list_out_of_range(self):
        """ -- Accede a un elemento fuera dede la lista, modifica su valor y verifica que devuelva False
        """
        L=LinkedList()
        add(L,"hola")
        add(L,"jorge")
        res=update(L,"pepe",4)
        self.assertEqual(res,None)

    def test_queue_ops(self):
        """ -- Verifica que el primer elemento ingresado en la cola sea el primero en salir
        """
        L=LinkedList()
        enqueue(L,"hola")
        enqueue(L,"jorge")
        enqueue(L,"como")
        first=dequeue(L)
        second=dequeue(L)
        third=dequeue(L)
        fourth=dequeue(L)
        self.assertEqual([first,second,third,fourth],["hola","jorge","como",None])
   
    def test_stack_ops(self):
        """ -- Verifica que el ultimo elemento ingresado en la cola sea el primero en salir
        """
        L=LinkedList()
        push(L,"hola")
        push(L,"jorge")
        push(L,"como")
        push(L,"va?")
        first=pop(L)
        second=pop(L)
        self.assertEqual([first,second],["va?","como"])

    def test_length(self):
        """ -- Verifica el numero de elementos de la lsita cuando son mayores a 1
        """
        L=LinkedList()
        push(L,"hola")
        push(L,"jorge")
        push(L,"como")
        push(L,"va?")
        res=length(L)
        self.assertEqual(res,4)

    def test_length_list_empty(self):
        """ -- Verifica el numero de elementos de la lista cuando la lista esta vacia
        """
        L=LinkedList()
        res=length(L)
        self.assertEqual(res,0)








                
if __name__=="__main__":
    unittest.main(verbosity=2)
