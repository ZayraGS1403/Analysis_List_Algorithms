# app.py
from List.execution_time_gathering import execution_time_gathering

if __name__ == "__main__":
    minimum_size = 100000
    maximum_size = 1000000
    step = 200000
    samples_by_size = 10   

    table = execution_time_gathering(minimum_size, maximum_size, step, samples_by_size)

    print(
        "Size | Insert LL | Insert DLL | Insert Array | Delete LL | Delete DLL | Delete Array"
    )
    for row in table:
        print(row)
