from Nodo import nodo
from Dato import Dato
import xml.etree.ElementTree as ET


class ListaSimple():
    def __init__(self):
        self.head = None
        
    def leer_archivos(self, ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        for senal in root.findall('senal'):
            nombre = senal.get('nombre')
            t = senal.get('t')
            A = senal.get('A')
            print(f"Señal: {nombre}, t: {t}, A: {A}")
            
            for dato in senal.findall('dato'):
                t_dato = dato.get('t')
                A_dato = dato.get('A')
                dato = int(dato.text)
                
                nuevo_dato = Dato(dato, t_dato, A_dato)
                self.agregar(nuevo_dato)
                
    def agregar(self, dato):
        nuevo_nodo = nodo(dato=dato)
        
        if self.head is None:
            self.head = nuevo_nodo
        else:
            actual = self.head
            while actual.siguiente:
                actual = actual.siguiente
            
            actual.siguiente = nuevo_nodo

