import numpy as np

Kamra = [50, 30, 70]
weights = [0.1, 0.5, 0.3]

def crop_yield(region, weights):
    result = 0
    for x, y in zip(region, weights):
        result += x * y
    return result

print(crop_yield(Kamra, weights))

Kamra = np.array([50, 30, 70])
weights = np.array([0.1, 0.5, 0.3])

print(np.dot(Kamra, weights))

climate_data = np.array([
    [50, 90, 50],
    [42, 65, 70],
    [80, 30, 99],
    [ 5, 25, 50],
    [70, 50, 30]
])

print(np.matmul(climate_data, weights))