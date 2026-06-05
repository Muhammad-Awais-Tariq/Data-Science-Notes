# Pandas Notes - Complete Guide

## Table of Contents
1. [Reading Data from CSV](#reading-data-from-csv)
2. [Understanding DataFrames](#understanding-dataframes)
3. [Exploring Your Data](#exploring-your-data)
4. [Summary of Methods](#summary-of-methods)

---

## Reading Data from CSV

### Basic CSV Import

To read data from a CSV file using pandas, use the `read_csv()` function:

```python
import pandas as pd

covid_df = pd.read_csv("path/to/your/file.csv")
```

### What is a DataFrame?

The data read from a CSV file is stored in a **DataFrame** object. A DataFrame is the primary data structure in pandas for:
- Storing tabular (table-like) data
- Working with rows and columns
- Data manipulation and analysis

**Note:** It's a common convention to use the `_df` suffix to identify variables that store DataFrames (e.g., `covid_df`, `sales_df`).

### Basic Data Inspection

```python
print(covid_df)
```

When you print a DataFrame, you'll see:
- The structure of your data
- Total number of columns and rows
- **NaN** values appear where data is missing/empty
- First and last few rows of the data

---

## Understanding DataFrames

### What is NaN?

| Term | Meaning | Example |
|------|---------|---------|
| **NaN** | Not a Number | Empty cell in the CSV file |
| **Null Values** | Missing data points | Absence of value in a cell |

When a cell has no data, pandas displays `NaN`. These are important to identify for data cleaning and preprocessing.

---

## Exploring Your Data

### 1. Get DataFrame Information

```python
covid_df.info()
```

**Returns:**
- All column names
- Number of non-null values in each column
- Data type of each column
- Memory usage of the DataFrame

**Note:** If pandas can't determine the exact data type of a column, it assigns the `object` data type (usually for mixed types or strings).

### 2. Get Statistical Summary

```python
covid_df.describe()
```

**Returns statistical metrics for each numeric column:**

| Metric | Description |
|--------|-------------|
| **count** | Number of non-null values |
| **mean** | Average value |
| **std** | Standard deviation |
| **min** | Minimum value |
| **25%** | First quartile (25th percentile) |
| **50%** | Median (50th percentile) |
| **75%** | Third quartile (75th percentile) |
| **max** | Maximum value |

### 3. Get Column Names

```python
covid_df.columns
```

**Returns:** A list of all column names in the DataFrame

```python
# Example output:
Index(['Date', 'Country', 'Cases', 'Deaths', 'Recovered'], dtype='object')
```

### 4. Get DataFrame Shape

```python
covid_df.shape
```

**Returns:** A tuple showing `(number_of_rows, number_of_columns)`

```python
# Example output:
(5000, 5)  # 5000 rows and 5 columns
```

---

## Summary of Methods

| Method | Purpose | Returns | Example |
|--------|---------|---------|---------|
| `.info()` | Get info about columns, data types, and null values | Column information | `covid_df.info()` |
| `.describe()` | Get statistical summary of numeric columns | Statistics (mean, std, min, max, etc.) | `covid_df.describe()` |
| `.columns` | Get all column names | Index object with column names | `covid_df.columns` |
| `.shape` | Get dimensions of DataFrame | Tuple (rows, columns) | `covid_df.shape` |
| `.head()` | View first few rows | First 5 rows by default | `covid_df.head(10)` |
| `.tail()` | View last few rows | Last 5 rows by default | `covid_df.tail(10)` |

---

## Quick Example Workflow

```python
import pandas as pd

# Step 1: Read the data
df = pd.read_csv("covid_data.csv")

# Step 2: Check the shape
print(f"Shape: {df.shape}")  # Output: Shape: (5000, 5)

# Step 3: Explore the data
df.info()  # See data types and null values
df.describe()  # See statistics

# Step 4: View the data
print(df.head())  # See first 5 rows
print(df.columns)  # See column names
```
