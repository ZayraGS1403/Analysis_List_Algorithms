# List/plot.py
import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
tables = [
    [1000, 253, 74, 24, 236, 79, 31],
    [1500, 143, 104, 16, 182, 109, 12],
    [2000, 365, 86, 24, 491, 102, 16],
    [2500, 597, 328, 24, 575, 402, 16],
    [3000, 1483, 75, 15, 1331, 587, 30],
    [3500, 387, 206, 21, 1691, 634, 61],
    [4000, 2181, 562, 23, 484, 331, 26],
    [4500, 1168, 804, 22, 1636, 471, 40],
    [5000, 2881, 1352, 24, 3462, 886, 25],
    [5500, 2851, 2577, 33, 1718, 1451, 59],
    [6000, 4015, 3083, 22, 1808, 385, 17],
    [6500, 4180, 1741, 21, 2688, 2480, 74],
    [7000, 4838, 3316, 70, 2876, 995, 106],
    [7500, 3649, 2318, 25, 3275, 930, 66],
    [8000, 6518, 956, 24, 5168, 2645, 44],
    [8500, 6035, 1220, 25, 1964, 1717, 54],
    [9000, 7367, 4819, 44, 4729, 1485, 103],
    [9500, 1840, 3007, 25, 5002, 1774, 41],
    [10000, 6118, 1799, 41, 4707, 2969, 87]
]

tables2 = [
    [10000, 3164, 4181, 21, 7364, 996, 70],
    [15000, 12501, 5955, 35, 12257, 6075, 83],
    [20000, 13697, 4657, 25, 10944, 9327, 144],
    [25000, 15908, 11773, 37, 9668, 5384, 113],
    [30000, 10711, 14107, 55, 28619, 14109, 69],
    [35000, 15309, 7484, 74, 28175, 22289, 341],
    [40000, 25554, 20978, 81, 23184, 7385, 220],
    [45000, 11076, 26099, 92, 51870, 13882, 391],
    [50000, 27804, 13097, 75, 16069, 27956, 209],
    [55000, 15494, 24153, 94, 52025, 10270, 376],
    [60000, 38650, 25637, 151, 53154, 15111, 256],
    [65000, 38637, 20919, 135, 34554, 34298, 262],
    [70000, 50990, 42366, 99, 47051, 43910, 354],
    [75000, 53568, 45915, 116, 77650, 39493, 556],
    [80000, 41898, 33609, 223, 84678, 9210, 446],
    [85000, 47545, 47828, 148, 97249, 54812, 836],
    [90000, 70149, 41121, 122, 65271, 37543, 721],
    [95000, 113463, 36795, 236, 106836, 71405, 148],
    [100000, 100246, 54495, 109, 37247, 13794, 487]
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



