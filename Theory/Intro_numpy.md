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

