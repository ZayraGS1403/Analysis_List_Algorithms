# Time Comparison of Inserts in Different Data Structures

-------

## 📌 Problem Statement
is a project that implements and compares the efficiency of different data structures in Python, specifically LinkedList, DoublyLinkedList, and Array, focusing on random insertion and deletion operations. The project includes tools to measure the execution times of these operations, generate random data, and visualize results in graphs for comparative analysis. This repository is ideal for students, researchers, or developers interested in algorithms and data structures.

------
## 📊 Features
Implementation of LinkedList, DoublyLinkedList, and Array with random insertion and deletion methods.
Random data generation for testing the structures.
Measurement of execution times for specific operations on each structure.
Visualization of results using line and bar charts with Matplotlib.
Unit tests to ensure the correctness of the implementations.

### Install the dependencies:
``` pip install matplotlib numpy```

------
### Analyze the results

#### Initial Results
Insertion Time Analysis

![Imagen de WhatsApp 2025-03-07 a las 08 10 46_628e6c15](https://github.com/user-attachments/assets/b6bbfbdf-0a17-45b9-85ae-7b9144d2e75f)

![Imagen de WhatsApp 2025-03-07 a las 08 13 40_ae7a4a76](https://github.com/user-attachments/assets/d9cafe70-0af2-48ac-a4d5-93e90fa83637)



Random Deletion Time Analysis

![Imagen de WhatsApp 2025-03-07 a las 08 10 58_e5318226](https://github.com/user-attachments/assets/d6b4f997-ce22-4003-a4d8-cdc646eeff6f)

![Imagen de WhatsApp 2025-03-07 a las 08 13 48_41813125](https://github.com/user-attachments/assets/6498b7f8-e609-41cd-804a-24073b3bb779)


---------
## Current Coverage

Ensure you have coverage installed (pip install coverage) and run the following commands:
``` coverage run -m unittest discover ```
``` coverage report ```

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
List\__init__.py                  0      0   100%
List\algorithms.py               95     14    85%
List\constants.py                 2      0   100%
List\data_generator.py           19      2    89%
Test\__init__.py                  0      0   100%
Test\test_algorithm.py          126      1    99%
Test\test_data_generator.py      52      1    98%
-------------------------------------------------
TOTAL                           294     18    94%


```
------
## 🎨 Code Beautifier

This code is formatted using black:```  https://github.com/psf/black. ```
Run the following command to format the code:

``` black . -l 120 ```

-------
## Author
Zayra Gutiérrez Solano


