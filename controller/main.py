from ListaSimple import ListaSimple

lista_handler = ListaSimple()

ruta = "C:\\Users\\queza\\Documents\\Programacion\\Python\\USAC\\Lab IPC2\\Proyectos\\IPC2_Proyecto1_202200174\\src\\prueba1.xml"
def main():

    while True:
        print('-'*50)
        print('Menu Principal:')
        print('1. Cargar archivo')
        print('2. Procesar archivo')
        print('3. Escribir archivo salida')
        print('4. Mostrar datos del estudiante')
        print('5. Generar gráfica')
        print('6. Inicializar sistema')
        print('7. Salida')
        print('-'*50)
        opcion = input('Ingrese su opción a solicitar: ')
        print('-'*50)
        if opcion == '1':
            print('Opción Cargar Archivo: ')
            ruta = input('Ingrese la ruta del archivo: ')
            lista_handler.leer_archivos(ruta)
        elif opcion == '2':
            print()
        elif opcion == '3':
            print()
        elif opcion == '4':
            print()
        elif opcion == '5':
            print()
        elif opcion == '6':
            print()
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Error, opción incorrecta.')


main()