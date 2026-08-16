# 📊 Retail Sales Analysis — End-to-End Data Analytics Project

## 📌 Project Overview

This project is an end-to-end **Retail Sales Analysis** project that demonstrates the complete data analytics workflow from raw data preparation to business intelligence reporting.

The project analyzes **sales, profit, customers, products, regions, segments, and shipping performance** and presents the findings through an interactive **5-page Power BI dashboard**.

---

## 🎯 Business Objectives

The analysis aims to answer key business questions:

- How are sales and profit changing over time?
- Which categories and segments generate the most sales and profit?
- Which products are the top and bottom performers?
- Which customers contribute the most revenue?
- How are customers distributed by sales value?
- Does discounting appear to affect profitability?
- Which regions and states perform best?
- Which shipping modes are most frequently used and profitable?

---

## 🛠️ Tools & Technologies

- **Microsoft Excel** — Data cleaning and preparation
- **MySQL** — Database design, validation and SQL analysis
- **Python** — Exploratory Data Analysis and validation
- **Pandas / NumPy** — Data manipulation and analysis
- **Power BI** — Data modeling, DAX and dashboard development

---

## 🔄 Project Workflow

```text
Raw Data
   ↓
Excel Data Cleaning
   ↓
MySQL Database & SQL Analysis
   ↓
Python Exploratory Data Analysis
   ↓
Power BI Data Modeling
   ↓
DAX Measures & Time Intelligence
   ↓
Interactive Power BI Dashboard
   ↓
Business Insights & Recommendations

---

## Power BI Dashboard


---

## Power BI Data Modeling & DAX

A structured analytical model was created in Power BI using:

Fact_Sales transaction table
Calendar date table
Customer Sales Band helper table
Active Date → Sales relationship
Time-intelligence calculations

Key DAX measures include:
Total Sales
Total Profit
Total Orders
Total Customers
Average Order Value
Profit Margin %
Sales PY
Sales YoY %
Profit PY
Profit YoY %
Sales per Customer
Sales per Customer PY
Sales per Customer YoY %
Customers in Sales Band

---

##  Key Business Insights

- **Strong overall business performance:** The business generated approximately **₹2.30M in total sales** across **5,009 orders**, with an overall **12.47% profit margin**, indicating a profitable retail operation.

- **Customer base and order activity:** The analysis identified **793 unique customers** and 5,009 orders, providing a useful foundation for customer segmentation and identifying high-value customers.

- **Customer value varies significantly:** The Customer Sales Distribution analysis shows that customers are concentrated across different sales-value bands, helping identify high-value customer groups that could be targeted for retention and upselling.

- **Product performance is uneven:** The Top 5 and Bottom 5 product analysis highlights substantial differences in product profitability, helping identify products that should be prioritized and products that require pricing, discount, or inventory review.

- **Discounting requires profitability monitoring:** The Discount vs Profit analysis helps identify the relationship between discount levels and profitability, providing a basis for optimizing discount strategies rather than focusing only on increasing sales volume.

- **Regional and shipping performance varies:** Region, state, and shipping-mode analysis reveals differences in sales, profit, order volume, and shipping preferences, providing opportunities to optimize regional strategy and shipping decisions.
---

## Data Validation

The analysis was validated across SQL and Power BI to ensure consistency.

Key validation areas include:

Total transaction records
Distinct orders
Distinct customers
Total sales
Total profit
Total products
Total quantity
Average Order Value
Profit Margin %

Known validation checkpoints:

| Metric             | Result |
| ------------------ | -----: |
| Fact Sales Rows    |  9,994 |
| Distinct Orders    |  5,009 |
| Distinct Customers |    793 |

---

## Project Structure

Retail_Sales_Analysis/
│
├── 01_Data/
│   ├── Superstore Dataset Raw.xlsx
│   ├── Superstore_Dataset_cleaned.xlsx
│   └── Excel Cleaning Logs.xlsx
│
├── 02_SQL/
│   ├── Database_Design.sql
│   ├── Data_Validation.sql
│   └── Business_Analysis.sql
│
├── 03_Python/
│   ├── database.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── visualization.py
│   ├── export.py
│   └── retail_eda.ipynb
│
├── 04_PowerBI/
│   ├── Retail_Sales_Analysis.pbix
│   └── PowerBI_Documentation.xlsx
│
├── images/
│   ├── page1_Executive overview.png
│   ├── page2_sales & profit.png
│   ├── page3_customers.png
│   ├── page4_products.png
│   └── page5_regional & shipping.png
└── README.md

---

## Skills Demonstrated 

Data Preparation :
Data Cleaning
Data Validation
Data Quality Checks

SQL :
Database Design
Aggregations
JOINs
GROUP BY
DISTINCTCOUNT
Window Functions
Business Analysis

Python :
Pandas
NumPy
Exploratory Data Analysis
Data Validation
Data Visualization

Power BI :
Data Modeling
Star Schema Concepts
DAX
Time Intelligence
YoY Analysis
KPI Development
Interactive Dashboards
Data Visualization
Business Storytelling

---

## Project Outcome

This project demonstrates the ability to transform raw retail transaction data into a structured analytical solution:

Raw Data → Clean Data → SQL → Python → Power BI → Business Insights

The final dashboard provides an interactive view of business performance and helps identify opportunities related to sales growth, profitability, customer value, product performance, regional performance and shipping strategy.

---

## Author

Subash Venkatesan

Aspiring Data Analyst

Skills: Excel | SQL | Python | Pandas | Power BI | DAX | Data Visualization | Business Analysis