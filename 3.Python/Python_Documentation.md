# Python Documentation — Retail Sales Analytics

## 1. Overview

This document describes the Python workflow used in the **Retail Sales Analytics** project.

Python is used after the Excel data-cleaning and validation stage to perform:

* Data loading
* Data preprocessing
* Data validation
* Data transformation
* Exploratory Data Analysis (EDA)
* Statistical analysis
* Business analysis
* Data visualization
* KPI generation
* Export of analytical outputs

### Python Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SQLAlchemy
* Jupyter Notebook

---

# 2. Python Project Structure

```text
04_Python
│
├── 01_preprocessing.py
├── 02_database.py
├── 03_eda.py
├── 04_visualization.py
├── 05_export.py
│
├── Retail_Sales_Analysis.ipynb
│
├── Python_Documentation.md
│
├── Images
│
└── Exports
```

---

# 3. Python Workflow

The Python workflow follows this sequence:

```text
Cleaned Excel Dataset
        ↓
Python Preprocessing
        ↓
Data Validation
        ↓
MySQL / Data Loading
        ↓
Exploratory Data Analysis
        ↓
Visualization
        ↓
KPI / Analysis Export
        ↓
Power BI / Business Reporting
```

---

# 4. Python Environment

The project was developed using:

* Visual Studio Code
* Jupyter Notebook
* Python 3.x

The Python environment should contain the following packages:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
```

---

# 5. 01_preprocessing.py

## Purpose

The preprocessing module prepares the cleaned dataset for analysis.

The Excel cleaning stage has already validated the source data. Python preprocessing performs additional programmatic checks and transformations required for analysis.

## Main Responsibilities

* Load the cleaned dataset
* Inspect the dataset structure
* Verify data types
* Check missing values
* Check duplicate records
* Convert date columns
* Create analytical columns
* Validate numerical fields
* Prepare the final analytical dataset

## Typical Operations

### Load Dataset

```python
df = pd.read_excel("Cleaned_Superstore.xlsx")
```

### Inspect Dataset

```python
df.head()
df.shape
df.info()
df.describe()
```

### Check Missing Values

```python
df.isnull().sum()
```

### Check Duplicates

```python
df.duplicated().sum()
```

### Convert Dates

```python
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
```

### Create Analytical Columns

Examples:

```python
df["Order Year"] = df["Order Date"].dt.year
df["Order Month"] = df["Order Date"].dt.month
df["Order Month Name"] = df["Order Date"].dt.month_name()
df["Quarter"] = df["Order Date"].dt.quarter
```

### Calculate Shipping Days

```python
df["Shipping Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days
```

### Calculate Profit Margin

```python
df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
)
```

The final preprocessed dataset is then used for EDA and visualization.

---

# 6. 02_database.py

## Purpose

The database module connects Python to the MySQL database used in the project.

The relational database contains:

* Customers
* Products
* Orders
* Sales

## Database Structure

```text
Customers
    │
    │ Customer_ID
    ↓
Orders
    │
    │ Order_ID
    ↓
Sales
    │
    │ Product_ID
    ↓
Products
```

## Main Responsibilities

* Establish MySQL connection
* Execute SQL queries
* Retrieve data for analysis
* Validate database connectivity
* Load analytical datasets into Pandas

## SQLAlchemy Connection

Example:

```python
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://username:password@localhost/retail_sales_db"
)
```

Credentials should not be hard-coded in a public GitHub repository.

## Reading SQL Data

```python
query = """
SELECT *
FROM sales;
"""

df = pd.read_sql(query, engine)
```

For combined analytical data:

```python
query = """
SELECT
    s.row_id,
    s.order_id,
    o.order_date,
    o.ship_date,
    o.ship_mode,
    c.customer_id,
    c.customer_name,
    c.segment,
    o.country,
    o.city,
    o.state,
    o.postal_code,
    o.region,
    p.product_id,
    p.product_name,
    p.category,
    p.sub_category,
    s.sales,
    s.quantity,
    s.discount,
    s.profit
FROM sales s
JOIN orders o
    ON s.order_id = o.order_id
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON s.product_id = p.product_id;
"""

