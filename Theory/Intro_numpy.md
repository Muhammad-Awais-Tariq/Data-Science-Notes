# NumPy Notes — Arrays, Dot Product & Matrix Multiplication

---

## 1. The Problem — Predicting Crop Yield

Suppose we want to calculate the **total crop yield** for a region using environmental factors. Each factor (humidity, rainfall, temperature) has a corresponding weight that represents how much it influences the yield.

For a region called **Kamra**, the data is:

| Factor      | Value | Weight |
|-------------|-------|--------|
| Humidity    | 50    | 0.1    |
| Rainfall    | 30    | 0.5    |
| Temperature | 70    | 0.3    |

---

## 2. Manual Approach — Pure Python

Before using NumPy, we can calculate this using a simple loop:

```python
Kamra = [50, 30, 70]
weights = [0.1, 0.5, 0.3]

def crop_yield(region, weights):
    result = 0
    for x, y in zip(region, weights):
        result += x * y
    return result

print(crop_yield(Kamra, weights))
```

`zip()` pairs up each element from both lists and multiplies them together one by one, accumulating the total.

---

## 3. The Dot Product — Concept First

What the function above is actually computing is called the **dot product**.

Given two vectors **A** and **B** of equal length:

$$\mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} A_i \times B_i$$

In plain terms — **multiply each pair of elements, then sum all the results.**

For our example:

```
(50 × 0.1) + (30 × 0.5) + (70 × 0.3)
=  5  +  15  +  21
=  41
```

The dot product is used here because we want a **weighted sum** — each factor contributes to the final yield proportionally to its weight.

---

## 4. NumPy Arrays

NumPy provides a dedicated array type (`numpy.ndarray`) that is far more efficient than Python lists for numerical computation.

```python
import numpy as np

Kamra = np.array([50, 30, 70])
weights = np.array([0.1, 0.5, 0.3])
```

Both variables now have the type `numpy.ndarray`.

### 4.1 Dot Product with NumPy

NumPy has a built-in `np.dot()` function that computes the dot product directly:

```python
print(np.dot(Kamra, weights))
```

### 4.2 Element-wise Multiplication + Sum

You can also compute it step by step using element-wise multiplication followed by `.sum()`:

```python
multiplication = Kamra * weights
total = multiplication.sum()
print(total)
```

Or more concisely in a single line:

```python
print((Kamra * weights).sum())
```

All three approaches — `crop_yield()`, `np.dot()`, and `(array * array).sum()` — produce the **exact same result**. NumPy just makes it cleaner and faster.

---

## 5. Benefits of NumPy Arrays

1. **Ease of use** — Most mathematical operations (dot product, sum, mean, etc.) are built-in methods. No need to write manual loops.

2. **Performance** — NumPy is implemented in **C** (not Python), so array operations run significantly faster, especially on large datasets. This matters when working with thousands or millions of data points.

---

## 6. 2D NumPy Arrays — Multiple Regions

When you have data for more than one region, a **2D array** (a matrix) is the right structure. NumPy supports any number of dimensions — 1D, 2D, 3D, or more (n-dimensional).

```python
climate_data = np.array([
    [50, 90, 50],
    [42, 65, 70],
    [80, 30, 99],
    [ 5, 25, 50],
    [70, 50, 30]
])
```

Each **row** is a region; each **column** is a feature (humidity, rainfall, temperature).

### Shape

```python
print(climate_data.shape)
```

Returns `(5, 3)` — 5 rows (regions) and 3 columns (features).

### Data Type

All elements in a NumPy array must share the **same data type**. This is required for performance — uniform types allow the data to be stored in a compact, contiguous block of memory.

```python
print(climate_data.dtype)
```

Returns `int64` — each number is stored as a 64-bit integer.

> **Important:** If even a single element in the array is a float, NumPy will automatically convert **all** values to `float64`.

---

## 7. Matrix Multiplication — Concept First

