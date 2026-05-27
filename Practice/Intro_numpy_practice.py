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

array5 = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
array6 = np.array([[1, 2, 3, 4], [61, 71, 81, 91]])
 
print(array5 == array6)

total_common = (array5 == array6).sum()
print(total_common)

array7 = np.array([
    [[ 1,  2,  3,  4], [ 4,  3,  2,  1]],
    [[11, 21, 31, 41], [42, 33, 24, 14]],
    [[16, 26, 36, 46], [47, 37, 27, 17]]
])
 
print(array7.shape)

print(array7[1, 1, 1])

print(array7[1:, 0:1, :2])

print(array7[1:, 1, 0])

array8 = np.zeros((3, 2))
print(array8)

array9 = np.ones((3, 2))
print(array9)

print(np.eye(3))

print(np.random.rand(5))
print(np.random.rand(2, 3))

print(np.random.randn(5))
print(np.random.randn(2, 3))

print(np.full([2, 3], 4))

print(np.arange(10, 90, 3))
print(np.arange(10, 90, 3).reshape(3, 3, 3))
np.arange(10, 90, 3).reshape(3, 3, -1)

print(np.linspace(3, 27, 9))