df = pd.read_sql(query, engine)
```

This creates an analysis-ready dataset by joining the normalized MySQL tables.

---

# 7. 03_eda.py

## Purpose

The EDA module investigates the dataset to identify:

* Sales trends
* Profitability patterns
* Product performance
* Customer behavior
* Regional performance
* Shipping performance
* Discount impact

EDA is used to answer business questions before creating the final Power BI dashboard.

---

# 8. Dataset Overview

The first stage of EDA examines the overall dataset.

Typical commands:

```python
df.shape
df.columns
df.info()
df.describe()
```

Questions answered:

* How many records are available?
* How many customers are represented?
* How many products are represented?
* What is the overall sales value?
* What is the overall profit?
* What is the average order quantity?

---

# 9. Sales Analysis

## Total Sales

```python
total_sales = df["Sales"].sum()
```

## Total Profit

```python
total_profit = df["Profit"].sum()
```

## Total Quantity

```python
total_quantity = df["Quantity"].sum()
```

## Average Sales

```python
average_sales = df["Sales"].mean()
```

These metrics form the foundation for the project KPIs.

---

# 10. Monthly Sales Analysis

Sales are grouped by month to identify trends.

Example:

```python
monthly_sales = (
    df.groupby("Order Month Name")["Sales"]
    .sum()
)
```

For chronological analysis, a proper date-based grouping should be used rather than relying only on month names.

Example:

```python
monthly_sales = (
    df.groupby(
        df["Order Date"].dt.to_period("M")
    )["Sales"]
    .sum()
)
```

This analysis helps identify:

* Peak sales periods
* Low-performing months
* Seasonal patterns
* Sales growth or decline

---

# 11. Category Analysis

Sales and profit are analyzed by product category.

```python
category_analysis = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)
```

Business questions:

* Which category generates the most sales?
* Which category generates the most profit?
* Which category has high sales but low profitability?

---

# 12. Sub-Category Analysis

```python
subcategory_analysis = (
    df.groupby("Sub-Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Profit", ascending=False)
)
```

This helps identify:

* Top-performing sub-categories
* Loss-making sub-categories
* High-volume but low-profit products

---

# 13. Product Analysis

Top products can be identified using:

```python
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
```

The same approach can be used for:

* Profit
* Quantity
* Orders

This helps identify products that contribute significantly to revenue and profitability.

---

# 14. Customer Analysis

Customer-level performance can be analyzed using:

```python
customer_analysis = (
    df.groupby(
        ["Customer ID", "Customer Name"]
    )
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Sales", ascending=False)
)
```

Business questions:

* Who are the highest-value customers?
* Which customers generate the most profit?
* How many orders does each customer place?

---

# 15. Segment Analysis

```python
segment_analysis = (
    df.groupby("Segment")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
)
```

Segments include:

* Consumer
* Corporate
* Home Office

This helps identify the most valuable customer segment.

---

# 16. Regional Analysis

```python
regional_analysis = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Sales", ascending=False)
)
```

Analysis can be extended to:

* Region
* State
* City

Business questions:

* Which region generates the most revenue?
* Which region generates the most profit?
* Are there regions with strong sales but weak profitability?

---

# 17. Discount vs Profit Analysis

Discounting can have a significant effect on profitability.

```python
discount_analysis = (
    df.groupby("Discount")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)
```

This analysis helps determine whether higher discounts are associated with lower profitability.

---

# 18. Shipping Analysis

Shipping performance can be analyzed using the calculated `Shipping Days` field.

```python
shipping_analysis = (
    df.groupby("Ship Mode")
    .agg(
        Average_Shipping_Days=("Shipping Days", "mean"),
        Orders=("Order ID", "nunique"),
        Sales=("Sales", "sum")
    )
)
```

Business questions:

* Which shipping mode is used most frequently?
* Which shipping mode has the shortest average delivery time?
* Which shipping mode generates the most sales?

---

# 19. Profitability Analysis

Profit margin can be calculated as:

```python
df["Profit Margin"] = (
    df["Profit"] / df["Sales"]
)
```

Overall profit margin:

```python
profit_margin = (
    df["Profit"].sum() /
    df["Sales"].sum()
)
```

This metric is useful for understanding profitability rather than looking at revenue alone.

---

# 20. Visualization — 04_visualization.py

## Purpose

The visualization module converts analytical results into charts that communicate business findings.

Libraries:

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

## Visualizations

The project may include:

1. Monthly Sales Trend
2. Sales by Category
3. Profit by Category
4. Sales by Region
5. Profit by Region
6. Top 10 Products
7. Top 10 Customers
8. Discount vs Profit
9. Sales by Segment
10. Shipping Mode Analysis

---

# 21. Example — Monthly Sales Trend

```python
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "Images/monthly_sales_trend.png",
    dpi=300
)

plt.show()
```

---

# 22. Example — Sales by Category

```python
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "Images/sales_by_category.png",
    dpi=300
)

plt.show()
```

---

# 23. Visualization Principles

Charts should:

* Have meaningful titles
* Have labeled axes
* Use readable fonts
* Avoid unnecessary decoration
* Communicate one clear business message
* Be saved at appropriate resolution

The visualization module should focus on **business communication**, not creating charts simply for the sake of having more charts.

---

# 24. 05_export.py

## Purpose

The export module saves important analytical results so they can be reused in:

* Power BI
* Reports
* Presentations
* Business documentation

## Export Folder

```text
Exports
```

The script creates the folder automatically if it does not already exist.

Example:

```python
import os

EXPORT_FOLDER = "Exports"

