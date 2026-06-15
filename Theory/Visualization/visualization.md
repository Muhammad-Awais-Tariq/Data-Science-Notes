# Data Visualization with Matplotlib and Seaborn

## Table of Contents
1. [Why Visualization?](#why-visualization)
2. [Importing the Modules](#importing-the-modules)
3. [Line Charts](#line-charts)
4. [Improving and Customizing Line Charts](#improving-and-customizing-line-charts)

---

## Why Visualization?

Most real-world data comes in the form of numbers — thousands or even millions of rows of values that are impossible to interpret just by looking at them. Visualization solves this by converting raw numbers into a visual format that our brains can process instantly.

For example, instead of scanning 365 rows of daily case counts to spot a trend, a single line chart shows you the rise and fall at a glance. Instead of comparing 12 monthly totals in a table, a bar chart makes the highest and lowest months immediately obvious.

Common chart types and what they are best used for:

| Chart Type | Best Used For | Example |
|------------|--------------|---------|
| **Line Chart** | Trends over time | Daily cases over a year |
| **Bar Chart** | Comparing values across categories | Total cases per month |
| **Histogram** | Distribution of a single value | How often case counts fall in a range |
| **Scatter Plot** | Relationship between two variables | Cases vs tests per day |
| **Pie Chart** | Proportions of a whole | Share of cases per region |
| **Heatmap** | Patterns across two dimensions | Cases by weekday and month |

Good visualizations do not just make data look nice — they reveal patterns, outliers, and trends that would otherwise stay hidden in a spreadsheet.

---

## Importing the Modules

Python has two main libraries for data visualization that are used together:

- **Matplotlib** — the foundation. Handles all basic plotting: line charts, bar charts, histograms, scatter plots, and full control over labels, colors, axes, and figure size.
- **Seaborn** — built on top of Matplotlib. Adds more advanced and visually polished chart types with less code, and works especially well with pandas DataFrames.

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

**Why `plt` and `sns`?** These are the standard aliases used universally — every tutorial, documentation page, and Stack Overflow answer uses them. Stick to these aliases to keep your code readable and consistent.

---

## Line Charts

### What is a Line Chart?

A line chart is the most basic form of data visualization. It plots individual data points along an axis and connects them with a line, making it easy to see how a value changes over a sequence — most commonly over time.

### Basic Line Chart

To draw a line chart, pass a list of values to `plt.plot()` and call `plt.show()` to display it:

```python
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

plt.plot(yield_apples)
plt.show()
```

`plt.plot()` draws the chart and `plt.show()` actually renders and displays it. Without `plt.show()`, nothing appears on screen.

**Output:**

![Line Chart](Figure_1.png)

The x-axis shows the index of each value (0, 1, 2...) and the y-axis shows the actual values. By default there are no labels or titles — those need to be added manually, which is covered in the next section.

---

## Improving and Customizing Line Charts

### Adding Custom Axis Values

The basic plot uses row indexes on the x-axis which are not meaningful. You can pass a second list to `plt.plot()` to use as the x-axis values — the first argument is always x and the second is y:

```python
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
years = [2010, 2011, 2012, 2013, 2014, 2016]

plt.plot(years, yield_apples)
plt.show()
```

**Output:**

![Line Chart with Years](Figure_2.png)

### Adding Axis Labels

The axes still have no labels, so it is not clear what the chart is showing. Use `plt.xlabel()` and `plt.ylabel()` to label them:

```python
plt.plot(years, yield_apples)
plt.xlabel('Year')
plt.ylabel('Yield')
plt.show()
```

**Output:**

![Line Chart with Labels](Figure_3.png)

**Note:** Any function you call after `plt.plot()` applies to the same plot until `plt.show()` is called.

### Plotting Multiple Lines

You can plot more than one line on the same chart by calling `plt.plot()` multiple times before `plt.show()`. Each call adds a new line and Matplotlib automatically assigns a different color to each:

```python
years = range(2000, 2012)
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
yield_oranges = [0.925, 0.921, 0.900, 0.895, 0.890, 0.885]

plt.plot(years, yield_apples)
plt.plot(years, yield_oranges)
plt.xlabel('Year')
plt.ylabel('Yield')
plt.show()
```

**Output:**

![Multiple Lines](Figure_4.png)

### Adding a Title and Legend

With multiple lines on the same chart, you need a legend to tell which line is which. Use `plt.title()` for the chart title and `plt.legend()` with a list of labels in the same order as your `plt.plot()` calls:

```python
plt.plot(years, yield_apples)
plt.plot(years, yield_oranges)
plt.xlabel('Year')
plt.ylabel('Yield')
plt.title("Crop Yields in Pakistan")
plt.legend(["Apples", "Oranges"])
plt.show()
```

**Output:**

![Title and Legend](Figure_5.png)

### Adding Markers

Markers are symbols drawn at each data point on the line, making it easier to see exact values without guessing. Pass the `marker` argument to `plt.plot()`:

```python
plt.plot(years, yield_apples, marker='o')
plt.plot(years, yield_oranges, marker='X')
plt.xlabel('Year')
plt.ylabel('Yield')
plt.title("Crop Yields in Pakistan")
plt.legend(["Apples", "Oranges"])
plt.show()
```

**Output:**

![Markers](Figure_6.png)

You can use any marker symbol from the full list here: [Matplotlib Markers Reference](https://matplotlib.org/stable/api/markers_api.html)

### Line Style Shorthand (fmt)

Instead of passing multiple separate arguments, you can use a shorthand format string `fmt` to set the marker, line style, and color all in one string:

```
fmt = [marker][line][color]
```

```python
# 's' = square marker, '-' = solid line, 'b' = blue
plt.plot(years, yield_apples, 's-b')

# markers only, no line (skip the line character)
plt.plot(years, yield_oranges, 'sb')
```

**Output:**

![Line Style Shorthand](Figure_7.png)

### Customizing Line and Marker Appearance

For full control beyond the shorthand, you can pass individual styling arguments to `plt.plot()`:

| Argument | Purpose | Example Value |
|----------|---------|--------------|
| `color` | Line and marker color | `'red'`, `'#ff0000'` |
| `linestyle` | Style of the line | `'-'`, `'--'`, `':'`, `'-.'` |
| `linewidth` | Thickness of the line | `2`, `0.5` |
| `marker` | Marker shape at each point | `'o'`, `'s'`, `'X'`, `'^'` |
| `markersize` | Size of the marker | `8`, `12` |
| `markeredgecolor` | Color of the marker border | `'black'`, `'blue'` |
| `markeredgewidth` | Thickness of the marker border | `1`, `2` |
| `markerfacecolor` | Fill color of the marker | `'white'`, `'green'` |
| `alpha` | Transparency of the line (0=invisible, 1=solid) | `0.5`, `0.8` |

```python
plt.plot(years, yield_apples,
         color='green',
         linestyle='--',
         linewidth=2,
         marker='o',
         markersize=8,
         markeredgecolor='black',
         markeredgewidth=1,
         markerfacecolor='white',
         alpha=0.8)
plt.show()
```

### Changing the Figure Size

If the default chart feels too small or cramped, use `plt.figure()` with the `figsize` parameter before your plot call. The values are `(width, height)` in inches:

```python
plt.figure(figsize=(12, 6))
plt.plot(years, yield_apples, marker='o')
plt.plot(years, yield_oranges, marker='X')
plt.xlabel('Year')
plt.ylabel('Yield')
plt.title("Crop Yields in Pakistan")
plt.legend(["Apples", "Oranges"])
plt.show()
```

**Note:** `plt.figure()` must always be called **before** `plt.plot()`, otherwise it opens a new empty figure instead of resizing the current one.

### Enhancing Plots with Seaborn Styles

Seaborn provides ready-made styles that instantly make Matplotlib plots look cleaner and more polished — without changing any of your plotting code. Just call `sns.set_style()` once before your plot:

```python
sns.set_style("whitegrid")

plt.plot(years, yield_apples, marker='o')
plt.plot(years, yield_oranges, marker='X')
plt.xlabel('Year')
plt.ylabel('Yield')
plt.title("Crop Yields in Pakistan")
plt.legend(["Apples", "Oranges"])
plt.show()
```

**Output:**

![Seaborn Style](Figure_8.png)

Available styles: `"darkgrid"`, `"whitegrid"`, `"dark"`, `"white"`, and `"ticks"`. See the full reference and visual previews here:
- [Seaborn Style Documentation](https://seaborn.pydata.org/tutorial/aesthetics.html)
- [Visual Style Gallery](https://python-graph-gallery.com/104-seaborn-themes/)

### Changing Matplotlib Default Parameters

For finer control over global defaults — like font size, line width, or figure size — use `matplotlib.rcParams`. These are settings that apply to **every** plot in your script unless overridden individually:

```python
import matplotlib

# Set default font size to 14 for all plots
matplotlib.rcParams["font.size"] = 14

# Other useful defaults
matplotlib.rcParams["figure.figsize"] = (10, 6)   # Default figure size
matplotlib.rcParams["lines.linewidth"] = 2         # Default line width
matplotlib.rcParams["axes.grid"] = True            # Show grid by default
```

To see every parameter available, just print the full dictionary:

```python
print(matplotlib.rcParams)
```

**Note:** `rcParams` changes persist for the entire session. If you only want to change the style for one plot, use the individual arguments in `plt.plot()` instead.