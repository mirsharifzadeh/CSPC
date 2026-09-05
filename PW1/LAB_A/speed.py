import time
from decay import simulate_loop
from decay import simulate

python_pure_times = []
numpy_times = []

for i in range(1000):
    start_time_pure_python = time.perf_counter()

    simulate_loop(20000, 0.4)

    end_time_pure_python = time.perf_counter()

    start_time_numpy = time.perf_counter()

    simulate(20000, 0.4)

    end_time_numpy = time.perf_counter()

    pure_python_time = end_time_pure_python - start_time_pure_python
    numpy_time = end_time_numpy - start_time_numpy

    python_pure_times.append(pure_python_time)
    numpy_times.append(numpy_time)

pure_avr = sum(python_pure_times)/1000
numpy_avr = sum(numpy_times)/1000

print("Pure Python:", pure_avr)
print("Numpy Version:", numpy_avr)

print(f"NumPy Version is {pure_avr/numpy_avr:.2f} times faster than Pure Python Version")

