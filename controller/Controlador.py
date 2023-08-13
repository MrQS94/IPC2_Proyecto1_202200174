from ListaSimple import ListaSimple
from xml.dom import minidom

class Controlador():
    def __init__(self):
        self.xml= None
        self.lista_encabezado = ListaSimple()
        self.lista_datos = ListaSimple()
        self.lista_binarios = ListaSimple()
        
    
    def cargar_archivo(self, ruta):
        try:
            xml = minidom.parse(ruta)
            self.xml = xml
            print('El archivo ha sido cargado!!')
        except ExceptionGroup:
            print('Error, el archivo no ha sido cargado.')
    
    def procesar_archivo(self):
        nombres = self.xml.getElementsByTagName('senal')
        lista_temp_binario = ListaSimple()
        
        for matriz in nombres:
            fila = matriz.getAttribute('t')
            columna = matriz.getAttribute('A')
            nombre = matriz.attributes['nombre'].value
            self.lista_encabezado.agregar_encabezado(nombre, columna, fila)
            
            datos = matriz.getElementsByTagName('dato')
            for dato in datos:
                t = int(dato.attributes['t'].value)
                A = int(dato.attributes['A'].value)
                dato_ = dato.firstChild.data