os.makedirs(
    EXPORT_FOLDER,
    exist_ok=True
)
```

---

# 25. Export KPI Summary

Example:

```python
kpis = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Quantity",
        "Total Orders",
        "Total Customers"
    ],
    "Value": [
        df["Sales"].sum(),
        df["Profit"].sum(),
        df["Quantity"].sum(),
        df["Order ID"].nunique(),
        df["Customer ID"].nunique()
    ]
})
```

Export:

```python
kpis.to_csv(
    "Exports/overall_kpis.csv",
    index=False
)
```

---

# 26. Export Analytical Tables

Examples:

```text
Exports/
│
├── overall_kpis.csv
├── monthly_sales.csv
├── category_analysis.csv
├── subcategory_analysis.csv
├── customer_analysis.csv
├── product_analysis.csv
├── regional_analysis.csv
└── shipping_analysis.csv
```

These exported files provide reusable analytical outputs.

---

# 27. Images Folder

Visualization outputs are stored in:

```text
Images/
```

Example:

```text
Images/
│
├── monthly_sales_trend.png
├── sales_by_category.png
├── profit_by_category.png
├── sales_by_region.png
├── profit_by_region.png
├── top_products.png
├── top_customers.png
└── discount_vs_profit.png
```

These images can be used in:

* GitHub README
* Business Report
* Presentation
* Portfolio

---

# 28. Python Quality Checks

Before finalizing the Python analysis, verify:

### Data Quality

* Missing values checked
* Duplicate records checked
* Data types verified
* Date columns converted correctly
* Numeric columns validated

### Analysis Quality

* Aggregations verified
* Grouping logic checked
* Unique order/customer counts validated
* Profit calculations verified
* No accidental duplicate joins

### Visualization Quality

* Correct labels
* Correct aggregation
* Meaningful titles
* Readable charts
* Images successfully exported

### Export Quality

* Export folder created
* CSV files generated successfully
* Exported values match analysis
* No unexpected blank files

---

# 29. Python Files and Responsibilities

| File                          | Responsibility                                     |
| ----------------------------- | -------------------------------------------------- |
| `01_preprocessing.py`         | Data loading, validation, cleaning, transformation |
| `02_database.py`              | MySQL connection and data retrieval                |
| `03_eda.py`                   | Exploratory and business analysis                  |
| `04_visualization.py`         | Charts and visualization outputs                   |
| `05_export.py`                | KPI and analytical table exports                   |
| `Retail_Sales_Analysis.ipynb` | Interactive analysis and project demonstration     |
| `Python_Documentation.md`     | Documentation of the complete Python workflow      |

---

# 30. Recommended Execution Order

Run the Python files in this order:

```text
01_preprocessing.py
        ↓
02_database.py
        ↓
03_eda.py
        ↓
04_visualization.py
        ↓
05_export.py
```

The notebook can be used to demonstrate and document the analytical process interactively.

---

# 31. Final Python Outputs

After successful execution, the Python folder should contain:

```text
04_Python
│
├── 01_preprocessing.py
├── 02_database.py
├── 03_eda.py
├── 04_visualization.py
├── 05_export.py
│
├── Retail_Sales_Analysis.ipynb
├── Python_Documentation.md
│
├── Images
│   ├── monthly_sales_trend.png
│   ├── sales_by_category.png
│   ├── profit_by_category.png
│   └── ...
│
└── Exports
    ├── overall_kpis.csv
    ├── monthly_sales.csv
    ├── category_analysis.csv
    ├── product_analysis.csv
    └── ...
```

---

# 32. Business Insights

Python analysis should ultimately support business conclusions.

Examples of the types of insights to identify:

* Which categories generate the highest revenue?
* Which categories generate the highest profit?
* Which products have high sales but low profit?
* Which regions are most profitable?
* Which customer segments contribute the most revenue?
* Does higher discounting affect profitability?
* Which shipping modes are most frequently used?
* Which months have the highest sales?

The final insights should be based on the actual results generated from the dataset rather than assumptions.

---

# 33. Transition to Power BI

The outputs from Python can support the Power BI stage.

```text
Excel
  ↓
Data Validation
  ↓
MySQL
  ↓
SQL Analysis
  ↓
Python
  ↓
EDA
  ↓
Business Analysis
  ↓
Power BI
  ↓
Interactive Dashboard
```

Power BI should not simply reproduce every Python chart. Instead, the dashboard should present the most important business KPIs, trends, comparisons, and actionable insights interactively.

---

# 34. Final Objective

The purpose of Python in this project is not simply to demonstrate Python syntax.

It demonstrates the ability to:

1. Load business data
2. Validate data quality
3. Transform data
4. Analyze business performance
5. Identify trends and patterns
6. Create meaningful visualizations
7. Generate reusable analytical outputs
8. Translate data into business insights

This demonstrates an end-to-end analytical workflow suitable for a Data Analyst portfolio.
