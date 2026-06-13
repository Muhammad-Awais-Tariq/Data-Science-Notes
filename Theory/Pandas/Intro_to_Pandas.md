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
10. [Querying and Filtering Data](#querying-and-filtering-data)
11. [Sorting Data and Handling Faulty Values](#sorting-data-and-handling-faulty-values)
12. [Working with Dates](#working-with-dates)
13. [Grouping and Aggregation](#working-with-dates)

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
df.info()       # See data types and null values
df.describe()   # See statistics

# Step 4: View the data
print(df.head())     # See first 5 rows
print(df.columns)    # See column names
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

---

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
death_rate = total_deaths / total_cases    # Deaths per case
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

---

## Querying and Filtering Data

### Basic Boolean Querying

One of the most powerful features in pandas is the ability to query data using conditional statements. Boolean querying allows you to filter rows based on specific conditions.

When you create a query like `covid_df.new_cases > 1000`, pandas returns a new Series with the same length as the original DataFrame, but instead of containing the data values, it contains **True** or **False** values depending on whether each row satisfies the condition.

### Using Boolean Series as Filters

Once you have a boolean Series (True/False values), you can use it to filter the original DataFrame. When you pass a boolean Series as an index to a DataFrame, pandas returns only the rows where the Series contains **True**, giving you the complete row data for those matches.

### Inline Querying

Instead of creating a separate variable for the boolean Series, you can write the condition directly inline. This is more concise and readable, and produces the same result as creating an intermediate variable.

### Displaying More Rows

By default, pandas displays only the first and last 5 rows of large DataFrames, with `...` in between. If you want to display more or all rows, you can use the `pd.option_context()` function with the `display.max_rows` parameter. You'll need to import `display` from `IPython`.

### Complex Queries with Multiple Columns

You can create more sophisticated queries by combining conditions from multiple columns. For example, you can calculate a ratio between two columns and use that in your query condition. This allows you to find rows that meet complex criteria.

### Adding New Columns

In addition to querying existing columns, you can add new calculated columns to your DataFrame. Simply assign a Series (which can be a calculation involving existing columns) to a new column name using bracket notation.

### Dropping Columns

If you no longer need certain columns, you can remove them using the `.drop()` method. The `inplace=True` parameter tells pandas to modify the original DataFrame directly instead of creating a copy.

### Practical Examples

```python
# Basic boolean query - returns True/False Series
high_new_cases = covid_df.new_cases > 1000
print(high_new_cases)  # Series of True/False values

# Use boolean Series to filter the DataFrame
filtered_df = covid_df[high_new_cases]
print(filtered_df)  # Only rows where new_cases > 1000

# Inline querying - write condition directly
high_new_cases_df = covid_df[covid_df.new_cases > 1000]

# Display more rows than default (first 5 + last 5)
from IPython.display import display
import pandas as pd

with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])

# Complex query with multiple columns
# Find days where positive rate was higher than average
positive_rate_avg = covid_df.new_cases.sum() / covid_df.new_tests.sum()
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate_avg]

# Add a new column with calculated values
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

# Drop a column from the DataFrame
covid_df.drop(columns=['positive_rate'], inplace=True)

# Multiple conditions - rows meeting both criteria
covid_df[(covid_df.new_cases > 1000) & (covid_df.new_deaths > 50)]

# Multiple conditions - rows meeting either criteria
covid_df[(covid_df.new_cases > 1000) | (covid_df.new_deaths > 50)]
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `df['col'] > value` | Create boolean filter | `covid_df.new_cases > 1000` | Series of True/False |
| `df[boolean_series]` | Filter rows where True | `covid_df[high_new_cases]` | Filtered DataFrame |
| `df[df['col'] > value]` | Inline filtering | `covid_df[covid_df.new_cases > 1000]` | Filtered DataFrame |
| `pd.option_context()` | Temporarily change display settings | `pd.option_context('display.max_rows', 100)` | Context manager |
| `df['new_col'] = calc` | Add calculated column | `covid_df['rate'] = covid_df.new_cases / covid_df.new_tests` | New column added |
| `.drop(columns=[...])` | Remove columns | `covid_df.drop(columns=['col1'], inplace=True)` | Column removed |
| `&` (AND operator) | Multiple conditions (both must be true) | `(df['col1'] > 100) & (df['col2'] < 50)` | Combined filter |
| `\|` (OR operator) | Multiple conditions (either must be true) | `(df['col1'] > 100) \| (df['col2'] < 50)` | Combined filter |

---

## Sorting Data and Handling Faulty Values

### Basic Sorting with sort_values()

Sorting is a fundamental operation when working with data. The `.sort_values()` method allows you to order DataFrame rows based on the values in one or more columns. This is useful for ranking data, finding extremes (highest/lowest values), or organizing data for presentation.

The method returns a new DataFrame with rows sorted according to your specification. The original DataFrame remains unchanged unless you use the `inplace=True` parameter.

### Ascending vs Descending Order

By default, `.sort_values()` sorts in ascending order (smallest to largest). To reverse this and sort in descending order (largest to smallest), use the `ascending=False` parameter.

For example, to find the 10 days with the highest number of cases, you would sort by the `new_cases` column in descending order and then use `.head(10)` to get the top 10 rows.

### Identifying Faulty Data

When working with real-world data, you'll often encounter errors or anomalies. These can occur due to data entry mistakes, sensor errors, or system glitches. It's crucial to identify these faulty values before analysis.

For example, in a COVID dataset tracking daily cases, negative values would be physically impossible—cases cannot decrease below zero. Such values indicate an error that needs to be corrected.

### Approaches to Handle Faulty Data

When you discover faulty values, you have several options for how to handle them:

1. **Replace with 0** - Assume the faulty entry should be zero
2. **Replace with Column Average** - Use the mean of all values in that column
3. **Replace with Adjacent Average** - Use the average of the previous and next values (useful for time-series data)
4. **Drop the Row** - Remove the entire row if the data is unreliable

Each approach has trade-offs:
- **Zero replacement** is simple but may distort analysis
- **Column average** preserves overall statistics but may not be contextually appropriate
- **Adjacent average** works well for time-series data where values change gradually
- **Dropping rows** removes the faulty data completely but may lose other valid information in that row

The best approach depends on your data and analysis goals.

### Practical Examples

```python
# Basic sorting - ascending order (default)
sorted_df = covid_df.sort_values('new_cases')

# Sorting in descending order - find highest values
sorted_df = covid_df.sort_values('new_cases', ascending=False)

# Find the 10 days with highest number of cases
top_10_cases = covid_df.sort_values('new_cases', ascending=False).head(10)

# Sort by multiple columns
sorted_df = covid_df.sort_values(['new_cases', 'new_deaths'], ascending=False)

# Identify faulty data
# For example, negative cases (which should never occur)
faulty_rows = covid_df[covid_df.new_cases < 0]

# Approach 1: Replace faulty value with 0
covid_df.at[172, 'new_cases'] = 0

# Approach 2: Replace with column average
column_average = covid_df.new_cases.mean()
covid_df.at[172, 'new_cases'] = column_average

# Approach 3: Replace with average of adjacent values (previous and next)
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases']) / 2

# Approach 4: Drop the entire row
covid_df.drop(172, inplace=True)

# Sort after cleaning to see results
covid_df.sort_values('new_cases', ascending=False).head(10)
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `.sort_values('col')` | Sort by column ascending | `covid_df.sort_values('new_cases')` | Sorted DataFrame |
| `.sort_values('col', ascending=False)` | Sort by column descending | `covid_df.sort_values('new_cases', ascending=False)` | Sorted DataFrame (high to low) |
| `.sort_values([...])` | Sort by multiple columns | `covid_df.sort_values(['col1', 'col2'])` | Sorted by col1, then col2 |
| `.head(n)` + sort | Get top n rows | `covid_df.sort_values('col', ascending=False).head(10)` | Top 10 rows |
| `.tail(n)` + sort | Get bottom n rows | `covid_df.sort_values('col').tail(5)` | Bottom 5 rows |
| `df[df['col'] < 0]` | Find faulty values | `covid_df[covid_df.new_cases < 0]` | Rows with negative cases |
| `.at[row, 'col'] = value` | Replace single value | `covid_df.at[172, 'new_cases'] = 0` | Value replaced |
| `.mean()` | Calculate column average | `covid_df.new_cases.mean()` | Scalar (average value) |
| `.drop(row)` | Remove row | `covid_df.drop(172, inplace=True)` | Row removed |

---

## Working with Dates

### Why Convert Date Columns?

By default, pandas reads date columns as `object` type (plain strings). To unlock date-specific operations like extracting the year, month, or weekday, you need to convert the column to pandas' **datetime** type first.

```python
# Check the current type of the date column
print(covid_df.date)         # Displays as plain strings
print(covid_df.date.dtype)   # Output: object
```

### Converting to Datetime

Use `pd.to_datetime()` to convert a column from `object` to `datetime64`:

```python
covid_df["date"] = pd.to_datetime(covid_df.date)
```

After this, pandas understands the column as actual dates and you can extract components from it.

### Extracting Date Components

Once converted, use `pd.DatetimeIndex()` to extract useful parts of the date into separate columns:

```python
covid_df["year"]    = pd.DatetimeIndex(covid_df.date).year
covid_df["month"]   = pd.DatetimeIndex(covid_df.date).month
covid_df["day"]     = pd.DatetimeIndex(covid_df.date).day
covid_df["weekday"] = pd.DatetimeIndex(covid_df.date).weekday
```

**Weekday reference:**

| Value | Day |
|-------|-----|
| 0 | Monday |
| 1 | Tuesday |
| 2 | Wednesday |
| 3 | Thursday |
| 4 | Friday |
| 5 | Saturday |
| 6 | Sunday |

**Note:** The `.weekday` attribute follows Python's convention where Monday = 0 and Sunday = 6.

### Filtering by Date Components

With the extracted columns, you can filter data for any specific time period:

```python
# Filter for a specific month (e.g., May = month 5)
covid_df_may = covid_df[covid_df.month == 5]

# Filter for a specific year
covid_df_2020 = covid_df[covid_df.year == 2020]

# Filter for a specific weekday (e.g., Sunday = 6)
covid_df_sundays = covid_df[covid_df.weekday == 6]
```

### Calculating Monthly Metrics

Once filtered, you can select only the columns you need and aggregate them:

```python
# Step 1: Filter for the month
covid_df_may = covid_df[covid_df.month == 5]

# Step 2: Select only the relevant columns
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Step 3: Sum them up
covid_df_may_total = covid_df_may_metrics.sum()
```

Or do it all in one line:

```python
covid_df_may_total = covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
```

### Comparing Weekday vs Overall Averages

A common analysis is checking whether a specific day of the week has higher/lower values than the overall average:

```python
# Overall mean
overall_mean = covid_df.new_cases.mean()

# Mean for Sundays only (weekday == 6)
sunday_mean = covid_df[covid_df.weekday == 6].new_cases.mean()

# Compare
print(f"Overall avg cases: {overall_mean:.2f}")
print(f"Sunday avg cases:  {sunday_mean:.2f}")
print(f"Sundays higher? {sunday_mean > overall_mean}")
```

### Practical Examples

```python
# Convert date column to datetime type
covid_df["date"] = pd.to_datetime(covid_df.date)

# Extract date components into new columns
covid_df["year"]    = pd.DatetimeIndex(covid_df.date).year
covid_df["month"]   = pd.DatetimeIndex(covid_df.date).month
covid_df["day"]     = pd.DatetimeIndex(covid_df.date).day
covid_df["weekday"] = pd.DatetimeIndex(covid_df.date).weekday

# Filter for May
covid_df_may = covid_df[covid_df.month == 5]

# Get May totals for key metrics
covid_df_may_total = covid_df_may[['new_cases', 'new_deaths', 'new_tests']].sum()

# Compare Sunday average vs overall average
overall_mean = covid_df.new_cases.mean()
sunday_mean  = covid_df[covid_df.weekday == 6].new_cases.mean()
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `pd.to_datetime(df.col)` | Convert string to datetime | `pd.to_datetime(covid_df.date)` | datetime64 column |
| `pd.DatetimeIndex(df.col).year` | Extract year | `pd.DatetimeIndex(covid_df.date).year` | Series of years |
| `pd.DatetimeIndex(df.col).month` | Extract month (1–12) | `pd.DatetimeIndex(covid_df.date).month` | Series of months |
| `pd.DatetimeIndex(df.col).day` | Extract day (1–31) | `pd.DatetimeIndex(covid_df.date).day` | Series of days |
| `pd.DatetimeIndex(df.col).weekday` | Extract weekday (0=Mon, 6=Sun) | `pd.DatetimeIndex(covid_df.date).weekday` | Series of weekday ints |
| `df[df.month == n]` | Filter by month | `covid_df[covid_df.month == 5]` | Filtered DataFrame |
| `df[df.weekday == n]` | Filter by weekday | `covid_df[covid_df.weekday == 6]` | Sundays only |
| `.mean()` | Average of a column | `covid_df.new_cases.mean()` | Scalar (float) |

## Grouping and Aggregation

### Why Group Data?

Instead of analyzing the entire dataset at once, grouping lets you split data into logical buckets — by month, weekday, year, or any other column — and then apply aggregation functions like sum or mean to each group separately.

### Basic Grouping with groupby()

Use `.groupby()` to group rows by a column, then select the columns you want and apply an aggregation:

```python
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
```

This returns a new DataFrame with 12 rows (one per month), where each row contains the **total** cases, deaths, and tests for that month.

### Using Different Aggregations

Instead of `.sum()`, you can swap in any aggregation function depending on what you need:

```python
# Total per month
covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

# Average per month
covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()

# Max value recorded in each month
covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].max()

# Group by weekday instead of month
covid_df.groupby('weekday')[['new_cases', 'new_deaths', 'new_tests']].mean()
```

### Cumulative Sum with cumsum()

While `.sum()` gives you a single total, `.cumsum()` (cumulative sum) gives you a **running total** — for each row, it shows the sum of all values up to and including that row. This is useful for tracking how a metric has grown over time.

```python
covid_df["total_cases"] = covid_df.new_cases.cumsum()
```

**Example — what cumsum produces:**

| day | new_cases | total_cases (cumsum) |
|-----|-----------|----------------------|
| 1   | 100       | 100                  |
| 2   | 250       | 350                  |
| 3   | 180       | 530                  |
| 4   | 310       | 840                  |

Each value in `total_cases` is the sum of all `new_cases` from day 1 up to that row.

### Practical Examples

```python
# Group by month — total cases, deaths, tests per month
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()

# Group by month — average daily cases per month
covid_month_avg = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].mean()

# Group by weekday — see which day of week had highest avg cases
covid_weekday_df = covid_df.groupby('weekday')[['new_cases', 'new_deaths']].mean()

# Cumulative sum — running total of cases over time
covid_df["total_cases"] = covid_df.new_cases.cumsum()

# Cumulative sum for multiple columns
covid_df["total_deaths"] = covid_df.new_deaths.cumsum()
covid_df["total_tests"]  = covid_df.new_tests.cumsum()
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `.groupby('col')` | Group rows by a column | `covid_df.groupby('month')` | GroupBy object |
| `.groupby()[cols].sum()` | Total per group | `covid_df.groupby('month')[['new_cases']].sum()` | DataFrame with totals |
| `.groupby()[cols].mean()` | Average per group | `covid_df.groupby('month')[['new_cases']].mean()` | DataFrame with averages |
| `.groupby()[cols].max()` | Max value per group | `covid_df.groupby('month')[['new_cases']].max()` | DataFrame with max values |
| `.cumsum()` | Running total over rows | `covid_df.new_cases.cumsum()` | Series with cumulative sum |

## Merging Different DataFrames

### Why Merge DataFrames?

Sometimes the data you need is spread across multiple files. Merging lets you combine two DataFrames into one by matching rows that share a common column — similar to a JOIN in SQL.

**Example scenario:** You have daily COVID data for Italy, and a separate `locations.csv` with population and medical statistics for countries worldwide. To calculate metrics like cases per million, you need both files combined.

### Step 1 — Load and Inspect the Second DataFrame

```python
location_df = pd.read_csv("locations.csv")

# Check if Italy exists in the dataset
location_df[location_df.location == "Italy"]
```

This confirms the data is there and shows you what columns are available before merging.

### Step 2 — Add a Matching Column

For the merge to work, both DataFrames need a column with the **same name and matching values**. Since `covid_df` doesn't have a `location` column, add one manually:

```python
covid_df["location"] = "Italy"
```

Now `covid_df.location` and `location_df.location` both contain `"Italy"` and can be matched.

### Step 3 — Merge the DataFrames

```python
merged_df = covid_df.merge(location_df, on="location")
```

This joins both DataFrames on the `location` column. The result is a new DataFrame that contains all columns from `covid_df` plus all columns from `location_df` — side by side for every matching row.

### Step 4 — Calculate Cases Per Million

Once merged, you have access to the `population` column from `location_df`. You can now calculate meaningful normalized metrics:

```python
merged_df["cases_per_million"] = merged_df.total_cases * 1e6 / merged_df.population
```

**Why cases per million?**

Raw case counts are hard to compare across regions with different population sizes. A country with 10,000 cases means something very different if its population is 100,000 vs 100,000,000.

Cases per million normalizes this — it tells you: *"out of every 1 million people, how many got infected?"*

**How the math works:**

| Value | Meaning |
|-------|---------|
| `total_cases` | Raw number of cases (e.g. 50,000) |
| `population` | Total population (e.g. 60,000,000) |
| `* 1e6` | Multiply by 1,000,000 to scale the result |
| Result | `50000 * 1000000 / 60000000` = **833 cases per million** |

`1e6` is just Python's scientific notation for `1,000,000`. Multiplying first avoids very small decimal results that are hard to read.

### Practical Examples

```python
# Step 1: Load the location data
location_df = pd.read_csv("locations.csv")

# Step 2: Verify Italy exists in location data
location_df[location_df.location == "Italy"]

# Step 3: Add matching column to covid_df
covid_df["location"] = "Italy"

# Step 4: Merge on the shared column
merged_df = covid_df.merge(location_df, on="location")

# Step 5: Calculate normalized metrics
merged_df["cases_per_million"]  = merged_df.total_cases  * 1e6 / merged_df.population
merged_df["deaths_per_million"] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df["tests_per_million"]  = merged_df.total_tests  * 1e6 / merged_df.population
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `pd.read_csv("file.csv")` | Load a second dataset | `pd.read_csv("locations.csv")` | New DataFrame |
| `df[df.col == "value"]` | Check if a value exists | `location_df[location_df.location == "Italy"]` | Filtered rows |
| `df["col"] = value` | Add a constant column | `covid_df["location"] = "Italy"` | New column added |
| `df.merge(other, on="col")` | Merge two DataFrames | `covid_df.merge(location_df, on="location")` | Combined DataFrame |
| `* 1e6 / population` | Normalize to per-million | `total_cases * 1e6 / population` | Cases per million |