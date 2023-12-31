from Nodo import Nodo


class ListaSimple():
    def __init__(self):
        self.head = None
        
    def append(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.head is None:
            self.head = nuevo_nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nuevo_nodo
            
    def suma(self, otra_lista):
        actual_lista = self.head
        actual_otra_lista = otra_lista.head
        result = ListaSimple()
        
        while actual_lista and actual_otra_lista:
            result.append(int(actual_lista.dato) + int(actual_otra_lista.dato))
            actual_lista = actual_lista.next
            actual_otra_lista = actual_otra_lista.next
            
        return result
    
    def size(self):
        count = 0
        actual = self.head
        while actual:
            count += 1
            actual = actual.next
        return count
    
