import numpy as np
import random


MIN = 120
MAX = 250
SEED = 42

def sells():
    random.seed(SEED)
    return [random.randint(MIN, MAX) for _ in range(4 * 7 * 10)]

def create_weekly_sells_table(sells):
    return np.array(sells).reshape((-1, 7, 10))

print(create_weekly_sells_table(sells()))