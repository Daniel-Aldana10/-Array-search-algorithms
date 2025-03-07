import random
from data import constants
def get_random_list(size, limit=constants.MAX_VALUE):
    return [random.randint(0, limit) for _ in range(size)]

def get_sorted_random_list(size, limit=constants.MAX_VALUE):
    lst = get_random_list(size, limit)
    return lst.sort()
def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


