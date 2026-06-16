# Data Science Notes

A structured collection of notes and practice code covering the core Python data science stack — **NumPy**, **Pandas**, and **Matplotlib/Seaborn**. Built alongside hands-on coursework, this repo is meant to be read as a learning guide, not run as an application.

---

## What's Inside

```
Data-Science-Notes/
├── Practice/
│   ├── Numpy/
│   │   ├── climate_data.txt          # Sample dataset used in NumPy exercises
│   │   └── Intro_numpy_practice.py   # Hands-on NumPy practice code
│   ├── Pandas/
│   │   ├── italy-covid-daywise.csv   # COVID dataset used in Pandas exercises
│   │   ├── locations.csv             # Country/population data for merging
│   │   └── pandas_practice.py        # Hands-on Pandas practice code
│   └── Visualization/
│       ├── image (16).png            # Image used in Matplotlib image exercises
│       └── visualization.py          # Hands-on plotting practice code
└── Theory/
    ├── Numpy/
    │   ├── Indexing_Visualization.jpg  # Visual reference for NumPy indexing
    │   └── Intro_numpy.md              # Full NumPy notes
    ├── Pandas/
    │   └── Intro_to_Pandas.md          # Full Pandas notes
    └── Visualization/
        ├── Graphs/                     # All chart output images referenced in notes
        └── visualization.md            # Full Matplotlib & Seaborn notes
```

Each topic has two parts — a `Theory/` note file to read, and a matching `Practice/` script to experiment with.

---

## Reading Guide

### 1. NumPy — `Theory/Numpy/Intro_numpy.md`

Start here. NumPy is the numerical backbone of the entire Python data science stack.

| Section | What You'll Learn |
|---|---|
| The Dot Product | What it is, why it matters, manual vs NumPy implementation |
| NumPy Arrays | `ndarray`, dtypes, shape, 1D/2D/3D arrays |
| Matrix Multiplication | `np.matmul()`, the `@` operator, matrix-vector products |
| File I/O | `np.genfromtxt()`, `np.savetxt()`, reading/writing CSV data |
| `reshape()` | Reshaping arrays, using `-1` for auto-inference |
| Concatenation | `np.concatenate()`, `axis=0` vs `axis=1` |
| Arithmetic & Broadcasting | Scalar ops, array ops, broadcasting rules |
| Axis | Understanding `axis=0/1/2/3` in 2D, 3D, and 4D arrays |
| Comparison Operations | Boolean arrays, counting matches with `.sum()` |
| Indexing & Slicing | Exact indices vs slices, the shape rule, 3D indexing |
| Special Array Functions | `np.zeros`, `np.ones`, `np.eye`, `np.random.rand/randn`, `np.arange`, `np.linspace` |
| Python File I/O | `open()`, `readlines()`, manual CSV parsing, `read_csv()` / `write_csv()` from scratch |
| The `os` Module | `os.path.join`, `os.makedirs`, `os.path.exists` |

> **Companion file:** `Practice/Numpy/Intro_numpy_practice.py`

---

### 2. Pandas — `Theory/Pandas/Intro_to_Pandas.md`

Pandas builds on NumPy and is the standard tool for working with tabular data.

| Section | What You'll Learn |
|---|---|
| Reading CSV | `pd.read_csv()`, DataFrames, NaN values |
| Exploring Data | `.info()`, `.describe()`, `.columns`, `.shape`, `.head()`, `.tail()` |
| DataFrame Structure | Why DataFrames are "dictionaries of lists" and why that's efficient |
| Accessing Data | Column access, `.at[]`, `.loc[]`, `.sample()`, `.first_valid_index()` |
| Analyzing Data | `.sum()`, calculating rates and ratios |
| Querying & Filtering | Boolean queries, inline filters, `&` / `\|` operators, adding/dropping columns |
| Sorting & Faulty Data | `.sort_values()`, identifying negatives, 4 strategies for fixing bad values |
| Working with Dates | `pd.to_datetime()`, `DatetimeIndex`, extracting year/month/day/weekday |
| Grouping | `.groupby()`, `.sum()` / `.mean()` / `.max()` per group, `.cumsum()` |
| Merging | `.merge()`, joining on a shared column, normalizing to per-million |
| Writing Files | `.to_csv()`, `.to_excel()`, `.to_json()`, `.to_parquet()`, `index=False` |
| Basic Plotting | `.plot()`, setting date as index, line vs bar, grouped charts |

> **Companion files:** `Practice/Pandas/pandas_practice.py`, `italy-covid-daywise.csv`, `locations.csv`

---

### 3. Visualization — `Theory/Visualization/visualization.md`

Covers Matplotlib (the foundation) and Seaborn (the higher-level layer on top of it).

| Section | What You'll Learn |
|---|---|
| Why Visualize? | When to use which chart type |
| Line Charts | `plt.plot()`, axis labels, multiple lines, legend, markers, fmt shorthand, styling args, `figsize`, Seaborn styles, `rcParams` |
| Scatter Plots | `sns.scatterplot()`, `hue` for grouping, `data` parameter |
| Histograms | `plt.hist()`, bin count, `np.arange()` bins, unequal bins, stacked histograms |
| Bar Charts | `plt.bar()`, stacked bars, `sns.barplot()`, error bars, `hue`, horizontal bars |
| Heatmaps | `.pivot()`, `sns.heatmap()`, `annot`, `fmt`, `cmap` options |
| Images | Loading with PIL, images as NumPy arrays, `plt.imshow()`, cropping by slicing |
| Subplots | `plt.subplots()`, `axes[row, col]`, Seaborn `ax=` parameter, `tight_layout()` |
| Pair Plots | `sns.pairplot()`, `hue` for species/group separation |

> **Companion files:** `Practice/Visualization/visualization.py`, `Practice/Visualization/image (16).png`
> All chart outputs are saved in `Theory/Visualization/Graphs/`

---

## Recommended Reading Order

```
Intro_numpy.md  →  Intro_to_Pandas.md  →  visualization.md
```

Each topic builds on the previous one. NumPy arrays are the foundation that Pandas is built on, and both feed into visualization.

---

## Running the Practice Code

The practice scripts are standalone and don't need to be run in any particular order. If you want to run them:

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (recommended)

### With uv

```bash
# Install uv if you don't have it
pip install uv

# Sync dependencies
uv sync

# Run a practice script
uv run python Practice/Numpy/Intro_numpy_practice.py
uv run python Practice/Pandas/pandas_practice.py
uv run python Practice/Visualization/visualization.py
```

### With pip

```bash
pip install numpy pandas matplotlib seaborn pillow
python Practice/Numpy/Intro_numpy_practice.py
```

> **Note:** The visualization script uses `plt.show()` which opens an interactive window. Make sure your environment supports GUI display.

---

## Topics Covered at a Glance

| Library | Core Concepts |
|---|---|
| **NumPy** | Arrays, dot product, matrix multiplication, broadcasting, indexing, file I/O |
| **Pandas** | DataFrames, filtering, grouping, merging, date handling, writing files |
| **Matplotlib** | Line, bar, scatter, histogram, heatmap, subplots, image display |
| **Seaborn** | `scatterplot`, `barplot`, `heatmap`, `pairplot`, styles |

---

## Author

Muhammad Awais Tariq

---

If you like this project, consider giving it a star ⭐