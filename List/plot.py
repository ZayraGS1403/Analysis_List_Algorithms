# List/plot.py
import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
tables = [
    [10000, 1053, 999, 0, 1000, 0, 0],
    [30000, 2189, 2191, 0, 4001, 2002, 0],
    [50000, 5191, 3001, 0, 6155, 3164, 0],
    [70000, 2008, 4147, 0, 10387, 2125, 0],
    [90000, 15651, 15791, 0, 8572, 4917, 0]
]

tables2 = [

]

# Extraer tamaños y tiempos
sizes = [row[0] for row in tables]
LinkedList_insert_times = [row[1] for row in tables]
DoublyLinkedList_insert_times = [row[2] for row in tables]
Array_insert_times = [row[3] for row in tables]
LinkedList_delete_times = [row[4] for row in tables]
DoublyLinkedList_delete_times = [row[5] for row in tables]
Array_delete_times = [row[6] for row in tables]

# Imprimir tabla
print("Size | Insert LL | Insert DLL | Insert Array | Delete LL | Delete DLL | Delete Array")
for row in tables:
    print(row)

# Gráfico de líneas para inserciones
plt.figure(figsize=(10, 6))
plt.plot(sizes, [x if x > 0 else float('nan') for x in LinkedList_insert_times],
         marker='o', linestyle='-', label='LinkedList Insert', color='blue')
plt.plot(sizes, [x if x > 0 else float('nan') for x in DoublyLinkedList_insert_times],
         marker='o', linestyle='-', label='DoublyLinkedList Insert', color='red')
plt.plot(sizes, [x if x > 0 else float('nan') for x in Array_insert_times],
         marker='o', linestyle='-', label='Array Insert', color='green')

plt.xlabel('List Size')
plt.ylabel('Execution time (ns)')
plt.title('Time Comparison of Inserts in Different Data Structures')
plt.legend()
plt.grid()
plt.show()

# Gráfico de líneas para eliminaciones
plt.figure(figsize=(10, 6))
plt.plot(sizes, [x if x > 0 else float('nan') for x in LinkedList_delete_times],
         marker='o', linestyle='-', label='LinkedList Delete', color='purple')
plt.plot(sizes, [x if x > 0 else float('nan') for x in DoublyLinkedList_delete_times],
         marker='o', linestyle='-', label='DoublyLinkedList Delete', color='orange')
plt.plot(sizes, [x if x > 0 else float('nan') for x in Array_delete_times],
         marker='o', linestyle='-', label='Array Delete', color='brown')

plt.xlabel('List Size')
plt.ylabel('Execution time (ns)')
plt.title('Time Comparison of Deletes in Different Data Structures')
plt.legend()
plt.grid()
plt.show()

# Gráfico de barras
x = np.arange(len(sizes))
width = 0.3  # Ancho de las barras

# Gráfico de barras para inserciones
plt.figure(figsize=(12, 6))
plt.bar(x - width, [x if x > 0 else float('nan') for x in LinkedList_insert_times],
        width=width, label='LinkedList Insert', color='blue')
plt.bar(x, [x if x > 0 else float('nan') for x in DoublyLinkedList_insert_times],
        width=width, label='DoublyLinkedList Insert', color='red')
plt.bar(x + width, [x if x > 0 else float('nan') for x in Array_insert_times],
        width=width, label='Array Insert', color='green')

plt.xlabel('List Size')
plt.ylabel('Execution time (ns)')
plt.xticks(ticks=x, labels=sizes)
plt.title('Execution Time Comparison of Inserts (Bar Chart)')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Gráfico de barras para eliminaciones
plt.figure(figsize=(12, 6))
plt.bar(x - width, [x if x > 0 else float('nan') for x in LinkedList_delete_times],
        width=width, label='LinkedList Delete', color='purple')
plt.bar(x, [x if x > 0 else float('nan') for x in DoublyLinkedList_delete_times],
        width=width, label='DoublyLinkedList Delete', color='orange')
plt.bar(x + width, [x if x > 0 else float('nan') for x in Array_delete_times],
        width=width, label='Array Delete', color='brown')

plt.xlabel('List Size')
plt.ylabel('Execution time (ns)')
plt.xticks(ticks=x, labels=sizes)
plt.title('Execution Time Comparison of Deletes (Bar Chart)')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()



