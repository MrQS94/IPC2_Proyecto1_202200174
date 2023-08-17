from Controlador import Controlador

controlador_handler = Controlador()

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
            controlador_handler.cargar_archivo(ruta)
        elif opcion == '2':
            controlador_handler.procesar_archivo()
        elif opcion == '3':
            ruta_salida = input('Escribir una ruta especifica: ')
            controlador_handler.escribir_archivo_salida(ruta_salida)
        elif opcion == '4':
            controlador_handler.mostrar_datos_estudiante()
        elif opcion == '5':
            controlador_handler.graficar_original()
            controlador_handler.graficar_reducida()
        elif opcion == '6':
            reincio = input('El sistema está apunto de reiniciarse, ¿desea continuar? (Y/N): ')
            if reincio.lower() == 'y':
                controlador_handler.reinciar()
                print()
                print('El sistema ha sido reiniciado.')
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Error, opción incorrecta.')


if __name__ == '__main__':
    main()