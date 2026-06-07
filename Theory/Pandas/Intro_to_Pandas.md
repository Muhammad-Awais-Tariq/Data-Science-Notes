# Pandas Notes - Complete Guide

## Table of Contents
1. [Reading Data from CSV](#reading-data-from-csv)
2. [Understanding DataFrames](#understanding-dataframes)
3. [Exploring Your Data](#exploring-your-data)
4. [Summary of Methods](#summary-of-methods)
5. [Quick Example Workflow](#quick-example-workflow)
6. [Retrieving Data from a DataFrame](#retrieving-data-from-a-dataframe)
7. [Benefits of DataFrame Structure](#benefits-of-dataframe-structure)
8. [Accessing and Indexing DataFrame Values](#accessing-and-indexing-dataframe-values)
9. [Analyzing Data from a DataFrame](#analyzing-data-from-a-dataframe)

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

---

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

---

## Accessing and Indexing DataFrame Values

### Different Ways to Access Data

Once you have a DataFrame, you need to be able to retrieve specific values, columns, or rows. Pandas provides several methods for this, each with different use cases and advantages.

### Accessing Columns

A DataFrame is conceptually a dictionary of lists, so you can access entire columns similar to how you access dictionary values. When you access a column, pandas returns a **Series** object, which is a one-dimensional array with additional functions built in.

You can access a column in two ways:
1. **Using bracket notation** - `covid_df['column_name']` - works for all column names
2. **Using dot notation** - `covid_df.column_name` - only works if the column name has no spaces or special characters

### Accessing Specific Values

To access a single value at a specific row and column, use the `.at[]` method. This is more efficient and cleaner than using bracket notation with nested indices.

**Important:** The `.at[]` method syntax is `dataframe.at[row, column]` where row is first and column is second.

### Accessing Multiple Columns

You can select multiple columns at once by passing a list of column names. This returns a new DataFrame containing only those columns. However, this is a view of the original data, so any modifications to it will affect the original DataFrame. If you need an independent copy, use the `.copy()` method.

### Accessing Rows

You can access specific rows using the `.loc[]` method with row indices. This returns a Series object containing all values for that row. You can also slice rows using a range (e.g., `loc[start:end]`), and you can use `.head()` and `.tail()` methods to view the first or last n rows respectively.

### Sampling Data

The `.sample()` method randomly selects n rows from the DataFrame. This is useful when you want a random subset of your data for testing or analysis.

### Handling Missing Values

When pandas encounters missing data in your DataFrame, it represents it as **NaN** (Not a Number). The type of NaN is actually `float`, even though it doesn't represent a number. You can use methods like `.first_valid_index()` to find the first non-NaN value in a column.

### Practical Examples

Here are the main methods for accessing and indexing DataFrame values:

```python
# Access an entire column - returns a Series
print(covid_df['new_cases'])  # Returns all values in the new_cases column

# Check the type of a column
print(type(covid_df['new_cases']))  # Output: <class 'pandas.core.series.Series'>

# Access a specific value using bracket notation (less convenient)
print(covid_df['new_cases'][246])  # Value at row 246 in new_cases column

# Access a specific value using the .at[] method (recommended)
print(covid_df.at[241, 'new_cases'])  # First parameter is row, second is column
# Note: .at[] only works for column names without spaces or special characters

# Access a column using dot notation (if column name has no spaces/special chars)
print(covid_df.new_cases)  # Same as covid_df['new_cases']

# Access multiple columns (returns a DataFrame subset)
print(covid_df[['new_cases', 'date']])  # Returns a DataFrame with 2 columns
# Note: This is a view of the original, so changes affect the original DataFrame

# Create an independent copy if you need to modify without affecting original
subset = covid_df[['new_cases', 'date']].copy()

# Access a specific row - returns a Series
print(covid_df.loc[243])  # Returns all column values for row 243

# View first or last n rows
print(covid_df.head(5))  # First 5 rows
print(covid_df.tail(5))  # Last 5 rows

# Access a range of rows
print(covid_df.loc[108:113])  # Rows from index 108 to 113 (inclusive)

# Find the first non-NaN value in a column
print(covid_df.new_tests.first_valid_index())  # Returns the index of first non-NaN value

# Get a random sample of rows
print(covid_df.sample(10))  # Returns 10 randomly selected rows
```

### Quick Reference Table

| Method | Purpose | Returns | Example |
|--------|---------|---------|---------|
| `df['col']` | Access a column | Series | `covid_df['new_cases']` |
| `df.col` | Access a column (no spaces/special chars) | Series | `covid_df.new_cases` |
| `df.at[row, col]` | Access a specific value | Scalar value | `covid_df.at[241, 'new_cases']` |
| `df[['col1', 'col2']]` | Access multiple columns | DataFrame | `covid_df[['new_cases', 'date']]` |
| `df.loc[row]` | Access a specific row | Series | `covid_df.loc[243]` |
| `df.loc[start:end]` | Access a range of rows | DataFrame | `covid_df.loc[108:113]` |
| `df.head(n)` | View first n rows | DataFrame | `covid_df.head(5)` |
| `df.tail(n)` | View last n rows | DataFrame | `covid_df.tail(5)` |
| `df.sample(n)` | Random sample of n rows | DataFrame | `covid_df.sample(10)` |
| `df.first_valid_index()` | Find first non-NaN index | Index | `covid_df.new_tests.first_valid_index()` |

## Analyzing Data from a DataFrame
 
### Basic Aggregation and Summation
 
Once you have data in a DataFrame, you often want to perform calculations and analysis on it. The simplest operations involve aggregating data across rows to get totals or summaries.
 
The `.sum()` method calculates the sum of all values in a Series (column). This is similar to NumPy's sum function and is useful for getting totals like total cases, total deaths, or total tests conducted.
 
```python
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
```
 
### Calculating Rates and Ratios
 
Beyond just summing values, you can calculate meaningful metrics by performing operations on aggregated data. For example, you can calculate the death rate by dividing total deaths by total cases. This tells you the ratio of deaths to the number of cases.
 
Similarly, you can calculate the positive test rate by dividing total cases by total tests, which shows what percentage of tests resulted in positive cases.
 
```python
death_rate = total_deaths / total_cases  # Deaths per case
positive_rate = total_cases / total_tests  # Positive cases per test
```
 
### Incorporating Historical Data
 
Often, your DataFrame starts with a specific date and doesn't include all historical data. You may need to incorporate initial values from before your dataset begins. You can add these initial values to your aggregated DataFrame values to get a complete picture.
 
For example, if your dataset tracks new tests starting from a certain date, but you know there were tests conducted before that date, you can add that initial count to your calculation:
 
```python
initial_tests = 935310  # Tests conducted before dataset starts
total_tests = initial_tests + covid_df.new_tests.sum()
total_cases = covid_df.new_cases.sum()
 
# Now calculate the positive rate with complete historical data
positive_rate = total_cases / total_tests
```
 
### Practical Examples
 
Here are common analysis operations on DataFrames:
 
```python
# Calculate total cases and deaths from the DataFrame
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
 
# Calculate death rate (deaths per case)
death_rate = total_deaths / total_cases
 
# Calculate total tests conducted
total_tests = covid_df.new_tests.sum()
 
# Incorporate initial values into calculations
# If there were 935310 tests before the data starts
initial_tests = 935310
total_tests_complete = initial_tests + covid_df.new_tests.sum()
 
# Calculate positive test rate (cases per test) with complete historical data
positive_rate = total_cases / total_tests_complete
```
 
### Quick Reference Table
 
| Operation | Purpose | Example | Result Type |
|-----------|---------|---------|-------------|
| `.sum()` | Sum all values in a column | `covid_df.new_cases.sum()` | Scalar (int/float) |
| `/` (Division) | Calculate ratio or rate | `total_deaths / total_cases` | Scalar (float) |
| `+` (Addition) | Add values together | `initial_value + series.sum()` | Scalar (int/float) |