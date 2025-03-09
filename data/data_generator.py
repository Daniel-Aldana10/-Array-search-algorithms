import random
from data import constants
def get_random_list(size, limit=constants.MAX_VALUE):
    return sorted([random.randint(0, limit) for _ in range(size)])
def get_random_x(limit=constants.MAX_VALUE):
    return random.randint(1, limit)


