from Dato import ListaMatrices

class ListaSimple():
    def __init__(self):
        self.frecuencia_binaria = ''
        self.head = None
        self.flag = False
        self.size = 0
        
    def agregar_nuevo_dato(self, dato):
        nuevo_dato = ListaMatrices(dato)
        
        if self.head is None:
            self.head = nuevo_dato
            self.head.siguiente = self.head
            self.size += 1
        else:
            if self.head.siguiente == self.head:
                self.head.siguiente = nuevo_dato
                nuevo_dato.siguiente = self.head
                self.size += 1
            else:
                temp = self.head
                while temp.siguiente != self.head:
                    temp = temp.siguiente
                temp.siguiente = nuevo_dato
                nuevo_dato.siguiente = self.head
                self.size += 1    
                
    def agregar_tiempo_amplitud(self, dato, tiempo, amplitud):
        nuevo_TA = ListaMatrices(dato, tiempo, amplitud)
        if self.head is None:
            self.head = nuevo_TA
            self.head.siguiente = self.head
            self.size += 1
        else:
            if self.head.siguiente == self.head:
                self.head.siguiente = nuevo_TA
                nuevo_TA.siguiente = self.head
                self.size += 1
            else:
                temp = self.head
                while temp.siguiente != self.head:
                    temp = temp.siguiente
                temp.siguiente = nuevo_TA
                nuevo_TA.siguiente = self.head
                self.size += 1
                
    def agregar_lista(self, dato):
        nueva_lista = dato
        if self.head is None:
            self.head = nueva_lista
            self.head.siguiente = self.head
            self.size += 1
        else:
            temp = self.head
            while temp.siguiente != self.head:
                temp = temp.siguiente
            temp.siguiente = nueva_lista
            nueva_lista.siguiente = self.head
            self.size += 1
                
    def devolver_lista(self, indice):
        temp = self.head
        count = 1
        while count < indice:
            count += 1
            temp = temp.siguiente
        return temp
    
    def eliminar_lista(self, i):
        self.devolver_lista(i - 1).siguiente = self.devolver_lista(i + 1)
        self.size -= 1
        
    def get_size(self):
        return self.size
    
    def imprimir_nodos(self):
        temp = self.head
        size = 0
        while size < self.size:
            size += 1
            print('-', temp.nombre)
            temp = temp.siguiente
            
    def empty_lista(self):
        self.head = None
        
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
