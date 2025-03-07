import time
from array_search import algorithms

import array_search.algorithms
from data import constants, data_generator

def take_execution_time(minimum_size, maximum_size, step, samples_by_size):
    return_table = []

    for size in range(minimum_size, maximum_size + 1, step):
        print("Processing size: " + str(size))
        table_row = [size]
        times = take_times(size, samples_by_size)
        return_table.append(table_row + times)

    return return_table


"""
    It will return three values, one for each algorithm: The execution time for that size on each algorithm
"""


def take_times(size, samples_by_size):
    samples = []
    for _ in range(samples_by_size):
        samples.append(data_generator.get_random_list(size))

    return [
        take_time_for_algorithm(samples, algorithms.linear_search),
        take_time_for_algorithm(samples, algorithms.binary_search),
        take_time_for_algorithm(samples, algorithms.ternary_search),
    ]


"""
    Returns the median of the execution time measures for a sorting approach given in 
"""


def take_time_for_algorithm(samples_array, search_algorithm):
    times = []
    for sample in samples_array:
        element = data_generator.get_random_x()
        start_time = time.time()
        search_algorithm(sample, element)
        times.append(int(constants.TIME_MULTIPLIER * (time.time() - start_time)))

    times.sort()
    return times[len(times) // 2]