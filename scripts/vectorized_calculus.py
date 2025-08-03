import numpy as np

def analisis_clicks(click):
    if click % 2 != 0:
        return click + 1
    else:
        return click

def get_even_clicks(clicks):
    clicks = np.array(clicks)
    vectorize = np.vectorize(analisis_clicks)
    return vectorize(clicks)

print(get_even_clicks([[5, 7], [12, 3]]))
print(get_even_clicks([[10, 15], [0, 15], [10, 5]]))