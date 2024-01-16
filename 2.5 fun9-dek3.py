import time
import numpy as np


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"CZas wykonania funkcji {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_function_sum():
    suma = 0
    for i in range(15_000_000):
        suma += i
    print("Sum is:", suma)


@measure_time
def my_function():
    total = sum(range(15_000_000))
    print("Sum is:", total)

@measure_time
def my_function_np():
    total = np.sum(np.arange(15_000_000), dtype=np.int64)
    print("Sum is:", total)


my_function()
my_function_sum()
# Sum is: 112499992500000
# CZas wykonania funkcji my_function: 0.5877254009246826
# Sum is: 112499992500000
# CZas wykonania funkcji my_function_sum: 0.711397647857666
my_function_np()
# Sum is: 112499992500000
# CZas wykonania funkcji my_function: 0.6068851947784424
# Sum is: 112499992500000
# CZas wykonania funkcji my_function_sum: 0.7368135452270508
# Sum is: 1914115872
# CZas wykonania funkcji my_function_np: 0.03508877754211426