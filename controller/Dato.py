class ListaMatrices():
    def __init__(self, nombre, fila = None, columna = None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.matriz = None
        self.matriz_reducida = None
        self.repeticiones = None
        self.siguiente = None