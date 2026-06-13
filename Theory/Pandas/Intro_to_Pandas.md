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
13. [Grouping and Aggregation](#grouping-and-aggregation)
14. [Merging Different DataFrames](#merging-different-dataframes)
15. [Writing Data Back to Files](#writing-data-back-to-files)
16. [Basic Plotting in Pandas](#basic-plotting-in-pandas)

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

### 1. Efficient Storage for Same Data Types

Since all values in a column typically store data of the same type, it's efficient to store them as arrays.

```python
# Each column stores a single data type
covid_df['new_cases']  # All integers
covid_df['date']       # All strings/dates
```

**Benefit:** Arrays of the same type use less memory and are faster to process.

### 2. Simple Row Value Retrieval

Retrieving the value of a given row is simple — you just provide the index of that row to the column to extract the data.

```python
# Get new_cases for row 2
cases_row_2 = covid_df.loc[2, 'new_cases']  # Returns 1385

# Get entire row 2
row_2_data = covid_df.loc[2]
```

### 3. Compact Representation

This representation is more compact compared to alternatives. For example:

| Format | Structure | Space Used |
|--------|-----------|-----------|
| **Dictionary of Lists** (pandas) | Column names stored once, values in arrays | ✅ Minimal |
| **List of Dictionaries** | Column names repeated for every single row | ❌ More space |

**Why List of Dictionaries is Less Efficient:**

```python
# Less efficient approach - column names repeated for every row
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
print(covid_df['new_cases'])

# Check the type of a column
print(type(covid_df['new_cases']))  # Output: <class 'pandas.core.series.Series'>

# Access a specific value using bracket notation (less convenient)
print(covid_df['new_cases'][246])  # Value at row 246

# Access a specific value using .at[] (recommended)
print(covid_df.at[241, 'new_cases'])  # Row first, column second

# Access a column using dot notation
print(covid_df.new_cases)  # Same as covid_df['new_cases']

# Access multiple columns - returns a DataFrame
print(covid_df[['new_cases', 'date']])

# Create an independent copy to avoid modifying the original
subset = covid_df[['new_cases', 'date']].copy()

# Access a specific row - returns a Series
print(covid_df.loc[243])

# View first or last n rows
print(covid_df.head(5))
print(covid_df.tail(5))

# Access a range of rows
print(covid_df.loc[108:113])  # Rows 108 to 113 (inclusive)

# Find the first non-NaN value in a column
print(covid_df.new_tests.first_valid_index())

# Get a random sample of rows
print(covid_df.sample(10))
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

The `.sum()` method calculates the sum of all values in a Series (column). This is useful for getting totals like total cases, total deaths, or total tests conducted.

```python
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()
```

### Calculating Rates and Ratios

Beyond just summing values, you can calculate meaningful metrics by performing operations on aggregated data. For example, you can calculate the death rate by dividing total deaths by total cases.

```python
death_rate = total_deaths / total_cases    # Deaths per case
positive_rate = total_cases / total_tests  # Positive cases per test
```

### Incorporating Historical Data

Often, your DataFrame starts with a specific date and doesn't include all historical data. You may need to incorporate initial values from before your dataset begins:

```python
initial_tests = 935310  # Tests conducted before dataset starts
total_tests = initial_tests + covid_df.new_tests.sum()
total_cases = covid_df.new_cases.sum()

positive_rate = total_cases / total_tests
```

### Practical Examples

```python
# Calculate total cases and deaths
total_cases = covid_df.new_cases.sum()
total_deaths = covid_df.new_deaths.sum()

# Calculate death rate (deaths per case)
death_rate = total_deaths / total_cases

# Calculate total tests conducted
total_tests = covid_df.new_tests.sum()

# Incorporate historical data before dataset start
initial_tests = 935310
total_tests_complete = initial_tests + covid_df.new_tests.sum()

# Calculate positive test rate with complete historical data
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

One of the most powerful features in pandas is the ability to query data using conditional statements. When you create a query like `covid_df.new_cases > 1000`, pandas returns a Series of **True** or **False** values for every row depending on whether the condition is met.

### Using Boolean Series as Filters

Once you have a boolean Series, you can pass it as an index to the DataFrame. Pandas returns only the rows where the value is **True**.

### Inline Querying

Instead of creating a separate variable for the boolean Series, you can write the condition directly inline — more concise and produces the same result.

### Adding New Columns

You can add new calculated columns to your DataFrame by assigning a Series to a new column name using bracket notation.

### Dropping Columns

Remove unwanted columns using the `.drop()` method. The `inplace=True` parameter modifies the original DataFrame directly instead of creating a copy.

### Practical Examples

```python
# Basic boolean query - returns True/False Series
high_new_cases = covid_df.new_cases > 1000
print(high_new_cases)

# Use boolean Series to filter the DataFrame
filtered_df = covid_df[high_new_cases]

# Inline querying - write condition directly
high_new_cases_df = covid_df[covid_df.new_cases > 1000]

# Display more rows than default
from IPython.display import display

with pd.option_context('display.max_rows', 100):
    display(covid_df[covid_df.new_cases > 1000])

# Complex query using a ratio between two columns
positive_rate_avg = covid_df.new_cases.sum() / covid_df.new_tests.sum()
high_ratio_df = covid_df[covid_df.new_cases / covid_df.new_tests > positive_rate_avg]

# Add a new calculated column
covid_df['positive_rate'] = covid_df.new_cases / covid_df.new_tests

# Drop a column
covid_df.drop(columns=['positive_rate'], inplace=True)

# Multiple conditions - both must be true (AND)
covid_df[(covid_df.new_cases > 1000) & (covid_df.new_deaths > 50)]

# Multiple conditions - either must be true (OR)
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
| `&` (AND) | Both conditions must be true | `(df['col1'] > 100) & (df['col2'] < 50)` | Combined filter |
| `\|` (OR) | Either condition must be true | `(df['col1'] > 100) \| (df['col2'] < 50)` | Combined filter |

---

## Sorting Data and Handling Faulty Values

### Basic Sorting with sort_values()

The `.sort_values()` method orders DataFrame rows based on the values in one or more columns. It returns a new sorted DataFrame — the original stays unchanged unless you use `inplace=True`.

### Ascending vs Descending Order

By default, `.sort_values()` sorts in ascending order (smallest to largest). Use `ascending=False` to reverse this.

### Identifying Faulty Data

Real-world data often contains errors — negative case counts, impossibly large values, or data entry mistakes. It's important to identify and handle these before analysis.

### Approaches to Handle Faulty Data

When you discover faulty values, you have several options:

1. **Replace with 0** — simple but may distort analysis
2. **Replace with Column Average** — preserves overall statistics but may not be contextually appropriate
3. **Replace with Adjacent Average** — works well for time-series data where values change gradually
4. **Drop the Row** — removes faulty data completely but loses other valid values in that row

The best approach depends on your data and analysis goals.

### Practical Examples

```python
# Basic sorting - ascending order (default)
sorted_df = covid_df.sort_values('new_cases')

# Sorting in descending order
sorted_df = covid_df.sort_values('new_cases', ascending=False)

# Find the 10 days with highest number of cases
top_10_cases = covid_df.sort_values('new_cases', ascending=False).head(10)

# Sort by multiple columns
sorted_df = covid_df.sort_values(['new_cases', 'new_deaths'], ascending=False)

# Identify faulty data (e.g. negative cases — physically impossible)
faulty_rows = covid_df[covid_df.new_cases < 0]

# Approach 1: Replace with 0
covid_df.at[172, 'new_cases'] = 0

# Approach 2: Replace with column average
covid_df.at[172, 'new_cases'] = covid_df.new_cases.mean()

# Approach 3: Replace with average of adjacent rows
covid_df.at[172, 'new_cases'] = (covid_df.at[171, 'new_cases'] + covid_df.at[173, 'new_cases']) / 2

# Approach 4: Drop the entire row
covid_df.drop(172, inplace=True)
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `.sort_values('col')` | Sort ascending | `covid_df.sort_values('new_cases')` | Sorted DataFrame |
| `.sort_values('col', ascending=False)` | Sort descending | `covid_df.sort_values('new_cases', ascending=False)` | Sorted DataFrame (high to low) |
| `.sort_values([...])` | Sort by multiple columns | `covid_df.sort_values(['col1', 'col2'])` | Sorted by col1, then col2 |
| `.head(n)` + sort | Get top n rows | `covid_df.sort_values('col', ascending=False).head(10)` | Top 10 rows |
| `df[df['col'] < 0]` | Find faulty values | `covid_df[covid_df.new_cases < 0]` | Rows with negative values |
| `.at[row, 'col'] = value` | Replace a single value | `covid_df.at[172, 'new_cases'] = 0` | Value replaced |
| `.mean()` | Calculate column average | `covid_df.new_cases.mean()` | Scalar (float) |
| `.drop(row)` | Remove a row | `covid_df.drop(172, inplace=True)` | Row removed |

---

## Working with Dates

### Why Convert Date Columns?

By default, pandas reads date columns as `object` type (plain strings). To unlock date-specific operations like extracting the year, month, or weekday, you need to convert the column to pandas' **datetime** type first.

```python
# Check the current type of the date column
print(covid_df.date.dtype)   # Output: object
```

### Converting to Datetime

Use `pd.to_datetime()` to convert a column from `object` to `datetime64`:

```python
covid_df["date"] = pd.to_datetime(covid_df.date)
```

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

**Note:** Monday = 0 and Sunday = 6.

### Filtering by Date Components

```python
# Filter for a specific month (e.g., May = month 5)
covid_df_may = covid_df[covid_df.month == 5]

# Filter for a specific year
covid_df_2020 = covid_df[covid_df.year == 2020]

# Filter for Sundays only
covid_df_sundays = covid_df[covid_df.weekday == 6]
```

### Calculating Monthly Metrics

```python
# Step 1: Filter for the month
covid_df_may = covid_df[covid_df.month == 5]

# Step 2: Select only the relevant columns
covid_df_may_metrics = covid_df_may[['new_cases', 'new_deaths', 'new_tests']]

# Step 3: Sum them up
covid_df_may_total = covid_df_may_metrics.sum()

# Or do it all in one line
covid_df_may_total = covid_df[covid_df.month == 5][['new_cases', 'new_deaths', 'new_tests']].sum()
```

### Comparing Weekday vs Overall Averages

```python
# Overall mean
overall_mean = covid_df.new_cases.mean()

# Mean for Sundays only
sunday_mean = covid_df[covid_df.weekday == 6].new_cases.mean()

print(f"Overall avg cases: {overall_mean:.2f}")
print(f"Sunday avg cases:  {sunday_mean:.2f}")
print(f"Sundays higher? {sunday_mean > overall_mean}")
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `pd.to_datetime(df.col)` | Convert string to datetime | `pd.to_datetime(covid_df.date)` | datetime64 column |
| `pd.DatetimeIndex(df.col).year` | Extract year | `pd.DatetimeIndex(covid_df.date).year` | Series of years |
| `pd.DatetimeIndex(df.col).month` | Extract month (1–12) | `pd.DatetimeIndex(covid_df.date).month` | Series of months |
| `pd.DatetimeIndex(df.col).day` | Extract day (1–31) | `pd.DatetimeIndex(covid_df.date).day` | Series of days |
| `pd.DatetimeIndex(df.col).weekday` | Extract weekday (0=Mon, 6=Sun) | `pd.DatetimeIndex(covid_df.date).weekday` | Series of ints |
| `df[df.month == n]` | Filter by month | `covid_df[covid_df.month == 5]` | Filtered DataFrame |
| `df[df.weekday == n]` | Filter by weekday | `covid_df[covid_df.weekday == 6]` | Sundays only |
| `.mean()` | Average of a column | `covid_df.new_cases.mean()` | Scalar (float) |

---

## Grouping and Aggregation

### Why Group Data?

Instead of analyzing the entire dataset at once, grouping lets you split data into logical buckets — by month, weekday, year, or any other column — and then apply aggregation functions like sum or mean to each group separately.

### Basic Grouping with groupby()

Use `.groupby()` to group rows by a column, then select the columns you want and apply an aggregation:

```python
covid_month_df = covid_df.groupby('month')[['new_cases', 'new_deaths', 'new_tests']].sum()
```

This returns a DataFrame with one row per month, where each row contains the **total** cases, deaths, and tests for that month.

### Using Different Aggregations

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

While `.sum()` gives you a single total, `.cumsum()` gives you a **running total** — for each row, it shows the sum of all values up to and including that row. This is useful for tracking how a metric grows over time.

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

# Group by weekday — see which day had highest avg cases
covid_weekday_df = covid_df.groupby('weekday')[['new_cases', 'new_deaths']].mean()

# Cumulative sum — running total of cases over time
covid_df["total_cases"]  = covid_df.new_cases.cumsum()
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

---

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

This joins both DataFrames on the `location` column. The result contains all columns from both DataFrames side by side for every matching row.

### Step 4 — Calculate Cases Per Million

Once merged, you have access to the `population` column from `location_df` and can calculate normalized metrics:

```python
merged_df["cases_per_million"] = merged_df.total_cases * 1e6 / merged_df.population
```

**Why cases per million?**

Raw case counts are hard to compare across regions with different population sizes. A country with 10,000 cases means something very different if its population is 100,000 vs 100,000,000. Cases per million normalizes this — it tells you: *"out of every 1 million people, how many got infected?"*

**How the math works:**

| Value | Meaning |
|-------|---------|
| `total_cases` | Raw number of cases (e.g. 50,000) |
| `population` | Total population (e.g. 60,000,000) |
| `* 1e6` | Multiply by 1,000,000 to scale the result |
| Result | `50000 * 1000000 / 60000000` = **833 cases per million** |

`1e6` is Python's scientific notation for `1,000,000`. Multiplying first avoids very small decimal results that are hard to read.

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

---

## Writing Data Back to Files

### Why Create a Clean DataFrame First?

Before writing data to a file, it's good practice to create a trimmed DataFrame containing only the columns you actually need. This keeps your output file clean and avoids carrying over intermediate or redundant columns from earlier in your analysis.

```python
result_df = merged_df[['date', 'new_cases', 'total_cases', 'cases_per_million']]
```

### Writing to CSV

Use `.to_csv()` to save your DataFrame as a CSV file:

```python
result_df.to_csv("results.csv", index=False)
```

**The `index` parameter:**

By default, pandas writes the row index (0, 1, 2, 3...) as an extra column in the CSV. This is usually unwanted since it's just a positional number, not real data. Setting `index=False` skips it.

| Setting | Output |
|---------|--------|
| `index=True` (default) | Row numbers included as first column |
| `index=False` | Row numbers excluded — cleaner output |

**NaN values:** Any missing values in your DataFrame are written as empty cells in the CSV automatically — no extra handling needed.

### Writing to Other File Formats

Just like `pd.read_csv()` has equivalents for other formats, `.to_csv()` does too:

```python
# CSV — most common, works everywhere
result_df.to_csv("results.csv", index=False)

# Excel — useful for sharing with non-technical users
result_df.to_excel("results.xlsx", index=False)

# JSON — useful for web apps or APIs
result_df.to_json("results.json")

# Parquet — efficient binary format for large datasets
result_df.to_parquet("results.parquet", index=False)
```

### Practical Examples

```python
# Step 1: Select only the columns you need
result_df = merged_df[['date', 'new_cases', 'total_cases', 'cases_per_million']]

# Step 2: Preview before writing to catch any issues
print(result_df.head())
print(result_df.shape)

# Step 3: Write to CSV
result_df.to_csv("results.csv", index=False)

# Writing to other formats
result_df.to_excel("results.xlsx", index=False)
result_df.to_json("results.json")
result_df.to_parquet("results.parquet", index=False)
```

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `df[['col1', 'col2']]` | Select specific columns | `merged_df[['date', 'new_cases']]` | Trimmed DataFrame |
| `.to_csv("file.csv")` | Write to CSV | `result_df.to_csv("results.csv")` | CSV file saved |
| `index=False` | Skip row numbers in output | `result_df.to_csv("results.csv", index=False)` | Cleaner CSV |
| `.to_excel("file.xlsx")` | Write to Excel | `result_df.to_excel("results.xlsx", index=False)` | Excel file saved |
| `.to_json("file.json")` | Write to JSON | `result_df.to_json("results.json")` | JSON file saved |
| `.to_parquet("file.parquet")` | Write to Parquet | `result_df.to_parquet("results.parquet")` | Parquet file saved |

---

## Basic Plotting in Pandas

### Why Plot Directly in Pandas?

For advanced visualizations you would typically use libraries like **Matplotlib** or **Seaborn**, but pandas has built-in `.plot()` support for quick, basic charts without any extra setup. It's useful for fast exploration during analysis.

### Basic Line Plot

```python
result_df.new_cases.plot()
```

By default, pandas uses the row index (0, 1, 2...) on the x-axis, which makes it hard to read dates or meaningful values.

### Setting the Date as the Index

To get dates on the x-axis instead of row numbers, set the `date` column as the DataFrame index:

```python
result_df.set_index('date', inplace=True)
```

Now any plot will automatically use dates on the x-axis, making your graphs much more readable. You can also use the date index to access data for a specific date directly:

```python
result_df.loc['2020-05-15']  # Get all values for a specific date
```

### Plotting Multiple Columns

Calling `.plot()` on multiple columns in sequence plots them all on the **same graph**, making it easy to compare trends:

```python
result_df.new_cases.plot()
result_df.new_deaths.plot()
```

Both lines appear on one chart. pandas automatically assigns different colors to each line.

### Plotting a Calculated Series

You can plot the result of a calculation directly without adding it as a new column first:

```python
death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title="Death Rate Over Time")
```

The `title` parameter adds a title to the chart.

### Bar Charts

Use `kind="bar"` to switch from a line plot to a bar chart. This is especially useful after grouping — for example, comparing total cases across months:

```python
covid_month_df.new_cases.plot(kind="bar")
```

Each bar represents one month, making it easy to spot which months had the highest case counts.

### Practical Examples

```python
# Set date as index so x-axis shows dates
result_df.set_index('date', inplace=True)

# Basic line plot — new cases over time
result_df.new_cases.plot()

# Plot multiple columns on the same graph
result_df.new_cases.plot()
result_df.new_deaths.plot()

# Plot a calculated metric with a title
death_rate = result_df.total_deaths / result_df.total_cases
death_rate.plot(title="Death Rate Over Time")

# Bar chart — total cases per month
covid_month_df.new_cases.plot(kind="bar")

# Bar chart — total deaths per month
covid_month_df.new_deaths.plot(kind="bar")

# Access data by date after setting date as index
result_df.loc['2020-05-15']
```

### Plot Types Available in Pandas

| `kind` value | Chart Type | Best Used For |
|--------------|------------|---------------|
| `"line"` (default) | Line chart | Trends over time |
| `"bar"` | Vertical bar chart | Comparing categories |
| `"barh"` | Horizontal bar chart | Comparing categories with long labels |
| `"hist"` | Histogram | Distribution of values |
| `"pie"` | Pie chart | Proportions of a whole |
| `"scatter"` | Scatter plot | Relationship between two columns |

### Quick Reference Table

| Operation | Purpose | Example | Result |
|-----------|---------|---------|--------|
| `df.col.plot()` | Basic line plot | `result_df.new_cases.plot()` | Line chart |
| `df.set_index('col')` | Set a column as the index | `result_df.set_index('date', inplace=True)` | Date on x-axis |
| `df.col.plot(title="...")` | Add a title to the plot | `death_rate.plot(title="Death Rate")` | Titled chart |
| `df.col.plot(kind="bar")` | Bar chart | `covid_month_df.new_cases.plot(kind="bar")` | Bar chart |
| `df.loc['date']` | Access row by date index | `result_df.loc['2020-05-15']` | Row for that date |