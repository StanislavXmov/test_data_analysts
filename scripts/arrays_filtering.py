import numpy as np

def fill_neg_values(arr):
    np_list = np.array(arr)
    return np.where(np_list > 0, np_list, abs(np_list))

def fill_nan_values(arr):
    np_list = np.array(arr, dtype=np.float64)
    nan_mask = np.isnan(np_list)
    return np.where(nan_mask, 0, np_list)

print(fill_neg_values([5, -7, -12, 3]))
print(fill_nan_values([5, 7, None, None]))

def standard_scaler(image_mnist):
    image = np.array(image_mnist)
    mean_value = image.mean()
    std_value = image.std()
    return (image - mean_value) / std_value