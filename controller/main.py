"""from Controlador import Controlador

lista_handler = Controlador()

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
            #ruta = input('Ingrese la ruta del archivo: ')
            lista_handler.cargar_archivo(ruta)
        elif opcion == '2':
            lista_handler.procesar_archivo()
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

main()"""

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        nuevo_nodo = Node(data)
        if self.head is None:
            self.head = nuevo_nodo
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = nuevo_nodo
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
        print('None')    
        

def crear_grupo(numbers, size, linked_list):
    count = 0
    for num in numbers:
        linked_list.append(num)
        count += 1
        if count == size:
            break

def main():
    data = [2, 3, 0, 4, 0, 0, 6, 3, 3, 4, 0, 2, 1, 0, 1, 5, 0, 0, 3, 1]
    group_size = 4
    
    main_list = LinkedList()
    
    while data:
        group_list = LinkedList()
        crear_grupo(data, group_size, group_list)
        data = data[group_size:]
    
    
    
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def convert_to_pattern(number_list):
    patterns = []
    current_pattern = []

    for number in number_list:
        if len(current_pattern) < 4:
            current_pattern.append(number)
        if len(current_pattern) == 4:
            patterns.append(current_pattern.copy())
            current_pattern = []

    return patterns

def apply_patterns(patterns):
    new_patterns = []

    for pattern in patterns:
        new_pattern = [0 if num == 0 else 1 for num in pattern]
        new_patterns.append(new_pattern)

    return new_patterns

def compare_patterns(patterns):
    grouped_patterns = {}
    
    for idx, pattern in enumerate(patterns):
        key = tuple(pattern)
        if key not in grouped_patterns:
            grouped_patterns[key] = []
        grouped_patterns[key].append(idx)

    return grouped_patterns

def sum_original_values(number_list, groups):
    group_sums = {}

    for pattern, indices in groups.items():
        group_sum = sum(number_list[i] for i in indices)
        group_sums[pattern] = group_sum

    return group_sums

def print_grouped_sums_with_sums(grouped_sums, original_patterns, group_sums):
    for pattern, indices in grouped_sums.items():
        print("Grupo", indices, end=" ")
        if len(indices) == 1:
            pattern_values = original_patterns[indices[0]]
            pattern_sum = " + ".join(f"({a})" for a in pattern_values)
        else:
            pattern_values = original_patterns[indices[0]]
            sum_values = []
            for idx in indices[1:]:
                sum_values.extend(original_patterns[idx])
            pattern_sum = " + ".join(f"({a + b})" for a, b in zip(pattern_values, sum_values))
        print(pattern_sum)
        print("Suma:", group_sums[pattern])

number_list = [2, 3, 0, 4, 0, 0, 6, 3, 3, 4, 0, 2, 1, 0, 1, 5, 0, 0, 3, 1]
original_patterns = convert_to_pattern(number_list)
new_patterns = apply_patterns(original_patterns)
grouped_new_patterns = compare_patterns(new_patterns)
group_sums = sum_original_values(number_list, grouped_new_patterns)

grouped_sums = {}
for pattern, indices in grouped_new_patterns.items():
    if pattern in grouped_sums:
        grouped_sums[pattern].extend(indices)
    else:
        grouped_sums[pattern] = indices

print("Original Numbers:", number_list)
print("\nGrouped Sums with Sums:")
print_grouped_sums_with_sums(grouped_sums, original_patterns, group_sums)"""