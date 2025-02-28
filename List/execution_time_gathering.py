import time
import random
from List.data_generator import (
    get_random_linked_list,
    get_random_doubly_linked_list,
    get_random_array,
)
from List.constants import MAX_VALUE, TIME_MULTIPLIER


def execution_time_gathering(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    Returns six values: execution time for insert and delete operations on each structure
"""


def take_times(size, samples_by_size):
    # Generar muestras una vez para cada estructura
    samples_ll = [get_random_linked_list(size) for _ in range(samples_by_size)]
    samples_dll = [get_random_doubly_linked_list(size) for _ in range(samples_by_size)]
    samples_arr = [get_random_array(size) for _ in range(samples_by_size)]

    # Usar lambdas para minimizar overhead
    return [
        take_time_for_operation(samples_ll, "Insert LL"),
        take_time_for_operation(samples_dll, "Insert DLL"),
        take_time_for_operation(samples_arr, "Insert Array"),
        take_time_for_operation(samples_ll, "Delete LL"),
        take_time_for_operation(samples_dll, "Delete DLL"),
        take_time_for_operation(samples_arr, "Delete Array"),
    ]


"""
    Returns the median execution time for an operation on a given structure
    Usa una muestra para minimizar copias innecesarias
"""


def take_time_for_operation(samples_array, label):
    times = []

    for sample in samples_array:
        start_time = time.time()

        if label == "Insert LL":
            sample.insert_random(random.randint(0, MAX_VALUE))
        elif label == "Insert DLL":
            sample.insert_random(random.randint(0, MAX_VALUE))
        elif label == "Insert Array":
            sample.insert(
                random.randint(5000, len(sample) - 1), random.randint(0, MAX_VALUE)
            )
        elif label == "Delete LL":
            sample.delete_random()
        elif label == "Delete DLL":
            sample.delete_random()
        elif label == "Delete Array":
            if len(sample) > 0:
                sample.pop(
                    random.randint(5000, len(sample) - 1)
                )  # Eliminación aleatoria en array

        times.append(int(TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]
