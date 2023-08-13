from xml.dom import minidom
from ListaSimple import ListaSimple
from xml.etree.ElementTree import Element, SubElement
from xml.etree import ElementTree


class Controlador():
    def __init__(self):
        self.aux = None
        self.matrix = ListaSimple()
        self.repeated_times = []

    def subir_archivo(self, ruta):
        try:
            xml = minidom.parse(ruta)
            self.aux = xml
            print('El archivo ha sido cargado!!')
        except ExceptionGroup:
            print('Error, el archivo no ha sido cargado.')
            
    def procesar_archivo(self):
        nombres = self.aux.getElementsByTagName('senal')
        count = 1
        
        for matriz in nombres:
            fila = matriz.getAttribute('t')
            columnas = matriz.getAttribute('A')
            self.matrix.agregar_tiempo_amplitud(matriz.attributes['nombre'].value, fila, columnas)
            filas = ListaSimple()
            
            for _ in range(int(fila)):
                fila_t = ListaSimple()
                filas.agregar_lista(fila_t)
            datos = matriz.getElementsByTagName('dato')
            
            for dato in datos:
                t = int(dato.attributes['t'].value)
                valor = dato.firstChild.data
                
                self.repeated_times.append(t)
                filas.devolver_lista(t).agregar_nuevo_dato(valor)
                if int(valor) == 0:
                    filas.devolver_lista(t).frecuencia_binaria += '0'
                else:
                    filas.devolver_lista(t).frecuencia_binaria += '1'
            self.matrix.devolver_lista(count).matriz = filas
            count += 1
            print('Matriz Cargado Exitosamente')
            
        for k in range(self.matrix.size):
            print('\nCalculando matriz binaria: ', str(k + 1))
            
            repeats = ListaSimple()
            repeats.empty_lista()
            
            reductions = ListaSimple()
            reductions.empty_lista()
            
            for i in range(self.matrix.devolver_lista(k + 1).matriz.size):
                repeat = ListaSimple()
                repeat.empty_lista()
            
                nueva_fila = ListaSimple()
                nueva_fila.empty_lista()
                
                for j in range(self.matrix.devolver_lista(k + 1).matriz.size):
                    if (i + 1) != (j + 1):
                        if self.matrix.devolver_lista(k + 1).matriz.devolver_lista(i + 1).frecuencia_binaria == self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).frecuencia_binaria and self.matrix.devolver_lista(k + 1).matriz.devolver_lista(i + 1).flag == False and self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).flag == False:
                            if repeat.is_empty() is True:
                                repeat.agregar_nuevo_dato(i + 1)
                                repeat.agregar_nuevo_dato(j + 1)
                                self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).flag = True
                                
                                tiempo_i = self.repeated_times[i]
                                tiempo_j = self.repeated_times[j]
                                print('en i', tiempo_i, " en j", tiempo_j)
                                
                                for p in range(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(i + 1).size):
                                    valor = int(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(i + 1).devolver_lista(p + 1).nombre) + int(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).devolver_lista(p + 1).nombre)
                                    nueva_fila.agregar_nuevo_dato(valor)
                            else:
                                repeat.agregar_nuevo_dato(j + 1)
                                self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).flag = True
                                for p in range(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(i + 1).size):
                                    nueva_fila.devolver_lista(p + 1).nombre += int(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(j + 1).devolver_lista(p + 1).nombre)
                                    
                if repeat.is_empty() is False:
                    repeats.agregar_lista(repeat)
                    reductions.agregar_lista(nueva_fila)
            
            self.matrix.devolver_lista(k + 1).repeticiones = repeats
            self.matrix.devolver_lista(k + 1).matriz_reducida = reductions
            
            
            if repeats.is_empty() is False:
                count = 0
                for a in range(self.matrix.devolver_lista(k + 1).matriz.size):
                    flag = False # Aquí debe ir el algoritmo
                    
                    for t in range(repeats.size):
                        for A in range(repeats.devolver_lista(t + 1).size):
                            if a + 1 == repeats.devolver_lista(t + 1).devolver_lista(A + 1).nombre:
                                flag = True
                                
                    if flag is False:
                        nueva_fila = ListaSimple()
                        nueva_fila.empty_lista()
                        
                        for u in range(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(a + 1).size):
                            nueva_fila.agregar_nuevo_dato(self.matrix.devolver_lista(k + 1).matriz.devolver_lista(a + 1).devolver_lista(u + 1).nombre)
                        self.matrix.devolver_lista(k + 1).matriz_reducida.agregar_lista(nueva_fila)
                        count += 1
                        
            for _ in range(count):
                lista_reducida = ListaSimple()
                lista_reducida.agregar_nuevo_dato(1)
                self.matrix.devolver_lista(k + 1).repeticiones.agregar_lista(lista_reducida)
                        
            print('\nMatriz Reducida')
            for n in range(self.matrix.devolver_lista(k + 1).matriz_reducida.size):
                print('fila ', str(n + 1))
                self.matrix.devolver_lista(k + 1).matriz_reducida.devolver_lista(n + 1).imprimir_nodos()
                
            print('\n Proceso terminado')
    
    def escribir_archivo_salida(self):
        print('Cargando archivo XML...')
        senales_reducidad = Element('senalesReducidas')
        
        for k in range(self.matrix.size):
            fila = str(self.matrix.devolver_lista( k + 1).matriz_reducida.size + 1)
            columna = str(self.matrix.devolver_lista(k + 1).columna)
            
            name = str(self.matrix.devolver_lista(k + 1).nombre)
            grupo = self.matrix.devolver_lista(k + 1).repeticiones.size
            child_senal = SubElement(senales_reducidad, 'senal', nombre = str(name), A = str(fila))
            for p in range(int(grupo)):
                child_grupo = SubElement(child_senal, 'grupo', g = str(p + 1))
                child_tiempos = SubElement(child_grupo, 'tiempos')
                
                tiempos = fila # Aquí añadir los grupos con los nombres creados
                
                child_tiempos.text = 'Hola ' + str(tiempos) 
                child_gatos_grupo = SubElement(child_grupo, 'datosGrupo')
                for i in range(self.matrix.devolver_lista(k + 1).matriz_reducida.size + 1):
                    row = i + 1
                    child_dato = SubElement(child_gatos_grupo, 'dato', A = str(row))
                    child_dato.text = str(self.matrix.devolver_lista(k + 1).matriz_reducida.devolver_lista(p + 1).devolver_lista(i + 1).nombre)
        
        r_string = ElementTree.tostring(senales_reducidad, 'UTF-8')
        reparsed = minidom.parseString(r_string)
        
        file = open('salida.xml', 'w')
        file.write(reparsed.toprettyxml(indent="  "))
        file.close()
    
    def escribir_archivo_salida_2(self):
        print('Cargando archivo XML...')
        top = Element('senalesReucidas')
        
        for k in range(self.matrix.size):
            fila = str(self.matrix.devolver_lista( k + 1).matriz_reducida.size)
            columna = str(self.matrix.devolver_lista(k + 1).columna)
            name = str(self.matrix.devolver_lista(k + 1).nombre + "_salida")
            grupo = self.matrix.devolver_lista(k + 1).repeticiones.size
            child_senal = SubElement(top, 'senal', nombre = str(name), A = str(fila))
            
            for i in range(self.matrix.devolver_lista(k + 1).matriz_reducida.size):
                for j in range(int(self.matrix.devolver_lista(k + 1).columna)):
                    row = i + 1
                    column = j + 1
                    child_dato = SubElement(child_senal, 'dato', A = str(row))
                    child_dato.text = str(self.matrix.devolver_lista(k + 1).matriz_reducida.devolver_lista(i + 1).devolver_lista(j + 1).nombre)
            
            for p in range(int(grupo)):
                child_frecuencia = SubElement(child_senal, 'frecuencia', g = str(p + 1))
                child_frecuencia.text = str(self.matrix.devolver_lista(k + 1).repeticiones.devolver_lista(p + 1).size)
                
        file = open('salida.xml', 'w')
        #file.write(str(self.prettify(top)))
        file.close()
        
        