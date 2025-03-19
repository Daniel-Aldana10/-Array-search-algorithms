import time
import tracemalloc
from array_search import algorithms

import array_search.algorithms
from data import constants, data_generator

def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size:", size)
        samples = [data_generator.get_random_list(size) for _ in range(samples_by_size)]
        targets = [data_generator.get_random_x(size) for _ in range(samples_by_size)]
        results = take_times(samples, targets)
        lineal_time, lineal_mem = results[0]
        binary_time, binary_mem = results[1]
        ternary_time, ternary_mem = results[2]
        return_table.append([size, lineal_time, binary_time, ternary_time, lineal_mem, binary_mem, ternary_mem])
    return return_table

def take_execution_time_bin_ter(minimum_size, maximum_size, step, samples_by_size):
    return_table = []
    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size:", size)
        samples = [data_generator.get_random_list(size) for _ in range(samples_by_size)]
        targets = [data_generator.get_random_x(size) for _ in range(samples_by_size)]
        results = take_times(samples, targets)
        binary_time, binary_mem = results[1]
        ternary_time, ternary_mem = results[2]
        return_table.append([size,  binary_time, ternary_time, binary_mem, ternary_mem])
    return return_table
"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""

def take_times(sample, targets):
    return [
        take_time_and_memory_for_algorithm(sample,targets, algorithms.linear_search),
        take_time_and_memory_for_algorithm(sample,targets, algorithms.binary_search),
        take_time_and_memory_for_algorithm(sample,targets, algorithms.ternary_search),
    ]

"""
    Returns the median of the execution time measures for a sorting approach given in 
"""
def take_times_bin_ter(sample, targets):
    return [take_time_and_memory_for_algorithm(sample, targets, algorithms.binary_search),
            take_time_and_memory_for_algorithm(sample, targets, algorithms.ternary_search)]
def take_time_and_memory_for_algorithm(samples_array, elements, search_algorithm):
    times = []
    mem_usages = []
    for sample, element in zip(samples_array, elements):
        tracemalloc.start()
        start_time = time.time()
        search_algorithm(sample, element)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        exec_time = int(constants.TIME_MULTIPLIER * (end_time - start_time))
        times.append(exec_time)
        mem_usages.append(peak)
    times.sort()
    mem_usages.sort()
    return times[len(times) // 2], mem_usages[len(mem_usages) // 2]