# List/plot.py
import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
tables = [
    [10000, 1003, 0, 0, 998, 1136, 0],
    [20000, 2000, 1998, 0, 1008, 1188, 0],
    [30000, 3190, 1997, 0, 3184, 2002, 0],
    [40000, 3189, 1003, 0, 3173, 4176, 0],
    [50000, 5204, 4170, 0, 7079, 6001, 0],
    [60000, 7736, 4002, 0, 5989, 8201, 0],
    [70000, 1621, 6998, 1137, 6518, 11194, 0],
    [80000, 9998, 13005, 1002, 10509, 11999, 0],
    [90000, 10822, 14517, 998, 2384, 13999, 0],
    [100000, 27391, 32053, 0, 7874, 14476, 0]
]

tables2 = [
    [10000, 1036, 998, 0, 0, 998, 0],
    [30000, 1006, 1199, 0, 1999, 1001, 0],
    [50000, 13108, 5000, 1507, 8008, 3003, 0],
    [70000, 9995, 3999, 0, 8000, 6000, 0],
    [90000, 11637, 5237, 1020, 6999, 8509, 0]
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



