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

climate_data_csv = np.genfromtxt("climate_data.txt", delimiter=",", skip_header=1)
print(climate_data_csv)
print(climate_data_csv.shape)

crop_yield_results = climate_data_csv @ weights


climate_results = np.concatenate(
    (climate_data_csv , crop_yield_results.reshape(-1, 1)),
    axis=1
)
print(climate_results)

np.savetxt(
    "climate_data.txt",
    climate_results,
    fmt="%.2f",
    header="Temperature_C,Humidity_%,Rainfall_mm,Crop_Yield",
    comments=""
)

array1 = np.array([[1, 3, 4, 3], [2, 6, 7, 1], [7, 3, 4, 1]])
array2 = np.array([[11, 13, 14, 13], [22, 36, 47, 51], [17, 23, 64, 71]])

print(array2 + 2)

print(array1 + array2)

array3 = np.array([2, 3, 4, 5])
print(array1 + array3)

array4 = np.array([1, 3])
print(array1 + array4)  # raises ValueError