When you have a 2D array (matrix) and a 1D array (vector), multiplying them together is called **matrix-vector multiplication**.

Given a matrix **M** of shape `(n, k)` and a vector **v** of shape `(k,)`, the result is a vector of shape `(n,)` where each element is the **dot product of a row of M with v**.

Visually for our case (`5×3` matrix × `3,` vector → `5,` vector):

```
Region 1: (50×0.1) + (90×0.5) + (50×0.3) = 5  + 45 + 15 = 65
Region 2: (42×0.1) + (65×0.5) + (70×0.3) = 4.2 + 32.5 + 21 = 57.7
... and so on for each region
```

Each value in the output is the **weighted yield for that region**.

### 7.1 Using `np.matmul()`

```python
print(np.matmul(climate_data, weights))
```

### 7.2 Using the `@` Operator

Python's `@` operator is shorthand for matrix multiplication and is the modern, preferred way to write it:

```python
print(climate_data @ weights)
```

Both produce identical results — a 1D array of 5 values, one crop yield per region.

---

 
## 8. Reading Data from a CSV File
 
So far we've been typing data directly into the code. In practice, data lives in files. NumPy provides `np.genfromtxt()` to load tabular data from a text or CSV file.
 
```python
climate_data_csv = np.genfromtxt("climate_data.txt", delimiter=",", skip_header=1)
print(climate_data_csv)
print(climate_data_csv.shape)
```
 
The three parameters do the following:
 
| Parameter | Value | What it does |
|---|---|---|
| `fname` | `"climate_data.txt"` | Path to the file to read |
| `delimiter` | `","` | The character used to separate values in each row |
| `skip_header` | `1` | Skips the first N lines — used to ignore the column header row |
 
Once loaded, `climate_data_csv` is a normal NumPy 2D array and you can use it exactly like the manually defined one from before. If the file has 100 rows and 3 columns, its shape will be `(100, 3)`.
 
---

## 9. Computing Yield from Loaded Data
 
With the data loaded, we can apply the same matrix multiplication to get the crop yield for every region in one step:
 
```python
crop_yield_results = climate_data_csv @ weights
```
 
This produces a 1D array of shape `(100,)` — one yield value per row (region) in the CSV.

---

## 10. `reshape()` — Concept First
 
Before we can attach the yield results back to the climate data, we need to understand `reshape()`.
 
`reshape()` changes the **shape** of an array without changing its data or the number of elements.
 
After the matrix multiplication, `crop_yield_results` has shape `(100,)` — a flat 1D array of 100 numbers. But `climate_data_csv` has shape `(100, 3)` — a 2D array. You **cannot concatenate** a 1D array alongside a 2D array column-wise; the dimensions don't align.
 
The fix is to reshape the 1D array into a 2D column vector:
 
```
(100,)   →   (100, 1)
```
 
Visually:
 
```
Before reshape:  [65.0, 57.7, 88.1, ...]         shape: (100,)
 
After reshape:   [[65.0],
                  [57.7],
                  [88.1],
                  ...]                            shape: (100, 1)
```
 
Now it has 100 rows and 1 column — which lines up perfectly with the 100 rows of the climate data.
 
```python
crop_yield_results.reshape(-1, 1)
```
 
> **Tip:** Using `-1` instead of a hardcoded `100` is better practice. NumPy automatically infers that dimension from the array's size, so the code still works even if the number of rows changes.
 
---

## 11. Concatenating Arrays — Attaching the Yield Column
 
`np.concatenate()` joins two or more arrays together. The `axis` parameter controls the direction:
 
- `axis=0` — stack **vertically** (add more rows)
- `axis=1` — stack **horizontally** (add more columns) ✓ this is what we want
```python
climate_results = np.concatenate(
    (climate_data_csv, crop_yield_results.reshape(-1, 1)),
    axis=1
)
print(climate_results)
```
 
The result is a new array of shape `(100, 4)` — the original 3 feature columns plus the computed yield as a 4th column.
 
---