from ListaSimple import ListaSimple
from xml.dom import minidom
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element, SubElement
import time
from os import system


class Controlador():
    def __init__(self):
        self.xml= None
        self.patron_sumas = ListaSimple()
        self.nombre = ''
        self.columna = 0

    # Procesa los grupos y los convierte en binarios, también se puede hacer con bool pero no es lo más optimo
    def procesar_grupos(self, grupo):
        temp_str = ''
        datos_originales = ListaSimple()
        actual = grupo.head
        
        while actual:
            if actual.dato == 0:
                temp_str += '0'
            else:
                temp_str += '1'
            datos_originales.append(actual.dato)
            actual = actual.siguiente
        return temp_str, datos_originales

    def cargar_archivo(self, ruta):
        try:   
            _xml_ = minidom.parse(ruta)
            self.xml = _xml_   
            
            nombres = self.xml.getElementsByTagName('senal')
            for matriz in nombres:
                nombre = matriz.attributes['nombre'].value
                if self.nombre == nombre:
                    print('El archivo tiene el mismo nombre que el anterior.')
                    print('Se van a reemplazar los datos antiguos con los nuevos.')
            
            print('El archivo ha sido cargado exitosamente.')
        except FileNotFoundError:
            print('Error, el archivo no ha sido cargado.')
            
    def procesar_archivo(self):
        nombres = self.xml.getElementsByTagName('senal')
        grupos = ListaSimple()
        grupo_actual = ListaSimple()
        grupo_contador = 1
        
        for matriz in nombres:
            self.columna = matriz.getAttribute('A')
            fila = matriz.getAttribute('t')
            datos = matriz.getElementsByTagName('dato')
            self.nombre = matriz.attributes['nombre'].value
            
            if  not ((int(self.columna) > 0 and int(self.columna) <= 130) and (int(fila) > 0 and int(fila) <= 3600)):
                print('El archivo contiene un tiempo o amplitud mayor al necesario.')
                print('Verificar en el archivo .xml, debe ser: t > 0 y t <= 3600 y A > 0 y A <= 130')
                break
            else:
                # Se añaden los valores a una lista, y cuenta en la posición en donde se encuentra
                # También analiza la amplitud, y lo compara para saber que amplitud se deben de crear
                for dato in datos:
                    dato_str = dato.firstChild.data
                    dato_int = int(dato_str)
                    grupo_actual.append(dato_int)
                    if grupo_actual.size() == int(self.columna):
                        grupos.append((grupo_actual, grupo_contador))
                        grupo_actual = ListaSimple()
                        grupo_contador += 1
                    
                        
                # Es el proceso de la matriz binaria, es muy importante saber que acá mismo, se convierten en binarios
                # También se devuelven y hacen las sumas si hay un match, se sumaria el primero más el primero, y así ...
                actual = grupos.head
                
                while actual:
                    print('Calculando las matrices binarias...')
                    #time.sleep(1)
                    patron, datos_originales = self.procesar_grupos(actual.dato[0])
                    suma_datos = ListaSimple() 
                    datos_actuales = datos_originales.head
                    while datos_actuales:
                        suma_datos.append(datos_actuales.dato)
                        datos_actuales = datos_actuales.siguiente
                    if self.patron_sumas.head is None:
                        self.patron_sumas.append((patron, suma_datos, [actual.dato[1]]))
                    else:
                        # Acá se relizan las sumas y se hace un append a self.patron_sumas
                        actual_patron_suma = self.patron_sumas.head
                        while actual_patron_suma:
                            if actual_patron_suma.dato[0] == patron:
                                actual_patron_suma.dato = (patron, actual_patron_suma.dato[1].suma(suma_datos), actual_patron_suma.dato[2] + [actual.dato[1]])
                                break
                            elif actual_patron_suma.siguiente is None:
                                self.patron_sumas.append((patron, suma_datos, [actual.dato[1]]))
                                break
                            actual_patron_suma = actual_patron_suma.siguiente
                    actual = actual.siguiente
                print('Realizando suma de tuplas...')
                #time.sleep(2)
                print('Calculos de matrices y sumas, han sido completadas.')
                #time.sleep(1)
    
    def escribir_archivo_salida(self, ruta):
        top = Element('senalesReducidas')
        count_grupo = 0
        A_count = 0
        # Acá tenemos que self.patron_sumas, está en todo el Controlador, entonces solo necesitamos sacar
        # cada uno de sus valores, que sería patrones, suma_datos, grupo_contador, con ello los agrupamos siguiendo
        # la estructura que deseamos
        child_senal = SubElement(top, 'senal', nombre = str(self.nombre), A = f'{self.columna}')
        actual_patron_suma = self.patron_sumas.head
        while actual_patron_suma:
            _, suma_datos, grupo_contador = actual_patron_suma.dato
            count_grupo += 1
            child_grupo = SubElement(child_senal, 'grupo', g = str(count_grupo))
            child_tiempos = SubElement(child_grupo, 'tiempos')
            child_tiempos.text = str(grupo_contador)
            child_datos_grupo = SubElement(child_grupo, 'datosGrupo')
            A_count = 0
            
            actual_suma_datos = suma_datos.head
            while actual_suma_datos:
                A_count += 1
                child_dato = SubElement(child_datos_grupo, 'dato', A = str(A_count))
                child_dato.text = str(actual_suma_datos.dato)
                actual_suma_datos = actual_suma_datos.siguiente

            actual_patron_suma = actual_patron_suma.siguiente
            
        r_string = ET.tostring(top, 'UTF-8')
        reparsed = minidom.parseString(r_string)
        count_grupo = 0
        
        ruta_completa = ruta + 'salida.xml'
        with open(ruta_completa, 'w', encoding='UTF-8') as archivo:
            archivo.write(reparsed.toprettyxml(indent='  '))
            archivo.close()
            print('-'*100)
            print('Se guardo el archivo satisfactoriamente en la siguiente ruta: ')
            print('-'*100)
            print(ruta_completa)
            print('-'*100)
            input('Presione cualquier tecla para continuar...')
        
    def mostrar_datos_estudiante(self):
        print('Andres Alejandro Quezada Cabrera')
        print('202200174')
        print('Introducción a la Programción y Computación 2 - Sección \"D\"')
        print('Ingenieria en Ciencias y Sistemas')
        print('4to. Semestre')

    def graficar_reducida(self):
        print()
        print('Creando gráfica de matriz reducida...')
        time.sleep(2)
        nombres = self.xml.getElementsByTagName('senal')

        for matriz in nombres:  
            nombre = matriz.attributes['nombre'].value
            columna = matriz.getAttribute('A')
        
            graph_head = '''
            digraph L_reducida{
            node[shape=box]

            subgraph cluster_reducida{
            raiz[label = "'''+ str(nombre) +'''"]
            edge[dir = ""]
            
            Fila1[label="A = '''+ str(columna) +'''"];

            raiz -> Fila1
            '''
            
            graph_nodos = ""
            graph_nodos_edges = ""
            graph_edges = ""
            graph_grupos = ""
            count_grupo = 1
            count_nodo = 0
            actual_patron_suma = self.patron_sumas.head
            
            limite_patron_suma = self.patron_sumas_size()
            while actual_patron_suma: 
                _, suma_datos, grupo_contador = actual_patron_suma.dato
                graph_grupos += f'NodoGrupos{count_grupo}[label="g={count_grupo}| t={str(grupo_contador)}"]\n'
                if  count_grupo == 1:
                    graph_edges += f'raiz -> NodoGrupos{count_grupo}\n'
                elif count_grupo <= limite_patron_suma: 
                    graph_edges += f'NodoGrupos{count_grupo - 1} -> NodoGrupos{count_grupo}\n'
                actual_suma_datos = suma_datos.head
                while actual_suma_datos:
                    graph_nodos += f'Nodo{count_nodo}[label="{actual_suma_datos.dato}"];\n'
                    if count_nodo < int(columna):
                        graph_nodos_edges += f'raiz -> Nodo{count_nodo}\n'
                    else:
                        graph_nodos_edges += f'Nodo{count_nodo - int(columna)} -> Nodo{count_nodo}\n'
                        
                    count_nodo += 1
                    actual_suma_datos = actual_suma_datos.siguiente
                
                count_grupo += 1
                actual_patron_suma = actual_patron_suma.siguiente
        graph_footer = '''
            }
        }
        '''        
        graph = graph_head + graph_grupos + graph_nodos + graph_nodos_edges +  graph_edges + graph_footer
        self.cargar_grafica(graph, str(nombre) + '_salida')

    def patron_sumas_size(self):
        actual_patron_suma = self.patron_sumas.head
        count = 1
        while actual_patron_suma:
            count += 1
            actual_patron_suma = actual_patron_suma.siguiente
        return count

    def graficar_original(self):
        print()
        print('Creando gráfica orignal...')
        time.sleep(2)
        nombres = self.xml.getElementsByTagName('senal')

        for matriz in nombres:
            nombre = matriz.attributes['nombre'].value
            columna = matriz.getAttribute('A')
            fila = matriz.getAttribute('t')
            datos = matriz.getElementsByTagName('dato')
        
            graph_head = '''
            digraph L{
            node[shape=box]

            subgraph cluster{
            raiz[label = "'''+ str(nombre) +'''"]
            edge[dir = ""]

            Fila1[label="t = '''+ str(columna) +'''"];
            Fila2[label="A = '''+ str(fila) +'''"];

            raiz -> Fila1
            raiz -> Fila2 
            '''

            graph_nodos = ""
            graph_edges = ""
            count = 0
            for dato in datos:
                dato = dato.firstChild.data
                graph_nodos += f'Nodo{count}[label="{(dato)}"];\n'
                
                if count < int(columna):
                    graph_edges += f'raiz -> Nodo{count}\n'
                else:
                    graph_edges += f'Nodo{count - int(columna)} -> Nodo{count}\n'
                count += 1
            
        
        graph_footer = '''
            }
        }
        '''
        
        graph = graph_head + graph_nodos + graph_edges + graph_footer
        self.cargar_grafica(graph, nombre)
    
    def cargar_grafica(self, graph, nombre):
        nombre_sin_espacios = str(nombre).replace(' ', '')
        with open(f'graphviz_{nombre_sin_espacios}.dot', 'w', encoding='UTF-/') as archivo:
            archivo.write(graph)
            archivo.close()

        system(f'dot -Tpng graphviz_{nombre_sin_espacios}.dot -o graphviz_{nombre_sin_espacios}.png')
        system(f'cd ./graphviz_{nombre_sin_espacios}.png')
        
    def reinciar(self):
        self.xml = None