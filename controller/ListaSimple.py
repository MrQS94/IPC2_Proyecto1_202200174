from Nodo import nodo


class ListaSimple():
    def __init__(self):
        self.head = None
        self.head_binarios = None
        
    def agregar_encabezado(self, dato, amplitud, tiempo):
        nuevo_nodo = nodo(dato, amplitud, tiempo)
        
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            
            actual.siguiente = nuevo_nodo
        
    def agrupar_grupos(self, listas):
        current = listas.head
        binario_grupo = ''
        count = 0
        count_grupo = 0
        
        while current is not None:
            binario_grupo += current.dato # Corregir que en vez que el dato se vuelva 0 o 1 que sea booleano, asi evitamos que se cambien los números
            count += 1
            if count == 4:
                count_grupo += 1
                print(f'Grupo {count_grupo} binario: {binario_grupo}')
                binario_grupo = ''
                count = 0
            current = current.siguiente
        
    def imprimir(self):
        actual = self.head
        while actual:
            print(f"Tiempo: {actual.tiempo} - Amplitud: {actual.amplitud} - Dato: {actual.dato}")
            actual = actual.siguiente
