# NumPy Notes — Arrays, Dot Product & Matrix Multiplication

---
 
## Table of Contents

**NumPy Fundamentals**

1. [The Problem — Predicting Crop Yield](#1-the-problem--predicting-crop-yield)
2. [Manual Approach — Pure Python](#2-manual-approach--pure-python)
3. [The Dot Product — Concept First](#3-the-dot-product--concept-first)
4. [NumPy Arrays](#4-numpy-arrays)
5. [Benefits of NumPy Arrays](#5-benefits-of-numpy-arrays)
6. [2D NumPy Arrays — Multiple Regions](#6-2d-numpy-arrays--multiple-regions)
7. [Matrix Multiplication — Concept First](#7-matrix-multiplication--concept-first)

**File I/O with NumPy**

8. [Reading Data from a CSV File](#8-reading-data-from-a-csv-file)
9. [Computing Yield from Loaded Data](#9-computing-yield-from-loaded-data)
10. [reshape() — Concept First](#10-reshape--concept-first)
11. [Concatenating Arrays — Attaching the Yield Column](#11-concatenating-arrays--attaching-the-yield-column)
12. [Writing Data Back to a File](#12-writing-data-back-to-a-file)
13. [Useful NumPy Functions Reference](#13-useful-numpy-functions-reference)

**Array Operations**

14. [Arithmetic Operations](#14-arithmetic-operations)
15. [Broadcasting — Concept First](#15-broadcasting--concept-first)
15.1 [Understanding Axis in NumPy Arrays](#151-understanding-axis-in-numpy-arrays)
16. [Comparison Operations](#16-comparison-operations)
17. [Array Indexing and Slicing](#17-array-indexing-and-slicing)

**Creating Arrays**

18. [Special Array Creation Functions](#18-special-array-creation-functions)
    - [18.1 np.zeros()](#181-npzeros--array-of-all-zeros)
    - [18.2 np.ones()](#182-npones--array-of-all-ones)
    - [18.3 np.eye()](#183-npeye--identity-matrix)
    - [18.4 np.random.rand()](#184-nprandomrand--uniform-random-values)
    - [18.5 np.random.randn()](#185-nprandomrandn--standard-normal-random-values)
    - [18.6 np.full()](#186-npfull--array-filled-with-a-specific-value)
    - [18.7 np.arange()](#187-nparange--range-based-array)
    - [18.8 np.linspace()](#188-nplinspace--equally-spaced-values)

**Python File I/O & CSV Parsing**

19. [Downloading Files from the Web](#19-downloading-files-from-the-web)
20. [Reading a File in Python](#20-reading-a-file-in-python)
21. [Parsing CSV Data Manually](#21-parsing-csv-data-manually)
22. [The Complete read_csv() Function](#22-the-complete-read_csv-function)
23. [The write_csv() Function](#23-the-write_csv-function)
24. [What the Instructor Means by os](#24-what-the-instructor-means-by-os)

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
 
> **Note:** Avoid using `sum` as a variable name — it shadows Python's built-in `sum()` function.
 
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
 
> **Note:** The original code reused the name `crop_yield` for this result, which overwrites the function defined earlier. Renamed here to `crop_yield_results` to avoid that conflict.
 
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
 
## 12. Writing Data Back to a File
 
Once we have the combined results, we can save them back to a file using `np.savetxt()`:
 
```python
np.savetxt(
    "climate_results.txt",
    climate_results,
    fmt="%.2f",
    header="Temperature_C,Humidity_%,Rainfall_mm,Crop_Yield",
    comments=""
)
```
 
Here is what each parameter does:
 
| Parameter | Value | What it does |
|---|---|---|
| `fname` | `"climate_results.txt"` | Name of the output file |
| `X` | `climate_results` | The array to write |
| `fmt` | `"%.2f"` | Format string — rounds every number to 2 decimal places. Without this, NumPy writes up to 18 decimal places by default |
| `header` | `"Temperature_C,..."` | A line of text written at the very top of the file, before any data |
| `comments` | `""` | By default NumPy prepends `#` in front of the header and footer lines (treating them as comments). Setting this to an empty string removes that `#`, giving you a clean CSV header |
 
> **Note:** It is good practice to write to a new file (e.g. `climate_results.txt`) rather than overwriting the original input file. Overwriting means you lose the raw data if something goes wrong.
 
---
 
## 13. Useful NumPy Functions Reference
 
NumPy has a large standard library. Here are some of the most commonly used functions, all documented at [numpy.org/doc](https://numpy.org/doc/):
 
| Function | What it does |
|---|---|
| `np.sum(a)` | Sum of all elements (or along an axis) |
| `np.mean(a)` | Arithmetic mean |
| `np.median(a)` | Median value |
| `np.max(a)` / `np.min(a)` | Maximum / minimum element |
| `np.exp(a)` | Element-wise exponential (eˣ) |
| `np.round(a, n)` | Round elements to n decimal places |
| `np.reshape(a, shape)` | Change shape without changing data |
| `np.concatenate((a, b))` | Join arrays along an existing axis |
| `np.stack((a, b))` | Join arrays along a **new** axis |
| `np.split(a, n)` | Split an array into n equal sub-arrays |
| `np.matmul(a, b)` | Matrix multiplication |
| `np.dot(a, b)` | Dot product (also works for matrix multiply) |
| `np.transpose(a)` / `a.T` | Flip rows and columns |
| `np.linalg.eigvals(a)` | Eigenvalues of a square matrix |
 
---
 
## 14. Arithmetic Operations
 
NumPy supports all standard arithmetic operations. These can be applied in two ways — on a **scalar** (a single number) or between **two arrays**.
 
```python
array1 = np.array([[1, 3, 4, 3], [2, 6, 7, 1], [7, 3, 4, 1]])
array2 = np.array([[11, 13, 14, 13], [22, 36, 47, 51], [17, 23, 64, 71]])
```
 
### 14.1 Scalar Operations
 
A scalar operation applies the same value to **every single element** in the array:
 
```python
print(array2 + 2)
```
 
This adds `2` to every element of `array2`. The same works for all operators:
 
| Operator | Example | Effect |
|---|---|---|
| `+` | `array + 2` | Add 2 to every element |
| `-` | `array - 2` | Subtract 2 from every element |
| `*` | `array * 2` | Multiply every element by 2 |
| `/` | `array / 2` | Divide every element by 2 |
| `**` | `array ** 2` | Square every element |
| `%` | `array % 2` | Remainder when divided by 2 |
 
### 14.2 Array + Array (Same Shape)
 
When both arrays have **identical shapes**, the operation is applied element-by-element — each position in one array is paired with the same position in the other:
 
```python
print(array1 + array2)
```
 
`array1` and `array2` both have shape `(3, 4)`, so this works without any issues. If the shapes do not match and broadcasting (explained below) cannot reconcile them, NumPy raises a `ValueError`.
 
---
 
## 15. Broadcasting — Concept First
 
Broadcasting is NumPy's mechanism for performing arithmetic between arrays that have **different shapes**. Instead of requiring you to manually resize arrays, NumPy automatically "stretches" the smaller array to match the larger one — but only under specific rules.
 
### The Broadcasting Rules
 
NumPy compares the shapes of two arrays **from right to left**, dimension by dimension. A dimension is compatible if:
 
1. The sizes are **equal**, or
2. One of them is **1** (NumPy stretches that dimension to match the other)
If neither condition holds for any dimension, NumPy raises a `ValueError`.
 
### Worked Example — Compatible
 
```python
array3 = np.array([2, 3, 4, 5])
print(array1 + array3)
```
 
Shape comparison:
 
```
array1:  (3, 4)
array3:     (4)   ← treated as (1, 4) by padding a 1 on the left
```
 
Step by step:
- Rightmost dimensions: `4` vs `4` → equal ✓
- Next dimension: `3` vs `1` → stretch the `1` to `3` ✓
So NumPy replicates `array3` across all 3 rows before adding:
 
```
array3 becomes:  [[2, 3, 4, 5],
                  [2, 3, 4, 5],
                  [2, 3, 4, 5]]
```
 
Then the addition happens element-by-element as normal.
 
### Worked Example — Incompatible
 
```python
array4 = np.array([1, 3])
print(array1 + array4)  # raises ValueError
```
 
Shape comparison:
 
```
array1:  (3, 4)
array4:     (2)   ← treated as (1, 2)
```
 
- Rightmost dimensions: `4` vs `2` → not equal, and neither is `1` ✗
No matter how many times NumPy replicates `array4`, it will never produce a shape of `(3, 4)`. The operation fails.
 
> **Rule of thumb:** Broadcasting works when the trailing dimensions either match or one of them is 1. If neither is the case, you will get an error.
 
---

## 15.1 Understanding Axis in NumPy Arrays

The `axis` parameter controls **which dimension** an operation works along. When you use `axis`, NumPy collapses that dimension and returns a result with one fewer dimension.

### Axis in 2D Arrays

For a 2D array, you have two axes:
- **`axis=0`** — operates along the **rows** (vertically, top to bottom). Collapses the rows, keeps columns.
- **`axis=1`** — operates along the **columns** (horizontally, left to right). Collapses the columns, keeps rows.

#### 2D Array Example

```python
array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(array_2d.shape)  # (3, 3)
```

Visual representation:
```
     col0  col1  col2
row0 [ 1    2    3  ]
row1 [ 4    5    6  ]
row2 [ 7    8    9  ]
```

**Using `axis=0` — sum down each column:**

```python
result = np.sum(array_2d, axis=0)
print(result)  # [12, 15, 18]
```

Breaking it down:
- Column 0: 1 + 4 + 7 = 12
- Column 1: 2 + 5 + 8 = 15
- Column 2: 3 + 6 + 9 = 18

Result shape: `(3,)` — one value per column.

**Using `axis=1` — sum across each row:**

```python
result = np.sum(array_2d, axis=1)
print(result)  # [6, 15, 24]
```

Breaking it down:
- Row 0: 1 + 2 + 3 = 6
- Row 1: 4 + 5 + 6 = 15
- Row 2: 7 + 8 + 9 = 24

Result shape: `(3,)` — one value per row.

**No axis — sum all elements:**

```python
result = np.sum(array_2d)
print(result)  # 45
```

All elements are summed into a single scalar.

---

### Axis in 3D Arrays

For a 3D array with shape `(2, 3, 4)`, you have three axes:
- **`axis=0`** — operates along the **first dimension** (stacks of matrices). Combines the 2 matrices together.
- **`axis=1`** — operates along the **rows** (second dimension). Collapses rows within each matrix.
- **`axis=2`** — operates along the **columns** (third dimension). Collapses columns within each matrix.

#### 3D Array Example

```python
array_3d = np.array([
    [[1, 2],
     [3, 4]],
    
    [[5, 6],
     [7, 8]]
])

print(array_3d.shape)  # (2, 2, 2)
```

Visual representation:
```
Matrix 0:        Matrix 1:
[1, 2]           [5, 6]
[3, 4]           [7, 8]
```

**Using `axis=0` — sum across matrices:**

```python
result = np.sum(array_3d, axis=0)
print(result)
# [[6, 8],
#  [10, 12]]
```

Breaking it down (element-by-element):
- Position [0,0]: 1 + 5 = 6
- Position [0,1]: 2 + 6 = 8
- Position [1,0]: 3 + 7 = 10
- Position [1,1]: 4 + 8 = 12

Result shape: `(2, 2)` — the two matrices are combined into one.

**Using `axis=1` — sum down rows in each matrix:**

```python
result = np.sum(array_3d, axis=1)
print(result)
# [[4, 6],
#  [12, 14]]
```

Breaking it down by matrix:
- Matrix 0, Column 0: 1 + 3 = 4
- Matrix 0, Column 1: 2 + 4 = 6
- Matrix 1, Column 0: 5 + 7 = 12
- Matrix 1, Column 1: 6 + 8 = 14

Result shape: `(2, 2)` — rows collapsed within each matrix.

**Using `axis=2` — sum across columns in each row:**

```python
result = np.sum(array_3d, axis=2)
print(result)
# [[3, 7],
#  [11, 15]]
```

Breaking it down by matrix:
- Matrix 0, Row 0: 1 + 2 = 3
- Matrix 0, Row 1: 3 + 4 = 7
- Matrix 1, Row 0: 5 + 6 = 11
- Matrix 1, Row 1: 7 + 8 = 15

Result shape: `(2, 2)` — columns collapsed within each row of each matrix.

---

### Axis in 4D Arrays

For a 4D array with shape `(2, 2, 2, 2)`, you have four axes:
- **`axis=0`** — operates along the **first dimension**. Combines different 3D arrays.
- **`axis=1`** — operates along the **second dimension**. Combines different 2D arrays within 3D arrays.
- **`axis=2`** — operates along the **rows** (third dimension). Sums rows within 2D arrays.
- **`axis=3`** — operates along the **columns** (fourth dimension). Sums columns within rows.

#### 4D Array Example

```python
array_4d = np.arange(16).reshape(2, 2, 2, 2)
print(array_4d.shape)  # (2, 2, 2, 2)

print(array_4d)
# [[[[ 0  1]   ← 3D array 0
#    [ 2  3]]
#   
#   [[ 4  5]
#    [ 6  7]]]
#
#  [[[ 8  9]   ← 3D array 1
#    [10 11]]
#   
#   [[12 13]
#    [14 15]]]]
```

**Using `axis=0` — sum across the two 3D arrays:**

```python
result = np.sum(array_4d, axis=0)
print(result.shape)  # (2, 2, 2)

print(result)
# [[[8, 10],
#   [12, 14]],
#
#  [[16, 18],
#   [20, 22]]]
```

Each position combines values from both 3D arrays:
- [0,0,0]: 0 + 8 = 8
- [0,0,1]: 1 + 9 = 10
- [0,1,0]: 2 + 10 = 12
- And so on...

**Using `axis=1` — sum across different 2D arrays within each 3D array:**

```python
result = np.sum(array_4d, axis=1)
print(result.shape)  # (2, 2, 2)

print(result)
# [[[4, 6],
#   [8, 10]],
#
#  [[20, 22],
#   [24, 26]]]
```

For 3D array 0, we combine its two 2D arrays:
- [0, 0]: [0, 1] + [4, 5] = [4, 6]
- [1, 0]: [2, 3] + [6, 7] = [8, 10]

**Using `axis=2` — sum rows within each 2D array:**

```python
result = np.sum(array_4d, axis=2)
print(result.shape)  # (2, 2, 2)

print(result)
# [[[2, 4],
#   [8, 12]],
#
#  [[18, 20],
#   [26, 28]]]
```

For the first element in 3D array 0: [[0, 1], [2, 3]], summing rows:
- Column 0: 0 + 2 = 2
- Column 1: 1 + 3 = 4

**Using `axis=3` — sum columns within each row:**

```python
result = np.sum(array_4d, axis=3)
print(result.shape)  # (2, 2, 2)

print(result)
# [[[1, 5],
#   [9, 13]],
#
#  [[17, 21],
#   [25, 29]]]
```

For the first 2D array [[0, 1], [2, 3]], summing columns:
- Row 0: 0 + 1 = 1
- Row 1: 2 + 3 = 5

---

### Key Takeaway — The Axis Rule

> **When you use `axis=n`, NumPy removes that dimension and performs the operation along it.**

| Array Dimension | axis=0 | axis=1 | axis=2 | axis=3 |
|---|---|---|---|---|
| 1D | Scalar | — | — | — |
| 2D | Columns (3,) | Rows (3,) | — | — |
| 3D | Combine matrices | Sum rows | Sum columns | — |
| 4D | Combine 3D arrays | Combine 2D arrays | Sum rows | Sum columns |

---

## 16. Comparison Operations
 
Just like arithmetic, NumPy supports comparison operators applied **element-by-element** across arrays. The result is a **boolean array** of the same shape — each position holds `True` or `False` depending on whether the condition was met at that position.
 
```python
array5 = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
array6 = np.array([[1, 2, 3, 4], [61, 71, 81, 91]])
 
print(array5 == array6)
```
 
Output:
```
[[ True  True  True  True]
 [False False False False]]
```
 
The first row of both arrays is identical so every element is `True`. The second row differs completely so every element is `False`.
 
All comparison operators work the same way:
 
| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
 
### Counting Matches
 
Because `True` is treated as `1` and `False` as `0` in NumPy, you can call `.sum()` on a boolean array to count how many elements satisfy the condition:
 
```python
total_common = (array5 == array6).sum()
print(total_common)
```
 
This returns `4` — the four positions in the first row where both arrays agree.
 
---
 
## 17. Array Indexing and Slicing
 
NumPy extends Python's indexing to multi-dimensional arrays. Instead of chaining brackets like `array[1][1][0]`, NumPy lets you write all indices in a single bracket separated by commas: `array[1, 1, 0]`. This is cleaner and also faster.
 
### Understanding the Shape of a 3D Array
 
```python
array7 = np.array([
    [[ 1,  2,  3,  4], [ 4,  3,  2,  1]],
    [[11, 21, 31, 41], [42, 33, 24, 14]],
    [[16, 26, 36, 46], [47, 37, 27, 17]]
])
 
print(array7.shape)  # (3, 2, 4)
```
 
`shape = (3, 2, 4)` means:
 
```
Axis 0  →  3 blocks   (the outermost layer — which block?)
Axis 1  →  2 rows     (inside each block — which row?)
Axis 2  →  4 elements (inside each row — which element?)
```
 
Visualised:
 
```
Block 0:   [ 1,  2,  3,  4]   ← row 0
           [ 4,  3,  2,  1]   ← row 1
 
Block 1:   [11, 21, 31, 41]   ← row 0
           [42, 33, 24, 14]   ← row 1
 
Block 2:   [16, 26, 36, 46]   ← row 0
           [47, 37, 27, 17]   ← row 1
```
 
---
 
### Single-Element Indexing — `array7[1, 1, 1]`
 
Each index drills one level deeper, **reducing the result by one dimension at each step**.
 
```python
print(array7[1, 1, 1])
```
 
| Step | Index | What it selects | Result |
|---|---|---|---|
| 1 | `1` | Block at position 1 | `[[11, 21, 31, 41], [42, 33, 24, 14]]` |
| 2 | `1` | Row at position 1 within that block | `[42, 33, 24, 14]` |
| 3 | `1` | Element at position 1 within that row | `33` |
 
Final result: `33`
 
---
 
### Slice Indexing — `array7[1:, 0:1, :2]`
 
A **slice** (`start:stop`) selects a range instead of a single element. Crucially, **slices preserve the dimension** — the axis stays in the output shape.
 
```python
print(array7[1:, 0:1, :2])
```
 
Let's break down each part:
 
**Axis 0 — `1:`**
```
Start from block 1, go to the end.
Selects:  Block 1 and Block 2
```
 
**Axis 1 — `0:1`**
```
Start from row 0, stop before row 1.
Selects:  Row 0 only — but keeps the dimension (shape stays 1, not dropped)
```
 
**Axis 2 — `:2`**
```
Start from the beginning, stop before index 2.
Selects:  Elements at positions 0 and 1
```
 
Tracing through the selected data:
```
Block 1, Row 0, Elements 0–1:  [11, 21]
Block 2, Row 0, Elements 0–1:  [16, 26]
```
 
Output shape: `(2, 1, 2)` — 2 blocks, 1 row each, 2 elements each.
 
---
 
### Mixing Exact Indices and Slices — `array7[1:, 1, 0]`
 
You can freely mix slices and exact indices in the same expression.
 
```python
print(array7[1:, 1, 0])
```
 
| Step | Selector | Type | What it does |
|---|---|---|---|
| Axis 0 | `1:` | Slice | Keeps blocks 1 and 2 — **dimension preserved** |
| Axis 1 | `1` | Exact index | Takes row 1 from each — **dimension dropped** |
| Axis 2 | `0` | Exact index | Takes element 0 from each — **dimension dropped** |
 
Tracing through:
```
Block 1, Row 1, Element 0:  42
Block 2, Row 1, Element 0:  47
```
 
Output: `[42, 47]`  — shape `(2,)` because two dimensions were dropped by the exact indices.
 
---
 
### The Shape Rule — Slices vs Exact Indices
 
This is the single most important rule to remember about NumPy indexing:
 
> **An exact index removes that dimension from the output. A slice keeps it.**
 
```
array7[1,  1,  0]   → shape ()     — all three dims dropped → scalar
array7[1:, 1,  0]   → shape (2,)   — one slice kept
array7[1:, 0:1, :2] → shape (2,1,2)— all three dims kept as slices
```
 
### Using `:` to Select Everything
 
A bare `:` means "all elements along this axis". It is used when you want to preserve the shape on an axis you are not filtering:
 
```python
array7[:, 1, :]   # all blocks, row 1, all elements → shape (3, 4)
array7[0, :, :]   # block 0, all rows, all elements → shape (2, 4)
```
 
---
 
## 18. Special Array Creation Functions
 
So far we have been creating arrays by passing in data manually with `np.array()`. NumPy also provides several built-in functions for generating arrays with a specific pattern or size — useful for initialising data, setting up experiments, or building test matrices without typing every value by hand.
 
---
 
### 18.1 `np.zeros()` — Array of All Zeros
 
Creates an array of the given shape where every element is `0.0`.
 
```python
array8 = np.zeros((3, 2))
print(array8)
```
 
Output:
```
[[0. 0.]
 [0. 0.]
 [0. 0.]]
```
 
Shape `(3, 2)` gives 3 rows and 2 columns. The default dtype is `float64`, which is why values display as `0.` rather than `0`.
 
**When to use:** Initialising an output array before filling it in a loop, or creating a blank template matrix of a known size.
 
---
 
### 18.2 `np.ones()` — Array of All Ones
 
Identical in behaviour to `np.zeros()`, but fills with `1.0` instead.
 
```python
array9 = np.ones((3, 2))
print(array9)
```
 
Output:
```
[[1. 1.]
 [1. 1.]
 [1. 1.]]
```
 
**When to use:** Creating a default weight vector (every factor equally weighted), or as a starting point before scaling values.
 
---
 
### 18.3 `np.eye()` — Identity Matrix
 
Creates a **square** matrix where the diagonal is `1` and everything else is `0`. The single argument is the size of both dimensions.
 
```python
print(np.eye(3))
```
 
Output:
```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```
 
This is the matrix equivalent of the number `1` — multiplying any matrix by the identity matrix leaves it unchanged.
 
**When to use:** Linear algebra operations, setting up transformation matrices, or as a neutral starting point before adding off-diagonal values.
 
---
 
### 18.4 `np.random.rand()` — Uniform Random Values
 
Generates random values sampled from a **uniform distribution** between `0.0` (inclusive) and `1.0` (exclusive). Every value in that range has an equal chance of being picked.
 
You pass the **shape as separate arguments** (not as a tuple):
 
```python
print(np.random.rand(5))
print(np.random.rand(2, 3))
```
 
Example output for `np.random.rand(5)`:
```
[0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]
```
 
Example output for `np.random.rand(2, 3)`:
```
[[0.15601864 0.15599452 0.05808361]
 [0.86617615 0.70807258 0.02058449]]
```
 
Every value is between 0 and 1 with a flat distribution — no value is more likely than another.
 
**When to use:** Randomly initialising model weights, generating synthetic data, or any situation where you need values spread evenly between 0 and 1.
 
---
 
### 18.5 `np.random.randn()` — Standard Normal Random Values
 
Generates random values sampled from a **standard normal (Gaussian) distribution** — centred at `0` with a standard deviation of `1`.
 
```python
print(np.random.randn(5))
print(np.random.randn(2, 3))
```
 
Example output for `np.random.randn(5)`:
```
[ 0.49671415 -0.1382643   0.64768854  1.52302986  1.02272212]
```
 
Example output for `np.random.randn(2, 3)`:
```
[[ 0.22957721 -1.03693648  0.24196227]
 [-1.91328024 -1.72491783 -0.56228753]]
```
 
Values cluster around `0`. Most fall between `-3` and `3`, with values further from `0` becoming increasingly rare.
 
**When to use:** Initialising neural network weights, simulating real-world noise, or any bell-curve distributed data.
 
---
 
### `rand` vs `randn` — Key Difference
 
| | `np.random.rand()` | `np.random.randn()` |
|---|---|---|
| Distribution | Uniform | Normal (Gaussian) |
| Range | Strictly `[0, 1)` | Unbounded (mostly `-3` to `3`) |
| Centre | `0.5` | `0` |
| Use case | Equal probability across a range | Bell-curve, clustered around zero |
 
Both take shape as **separate integer arguments**, not a tuple — unlike `np.zeros()` and `np.ones()`:
 
```python
np.zeros((3, 2))      # ← tuple
np.random.rand(3, 2)  # ← separate ints
```
 
---
 
### 18.6 `np.full()` — Array Filled with a Specific Value
 
Creates an array of the given shape where every element is set to a value you choose.
 
```python
print(np.full([2, 3], 4))
```
 
Output:
```
[[4 4 4]
 [4 4 4]]
```
 
**When to use:** Creating a mask of constant values, pre-filling an array with a default score, or anywhere every cell needs to start with the same number.
 
---
 
### 18.7 `np.arange()` — Range-Based Array
 
Works like Python's built-in `range()`, but returns a NumPy array. Takes `start`, `stop` (exclusive), and `step`.
 
```python
print(np.arange(10, 90, 3))
```
 
Output:
```
[10 13 16 19 22 25 28 31 34 37 40 43 46 49 52 55 58 61 64 67 70 73 76 79 82 85 88]
```
 
#### Combining with `reshape()`
 
`np.arange()` always returns a flat 1D array. Chain `.reshape()` to reorganise it into any shape — as long as the total element count stays the same.
 
```python
print(np.arange(10, 90, 3).reshape(3, 3, 3))
```
 
`np.arange(10, 90, 3)` produces exactly 27 elements. `3 × 3 × 3 = 27` — it fits.
 
Output:
```
[[[10 13 16]
  [19 22 25]
  [28 31 34]]
 
 [[37 40 43]
  [46 49 52]
  [55 58 61]]
 
 [[64 67 70]
  [73 76 79]
  [82 85 88]]]
```
 
#### Using `-1` in reshape
 
Leave one dimension as `-1` and NumPy calculates it automatically:
 
```python
np.arange(10, 90, 3).reshape(3, 3, -1)
# NumPy sees: 3 × 3 × ? = 27  →  ? = 3
```
 
> **Constraint:** Only one dimension can be `-1`. Using it more than once is ambiguous and raises an error.
 
---
 
### 18.8 `np.linspace()` — Equally Spaced Values
 
Instead of a step size, you specify **how many values** you want and NumPy divides the range evenly.
 
```python
print(np.linspace(3, 27, 9))
```
 
Output:
```
[ 3.  6.  9. 12. 15. 18. 21. 24. 27.]
```
 
Arguments: `start=3`, `stop=27`, `num=9`. The gap between each pair is `(27 − 3) / (9 − 1) = 3`. Both endpoints are included by default.
 
#### `arange` vs `linspace`
 
| | `np.arange()` | `np.linspace()` |
|---|---|---|
| You control | The **step size** | The **number of values** |
| Endpoint included? | No (stop is exclusive) | Yes (both ends included) |
| Output dtype | Matches input | Always `float64` |
| Best when... | You know the step | You know how many points you need |
 
---
 
## 19. Downloading Files from the Web
 
So far all our data has either been typed in manually or already sitting on disk. In real projects, data is usually hosted online. Python's built-in `urllib.request` module lets you download a file from any URL and save it directly to a local path — no third-party libraries needed.
 
```python
import urllib.request
 
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
target_path = r"F:\Data-Science-Notes\Practice\climate_data.txt"
 
urllib.request.urlretrieve(url, target_path)
```
 
`urlretrieve(url, filename)` takes two arguments:
 
| Argument | What it does |
|---|---|
| `url` | The full web address of the file to download |
| `filename` | The local path where the downloaded file should be saved |
 
The function makes an HTTP request, streams the response, and writes it to the path you give it. If the file already exists at that path it will be overwritten.
 
> **Windows paths and backslashes:** In Python, a backslash `\` inside a normal string is treated as the start of an escape sequence (e.g. `\n` means newline, `\t` means tab). To write a Windows path safely, prefix the string with `r` to make it a **raw string** — this tells Python to treat every backslash literally: `r"F:\Data-Science-Notes\Practice\climate_data.txt"`. Alternatively you can double every backslash: `"F:\\Data-Science-Notes\\Practice\\climate_data.txt"`. Both are equivalent.
 
---
 
## 20. Reading a File in Python
 
Once a file is on disk you can open it and read its contents using Python's built-in `open()` function combined with a `with` block.
 
```python
with open(r"F:\Data-Science-Notes\Practice\climate_data.txt") as f:
    file_content = f.read()
    print(file_content)
```
 
### Why `with`?
 
The `with` statement is the correct way to open files in Python. It guarantees that the file is **automatically closed** when the block finishes — even if an error occurs inside it. Without `with`, you would have to call `f.close()` manually, and if an exception is raised before that line, the file stays open, which can cause data corruption or resource leaks.
 
### Two Ways to Read
 
| Method | What it returns | Best for |
|---|---|---|
| `f.read()` | One big string containing the entire file | Small files, inspecting raw content |
| `f.readlines()` | A list where each element is one line (including `\n`) | Processing line by line |
 
```python
with open(r"F:\Data-Science-Notes\Practice\climate_data.txt") as f:
    file_lines = f.readlines()
```
 
Each element in `file_lines` still has a `\n` newline character at the end. To remove it, call `.strip()` on individual lines as you process them — not on the list itself (`.strip()` is a string method, not a list method).
 
---
 
## 21. Parsing CSV Data Manually
 
`np.genfromtxt()` handles CSV loading automatically, but understanding how to parse a CSV by hand is important — it gives you full control and works in situations where NumPy is not available or where the data needs custom cleaning logic.
 
A CSV file looks like this:
 
```
Temperature_C,Humidity_%,Rainfall_mm
50.0,90.0,50.0
42.0,65.0,70.0
```
 
The first line is the **header** — it names the columns. Every line after it is a **data row**.
 
### Step 1 — Parsing the Header
 
```python
def parse_header(header_line):
    return header_line.strip().split(",")
```
 
`.strip()` removes any leading/trailing whitespace and the newline character. `.split(",")` breaks the string on every comma and returns a list of column names:
 
```python
parse_header("Temperature_C,Humidity_%,Rainfall_mm\n")
# → ["Temperature_C", "Humidity_%", "Rainfall_mm"]
```
 
Usage — the header is always the first line, so we pass `file_lines[0]`:
 
```python
with open(r"F:\Data-Science-Notes\Practice\climate_data.txt") as f:
    file_lines = f.readlines()
 
headers = parse_header(file_lines[0])
```
 
### Step 2 — Parsing a Data Line
 
```python
def parse_values(data_line):
    values = []
    for item in data_line.strip().split(","):
        if item.strip() == "":
            values.append(0.0)
        else:
            values.append(float(item))
    return values
```
 
For each line, this function:
1. Strips whitespace and splits on commas — same as the header
2. Checks if a cell is **empty** (a missing value in a CSV appears as two consecutive commas, leaving an empty string after splitting)
3. If it is empty, substitutes `0.0` as a safe default
4. Otherwise, converts the string to a `float`
```python
parse_values("50.0,90.0,50.0\n")
# → [50.0, 90.0, 50.0]
 
parse_values("42.0,,70.0\n")
# → [42.0, 0.0, 70.0]   ← missing value replaced with 0.0
```
 
### Step 3 — Combining into a Dictionary
 
```python
def create_dict(headers, values):
    result = {}
    for header, value in zip(headers, values):
        result[header] = value
    return result
```
 
`zip(headers, values)` pairs each column name with its corresponding value. The result is a dictionary where keys are column names and values are the numbers from that row:
 
```python
create_dict(["Temperature_C", "Humidity_%", "Rainfall_mm"], [50.0, 90.0, 50.0])
# → {"Temperature_C": 50.0, "Humidity_%": 90.0, "Rainfall_mm": 50.0}
```
 
Working with dictionaries is much more readable than raw arrays — you access a value by name (`row["Temperature_C"]`) rather than by position (`row[0]`).
 
---
 
## 22. The Complete `read_csv()` Function
 
The three helper functions above are combined into a single `read_csv()` function that reads an entire file and returns a **list of dictionaries** — one dictionary per data row.
 
```python
def read_csv(path):
    result = []
 
    with open(path, "r") as f:
        lines = f.readlines()
        headers = parse_header(lines[0])
 
        for line in lines[1:]:
            values = parse_values(line)
            item_dict = create_dict(headers, values)
            result.append(item_dict)
 
    return result
```
 
Walking through it step by step:
 
| Line | What it does |
|---|---|
| `open(path, "r")` | Opens the file in read mode (`"r"`) |
| `lines = f.readlines()` | Loads all lines into a list |
| `headers = parse_header(lines[0])` | Extracts column names from the first line |
| `for line in lines[1:]` | Iterates over every line **except** the header (`1:` skips index 0) |
| `values = parse_values(line)` | Converts the line's comma-separated text into a list of floats |
| `item_dict = create_dict(headers, values)` | Pairs the values with their column names |
| `result.append(item_dict)` | Adds the completed row-dictionary to the output list |
 
Usage:
 
```python
data = read_csv(r"F:\Data-Science-Notes\Practice\climate_data.txt")
 
print(data[0])
# → {"Temperature_C": 50.0, "Humidity_%": 90.0, "Rainfall_mm": 50.0}
 
print(data[0]["Temperature_C"])
# → 50.0
```
 
---
 
## 23. The `write_csv()` Function
 
The reverse of `read_csv()` — takes a list of dictionaries and writes them back to a CSV file.
 
```python
def write_csv(items, path):
    with open(path, "w") as f:
        if len(items) == 0:
            return
 
        headers = list(items[0].keys())
        f.write(",".join(headers) + "\n")
 
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(",".join(values) + "\n")
```
 
Walking through it step by step:
 
| Line | What it does |
|---|---|
| `open(path, "w")` | Opens the file in write mode (`"w"`). Creates the file if it does not exist; overwrites it if it does |
| `if len(items) == 0: return` | Guard clause — if the list is empty there is nothing to write, so we exit early |
| `headers = list(items[0].keys())` | Extracts column names from the keys of the first dictionary. All rows are assumed to have the same keys |
| `f.write(",".join(headers) + "\n")` | Joins the header list into a comma-separated string and writes it as the first line |
| `item.get(header, "")` | Safely retrieves a value by key. If the key is missing for some reason, it falls back to an empty string rather than crashing |
| `",".join(values) + "\n"` | Joins the values for one row into a comma-separated string and writes it |
 
Usage:
 
```python
data = read_csv(r"F:\Data-Science-Notes\Practice\climate_data.txt")
 
write_csv(data, r"F:\Data-Science-Notes\Practice\climate_data_output.txt")
```
 
> **Note:** `"w"` mode truncates (erases) the file before writing. If you want to **add** rows to an existing file without deleting what is already there, use `"a"` (append mode) instead.
 
---
 
## 24. What the Instructor Means by `os`
 
When your instructor mentions `os` alongside file reading, they are referring to Python's built-in `os` module, which gives you tools to work with the file system itself — not just the content of files.
 
The most commonly used function in this context is `os.path.join()`, which builds file paths correctly for whatever operating system you are on:
 
```python
import os
 
base_dir = r"F:\Data-Science-Notes\Practice"
filename = "climate_data.txt"
 
full_path = os.path.join(base_dir, filename)
# → "F:\Data-Science-Notes\Practice\climate_data.txt"
```
 
On Windows this produces backslash-separated paths; on Mac/Linux it uses forward slashes. Using `os.path.join()` instead of manually concatenating strings with `+` or `\` means your code works on any machine without changes.
 
Other commonly used `os` tools in data science:
 
| Function | What it does |
|---|---|
| `os.path.join(dir, file)` | Build a path from parts, cross-platform |
| `os.path.exists(path)` | Returns `True` if the file or folder exists |
| `os.path.dirname(path)` | Returns just the folder part of a path |
| `os.path.basename(path)` | Returns just the filename part of a path |
| `os.makedirs(path, exist_ok=True)` | Creates a folder (and any missing parent folders) |
| `os.getcwd()` | Returns the current working directory |
| `os.listdir(path)` | Lists all files and folders in a directory |
 
**Practical example** — download a file and save it safely using `os`:
 
```python
import os
import urllib.request
 
base_dir = r"F:\Data-Science-Notes\Practice"
filename = "climate_data.txt"
url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
 
os.makedirs(base_dir, exist_ok=True)
full_path = os.path.join(base_dir, filename)
 
if not os.path.exists(full_path):
    urllib.request.urlretrieve(url, full_path)
    print("Downloaded.")
else:
    print("File already exists, skipping download.")
```
 
This pattern — check if the file exists before downloading — is very common in data science notebooks so you do not re-download large files every time you run the script.