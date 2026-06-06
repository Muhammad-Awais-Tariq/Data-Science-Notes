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

## Retrieving Data from a DataFrame
 
### Understanding DataFrame Structure
 
Conceptually, a DataFrame can be categorized as a **dictionary of lists**, where:
- **Keys** = Column headers
- **Values** = Arrays of data
**Important Note:** This is just an analogy for understanding how a DataFrame works. It's not how it's actually implemented internally, but thinking of it this way helps you understand data retrieval.
 
### Example: COVID DataFrame as Dictionary of Lists
 
Consider a COVID DataFrame with the following columns: `date`, `new_cases`, `new_deaths`, `new_tests`
 
As a dictionary of lists, it would conceptually look like this:
 
```python
covid_dict = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'new_cases': [1500, 1620, 1385, 1402],
    'new_deaths': [45, 52, 38, 41],
    'new_tests': [50000, 52000, 48000, 51000]
}
```
 
When this is converted to a DataFrame:
 
```python
import pandas as pd
 
covid_df = pd.DataFrame(covid_dict)
print(covid_df)
```
 
**Output:**
```
        date  new_cases  new_deaths  new_tests
0  2023-01-01       1500          45      50000
1  2023-01-02       1620          52      52000
2  2023-01-03       1385          38      48000
3  2023-01-04       1402          41      51000
```
 
### How This Structure Helps Retrieval
 
Because of this dictionary-like structure:
 
```python
# Access a specific column (like accessing a dictionary key)
covid_df['new_cases']  # Returns all values in new_cases column
 
# Access a specific row by index
covid_df.loc[0]  # Returns all values for the first row
 
# Access a specific cell
covid_df.loc[0, 'new_cases']  # Returns 1500 (first row, new_cases column)
```
 
---
 
## Benefits of DataFrame Structure
 
### Why Pandas Uses This Structure
 
Representing data as a dictionary of lists provides several key benefits:
 
### 1. **Efficient Storage for Same Data Types**
 
Since all values in a column typically store data of the same type, it's efficient to store them as arrays.
 
```python
# Each column stores a single data type
covid_df['new_cases']  # All integers
covid_df['date']       # All strings/dates
```
 
**Benefit:** Arrays of the same type use less memory and are faster to process.
 
### 2. **Simple Row Value Retrieval**
 
Retrieving the value of a given row is simple—you just provide the index of that row to the column to extract the data.
 
```python
# Get new_cases for row 2
cases_row_2 = covid_df.loc[2, 'new_cases']  # Returns 1385
 
# Get entire row 2
row_2_data = covid_df.loc[2]
```
 
### 3. **Compact Representation**
 
This representation is more compact compared to alternatives. For example:
 
| Format | Structure | Example | Space Used |
|--------|-----------|---------|-----------|
| **Dictionary of Lists** (pandas) | `{'col1': [val1, val2], 'col2': [val3, val4]}` | Efficient - column names stored once | ✅ Minimal |
| **List of Dictionaries** | `[{'col1': val1, 'col2': val3}, {'col1': val2, 'col2': val4}]` | Column names repeated for each row | ❌ More space |
 
**Why List of Dictionaries is Less Efficient:**
 
```python
# Less efficient approach - column names repeated
covid_list_dicts = [
    {'date': '2023-01-01', 'new_cases': 1500, 'new_deaths': 45, 'new_tests': 50000},
    {'date': '2023-01-02', 'new_cases': 1620, 'new_deaths': 52, 'new_tests': 52000},
    {'date': '2023-01-03', 'new_cases': 1385, 'new_deaths': 38, 'new_tests': 48000},
    {'date': '2023-01-04', 'new_cases': 1402, 'new_deaths': 41, 'new_tests': 51000}
]
# Notice: 'date', 'new_cases', 'new_deaths', 'new_tests' keys are repeated 4 times!
```
 
**Benefit:** The dictionary of lists approach stores column names only once, resulting in significantly less memory usage, especially with large datasets.