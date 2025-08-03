import numpy as np

items = np.array([
    [4,5,6],
    [3,1,4],
    [5,8,6],
])

items1 = np.array([
    [4, 5, 6]
])
items2 = np.array([
    [6, 5, 12]
])

def get_iqr(items):
    q1 = np.percentile(items, 25)
    q3 = np.percentile(items, 75)
    
    return (q1, q3)

def get_correlation(items1, items2):
    return np.corrcoef(items1, items2)[0, 1]

print(get_iqr(items))
print(get_correlation(items1, items2))