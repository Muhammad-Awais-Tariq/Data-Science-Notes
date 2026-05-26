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

