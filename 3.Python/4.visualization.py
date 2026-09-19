"""
                RETAIL SALES ANALYSIS PROJECT
File Name  : visualization.py

Purpose
-------
This module contains all visualization functions used for
Exploratory Data Analysis (EDA).

Libraries   : Pandas, Matplotlib

"""


###### IMPORT LIBRARIES


import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


###### GLOBAL PLOT STYLE


plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (12, 6)
plt.rcParams["figure.dpi"] = 120
plt.rcParams["savefig.dpi"] = 300
plt.rcParams["font.size"] = 11
plt.rcParams["axes.titlesize"] = 18
plt.rcParams["axes.labelsize"] = 13
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10
plt.rcParams["legend.fontsize"] = 10
plt.rcParams["axes.titleweight"] = "bold"
plt.rcParams["axes.grid"] = True
plt.rcParams["grid.alpha"] = 0.30
plt.rcParams["figure.autolayout"] = True


###### CREATE IMAGES FOLDER


IMAGE_FOLDER = "Images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)


###### CURRENCY FORMATTER


def currency(x, pos):
    """
    Formats numbers into currency.
    Example
    1250000
    becomes
    $1,250,000
    """

    return f"${x:,.0f}"

currency_formatter = FuncFormatter(currency)


###### SAVE CHART HELPER

def save_chart(fig, filename):
    """
    Save a Matplotlib figure as a high-resolution PNG image.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib figure object that should be saved.

    filename : str
        Name of the output image file.

        Example:
        "01_sales_by_category.png"

    Returns
    -------
    None
        Saves the figure inside the Images folder.
    """

    
    # Make sure the Images folder exists
    
    os.makedirs(
        IMAGE_FOLDER,
        exist_ok=True
    )

    # Create complete image path    

    filepath = os.path.join(
        IMAGE_FOLDER,
        filename
    )

    # Save high-resolution chart    

    fig.savefig(
        filepath,
        dpi=300,
        bbox_inches="tight"
    )

    print(f"Chart Saved : {filepath}")


###### ADD VALUE LABELS


def add_value_labels(ax):
    """
    Add value labels to bar charts.
    """

    for bar in ax.patches:

        height = bar.get_height()
        ax.annotate(
            f"{height:,.0f}",
            (
                bar.get_x() + bar.get_width()/2,
                height
            ),
            ha="center",
            va="bottom",
            fontsize=9
        )


###### PROFESSIONAL CHART SETTINGS


def chart_layout(
    title,
    xlabel,
    ylabel
):
    """
    Apply professional formatting
    to all charts.
    """

    plt.title(
        title,
        pad=15,
        weight="bold"
    )

    plt.xlabel(
        xlabel
    )

    plt.ylabel(
        ylabel
    )

    plt.grid(
        linestyle="--",
        alpha=0.30
    )

    plt.xticks(

        rotation=0

    )


###### SHOW & SAVE


def finish_chart(filename):
    """
    Finalize chart.
    """
    save_chart(filename)
    plt.show()
    plt.close()


# CHARTS 1–6
# RETAIL SALES ANALYSIS VISUALIZATIONS


# CHART 1 — SALES BY CATEGORY

def sales_by_category(df):
    """
    Create a bar chart showing total sales by product category.

    Business Purpose
    ----------------
    Identifies which product categories generate the highest
    revenue and helps management understand category-level
    sales performance.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 1: Sales by Category...")

    summary = (
        df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Category"],
        summary["Sales"]
    )

    ax.set_title(
        "Sales by Product Category",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")

    ax.tick_params(axis="x", rotation=0)

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "01_sales_by_category.png"
    )

    plt.close(fig)

    print("Chart 1 completed.")



###### CHART 2 — PROFIT BY CATEGORY


def profit_by_category(df):
    """
    Create a bar chart showing total profit by product category.

    Business Purpose
    ----------------
    Identifies which product categories generate the highest
    profit and helps management compare revenue performance
    with profitability.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 2: Profit by Category...")

    summary = (
        df.groupby("Category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Category"],
        summary["Profit"]
    )

    ax.set_title(
        "Profit by Product Category",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Profit")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "02_profit_by_category.png"
    )

    plt.close(fig)
    print("Chart 2 completed.")


###### CHART 3 — SALES BY SUB-CATEGORY


def sales_by_subcategory(df):
    """
    Create a horizontal bar chart showing sales by sub-category.

    Business Purpose
    ----------------
    Identifies the strongest and weakest product sub-categories
    based on revenue.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 3: Sales by Sub-category...")

    summary = (
        df.groupby("Sub_category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=True)
    )

    fig, ax = plt.subplots(figsize=(11, 8))

    bars = ax.barh(
        summary["Sub_category"],
        summary["Sales"]
    )

    ax.set_title(
        "Sales by Product Sub-category",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("Sub-category")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "03_sales_by_subcategory.png"
    )

    plt.close(fig)

    print("Chart 3 completed.")



###### CHART 4 — PROFIT BY SUB-CATEGORY


def profit_by_subcategory(df):
    """
    Create a horizontal bar chart showing profit by sub-category.

    Business Purpose
    ----------------
    Highlights the most profitable and least profitable
    product sub-categories and identifies potential
    loss-making areas.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 4: Profit by Sub-category...")

    summary = (
        df.groupby("Sub_category", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=True)
    )

    fig, ax = plt.subplots(figsize=(11, 8))

    bars = ax.barh(
        summary["Sub_category"],
        summary["Profit"]
    )

    ax.set_title(
        "Profit by Product Sub-category",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Profit")
    ax.set_ylabel("Sub-category")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Add zero reference line
    ax.axvline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        if value >= 0:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f" {value:,.0f}",
                va="center",
                fontsize=9
            )

        else:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f"{value:,.0f} ",
                ha="right",
                va="center",
                fontsize=9
            )

    plt.tight_layout()

    save_chart(
        fig,
        "04_profit_by_subcategory.png"
    )

    plt.close(fig)

    print("Chart 4 completed.")



###### CHART 5 — SALES BY REGION


def sales_by_region(df):
    """
    Create a bar chart showing total sales by region.

    Business Purpose
    ----------------
    Compares regional revenue performance and identifies
    the strongest geographic markets.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 5: Sales by Region...")

    summary = (
        df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Region"],
        summary["Sales"]
    )

    ax.set_title(
        "Sales by Region",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Sales")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "05_sales_by_region.png"
    )

    plt.close(fig)

    print("Chart 5 completed.")



###### CHART 6 — PROFIT BY REGION


def profit_by_region(df):
    """
    Create a bar chart showing total profit by region.

    Business Purpose
    ----------------
    Compares regional profitability and identifies regions
    that may require strategic attention.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 6: Profit by Region...")

    summary = (
        df.groupby("Region", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Region"],
        summary["Profit"]
    )

    ax.set_title(
        "Profit by Region",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Region")
    ax.set_ylabel("Profit")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        if value >= 0:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="bottom",
                fontsize=10
            )

        else:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="top",
                fontsize=10
            )

    plt.tight_layout()

    save_chart(
        fig,
        "06_profit_by_region.png"
    )

    plt.close(fig)

    print("Chart 6 completed.")


###### CHART 7 — SALES BY CUSTOMER SEGMENT


def sales_by_segment(df):
    """
    Create a bar chart showing total sales by customer segment.

    Business Purpose
    ----------------
    Identifies which customer segments contribute the most
    revenue and helps management prioritize high-value
    customer groups.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 7: Sales by Customer Segment...")

    summary = (
        df.groupby("Segment", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Segment"],
        summary["Sales"]
    )

    ax.set_title(
        "Sales by Customer Segment",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Customer Segment")
    ax.set_ylabel("Sales")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "07_sales_by_segment.png"
    )

    plt.close(fig)

    print("Chart 7 completed.")



###### CHART 8 — PROFIT BY CUSTOMER SEGMENT


def profit_by_segment(df):
    """
    Create a bar chart showing total profit by customer segment.

    Business Purpose
    ----------------
    Compares the profitability of customer segments and
    identifies which segments contribute most to business
    profitability.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 8: Profit by Customer Segment...")

    summary = (
        df.groupby("Segment", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Segment"],
        summary["Profit"]
    )

    ax.set_title(
        "Profit by Customer Segment",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Customer Segment")
    ax.set_ylabel("Profit")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        if value >= 0:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="bottom",
                fontsize=10
            )

        else:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="top",
                fontsize=10
            )

    plt.tight_layout()

    save_chart(
        fig,
        "08_profit_by_segment.png"
    )

    plt.close(fig)

    print("Chart 8 completed.")



###### CHART 9 — MONTHLY SALES TREND


def monthly_sales(df):
    """
    Create a line chart showing monthly sales trends.

    Business Purpose
    ----------------
    Tracks revenue performance over time and helps identify
    seasonal patterns, growth periods and weaker sales months.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset containing Order_Date.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 9: Monthly Sales Trend...")

    data = df.copy()

    # Ensure Order_Date is a datetime column
    data["Order_Date"] = pd.to_datetime(
        data["Order_Date"]
    )

    summary = (
        data
        .groupby(
            data["Order_Date"].dt.to_period("M")
        )["Sales"]
        .sum()
        .reset_index()
    )

    summary["Order_Date"] = summary["Order_Date"].dt.to_timestamp()

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        summary["Order_Date"],
        summary["Sales"],
        marker="o",
        linewidth=2
    )

    ax.set_title(
        "Monthly Sales Trend",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Sales")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Rotate date labels
    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    save_chart(
        fig,
        "09_monthly_sales_trend.png"
    )

    plt.close(fig)

    print("Chart 9 completed.")



###### CHART 10 — MONTHLY PROFIT TREND


def monthly_profit(df):
    """
    Create a line chart showing monthly profit trends.

    Business Purpose
    ----------------
    Tracks profitability over time and helps identify months
    with strong or weak financial performance.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed retail sales dataset containing Order_Date.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 10: Monthly Profit Trend...")

    data = df.copy()

    # Ensure Order_Date is a datetime column
    data["Order_Date"] = pd.to_datetime(
        data["Order_Date"]
    )

    summary = (
        data
        .groupby(
            data["Order_Date"].dt.to_period("M")
        )["Profit"]
        .sum()
        .reset_index()
    )

    summary["Order_Date"] = summary["Order_Date"].dt.to_timestamp()

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(
        summary["Order_Date"],
        summary["Profit"],
        marker="o",
        linewidth=2
    )

    ax.set_title(
        "Monthly Profit Trend",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Month")
    ax.set_ylabel("Profit")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    save_chart(
        fig,
        "10_monthly_profit_trend.png"
    )

    plt.close(fig)

    print("Chart 10 completed.")


# CHART 11 — TOP 10 PRODUCTS BY SALES

def top_10_products_by_sales(df):
    """
    Create a horizontal bar chart showing the top 10 products
    ranked by total sales.

    Business Purpose:
    Identifies the products that contribute the most revenue
    and helps management understand high-performing products.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 11: Top 10 Products by Sales...")

    summary = (
        df.groupby(
            ["Product_ID", "Product_Name"],
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
        .head(10)
        .sort_values(
            "Sales",
            ascending=True
        )
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.barh(
        summary["Product_Name"],
        summary["Sales"]
    )

    ax.set_title(
        "Top 10 Products by Sales",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("Product")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "11_top_10_products_by_sales.png"
    )

    plt.close(fig)

    print("Chart 11 completed.")


###### CHART 12 — TOP 10 PRODUCTS BY PROFIT


def top_10_products_by_profit(df):
    """
    Create a horizontal bar chart showing the top 10 products
    ranked by total profit.

    Business Purpose:
    Identifies the products that contribute the most profit
    and supports product portfolio optimization decisions.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 12: Top 10 Products by Profit...")

    summary = (
        df.groupby(
            ["Product_ID", "Product_Name"],
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(10)
        .sort_values(
            "Profit",
            ascending=True
        )
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.barh(
        summary["Product_Name"],
        summary["Profit"]
    )

    ax.set_title(
        "Top 10 Products by Profit",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Profit")
    ax.set_ylabel("Product")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Zero reference line
    ax.axvline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "12_top_10_products_by_profit.png"
    )

    plt.close(fig)

    print("Chart 12 completed.")


###### CHART 13 — BOTTOM 10 PRODUCTS BY PROFIT


def bottom_10_products_by_profit(df):
    """
    Create a horizontal bar chart showing the bottom 10 products
    ranked by total profit.

    Business Purpose:
    Identifies the products with the weakest profitability and
    highlights products that may require pricing, discount,
    cost, or inventory strategy review.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 13: Bottom 10 Products by Profit...")

    summary = (
        df.groupby(
            ["Product_ID", "Product_Name"],
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=True
        )
        .head(10)
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.barh(
        summary["Product_Name"],
        summary["Profit"]
    )

    ax.set_title(
        "Bottom 10 Products by Profit",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Profit")
    ax.set_ylabel("Product")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Zero reference line
    ax.axvline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        if value >= 0:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f" {value:,.0f}",
                va="center",
                fontsize=9
            )

        else:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f"{value:,.0f} ",
                ha="right",
                va="center",
                fontsize=9
            )

    plt.tight_layout()

    save_chart(
        fig,
        "13_bottom_10_products_by_profit.png"
    )

    plt.close(fig)

    print("Chart 13 completed.")



###### CHART 14 — TOP 10 CUSTOMERS BY SALES


def top_10_customers_by_sales(df):
    """
    Create a horizontal bar chart showing the top 10 customers
    ranked by total sales.

    Business Purpose:
    Identifies high-value customers and helps management
    understand which customers contribute the most revenue.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 14: Top 10 Customers by Sales...")

    summary = (
        df.groupby(
            ["Customer_ID", "Customer_Name"],
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
        .head(10)
        .sort_values(
            "Sales",
            ascending=True
        )
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.barh(
        summary["Customer_Name"],
        summary["Sales"]
    )

    ax.set_title(
        "Top 10 Customers by Sales",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("Customer")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "14_top_10_customers_by_sales.png"
    )

    plt.close(fig)

    print("Chart 14 completed.")



###### CHART 15 — TOP 10 CUSTOMERS BY PROFIT


def top_10_customers_by_profit(df):
    """
    Create a horizontal bar chart showing the top 10 customers
    ranked by total profit.

    Business Purpose:
    Identifies customers who contribute the most profitability
    and supports customer retention and account-prioritization
    decisions.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 15: Top 10 Customers by Profit...")

    summary = (
        df.groupby(
            ["Customer_ID", "Customer_Name"],
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=False
        )
        .head(10)
        .sort_values(
            "Profit",
            ascending=True
        )
    )

    fig, ax = plt.subplots(figsize=(12, 8))

    bars = ax.barh(
        summary["Customer_Name"],
        summary["Profit"]
    )

    ax.set_title(
        "Top 10 Customers by Profit",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Profit")
    ax.set_ylabel("Customer")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Zero reference line
    ax.axvline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "15_top_10_customers_by_profit.png"
    )

    plt.close(fig)

    print("Chart 15 completed.")



###### CHART 16 — SALES BY STATE


def sales_by_state(df):
    """
    Create a horizontal bar chart showing total sales by state.

    Business Purpose:
    Compares state-level sales performance and identifies
    the strongest geographic markets.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 16: Sales by State...")

    summary = (
        df.groupby(
            "State",
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
        .head(15)
        .sort_values(
            "Sales",
            ascending=True
        )
    )

    fig, ax = plt.subplots(figsize=(12, 9))

    bars = ax.barh(
        summary["State"],
        summary["Sales"]
    )

    ax.set_title(
        "Top 15 States by Sales",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("State")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        ax.text(
            value,
            bar.get_y() + bar.get_height() / 2,
            f" {value:,.0f}",
            va="center",
            fontsize=9
        )

    plt.tight_layout()

    save_chart(
        fig,
        "16_sales_by_state.png"
    )

    plt.close(fig)

    print("Chart 16 completed.")



###### CHART 17 — PROFIT BY STATE


def profit_by_state(df):
    """
    Create a horizontal bar chart showing total profit by state.

    Business Purpose:
    Identifies the strongest and weakest states in terms of
    profitability and highlights regions requiring further
    business investigation.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 17: Profit by State...")

    summary = (
        df.groupby(
            "State",
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=True
        )
    )

    # Keep the 15 strongest and weakest states when the
    # dataset contains many states.
    if len(summary) > 30:

        lowest = summary.head(15)

        highest = summary.tail(15)

        summary = pd.concat(
            [lowest, highest]
        )

    fig, ax = plt.subplots(figsize=(12, 10))

    bars = ax.barh(
        summary["State"],
        summary["Profit"]
    )

    ax.set_title(
        "State-Level Profitability",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Profit")
    ax.set_ylabel("State")

    ax.grid(
        axis="x",
        alpha=0.3
    )

    # Zero reference line
    ax.axvline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_width()

        if value >= 0:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f" {value:,.0f}",
                va="center",
                fontsize=8
            )

        else:

            ax.text(
                value,
                bar.get_y() + bar.get_height() / 2,
                f"{value:,.0f} ",
                ha="right",
                va="center",
                fontsize=8
            )

    plt.tight_layout()

    save_chart(
        fig,
        "17_profit_by_state.png"
    )

    plt.close(fig)

    print("Chart 17 completed.")



###### CHART 18 — SALES BY SHIP MODE


def sales_by_ship_mode(df):
    """
    Create a bar chart showing total sales by shipping mode.

    Business Purpose:
    Compares revenue associated with different shipping modes
    and helps management understand customer shipping
    preferences and sales distribution.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 18: Sales by Ship Mode...")

    summary = (
        df.groupby(
            "Ship_Mode",
            as_index=False
        )["Sales"]
        .sum()
        .sort_values(
            "Sales",
            ascending=False
        )
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Ship_Mode"],
        summary["Sales"]
    )

    ax.set_title(
        "Sales by Shipping Mode",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Shipping Mode")
    ax.set_ylabel("Sales")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "18_sales_by_ship_mode.png"
    )

    plt.close(fig)

    print("Chart 18 completed.")


###### CHART 19 — PROFIT BY SHIP MODE


def profit_by_ship_mode(df):
    """
    Create a bar chart showing total profit by shipping mode.

    Business Purpose:
    Compares profitability across different shipping modes
    and helps identify whether certain shipping methods are
    associated with stronger or weaker profit performance.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 19: Profit by Ship Mode...")

    summary = (
        df.groupby(
            "Ship_Mode",
            as_index=False
        )["Profit"]
        .sum()
        .sort_values(
            "Profit",
            ascending=False
        )
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Ship_Mode"],
        summary["Profit"]
    )

    ax.set_title(
        "Profit by Shipping Mode",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Shipping Mode")
    ax.set_ylabel("Profit")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        if value >= 0:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="bottom",
                fontsize=10
            )

        else:

            ax.text(
                bar.get_x() + bar.get_width() / 2,
                value,
                f"{value:,.0f}",
                ha="center",
                va="top",
                fontsize=10
            )

    plt.tight_layout()

    save_chart(
        fig,
        "19_profit_by_ship_mode.png"
    )

    plt.close(fig)

    print("Chart 19 completed.")



###### CHART 20 — DISCOUNT VS PROFIT


def discount_vs_profit(df):
    """
    Create a scatter plot showing the relationship between
    discount percentage and profit.

    Business Purpose:
    Helps investigate whether higher discounts are associated
    with lower profitability.

    Each point represents an individual sales transaction.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 20: Discount vs Profit...")

    data = df[
        ["Discount", "Profit"]
    ].dropna().copy()

    # Convert discount from decimal to percentage
    data["Discount_Percentage"] = (
        data["Discount"] * 100
    )

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.scatter(
        data["Discount_Percentage"],
        data["Profit"],
        alpha=0.6
    )

    ax.set_title(
        "Discount vs Profit",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Discount (%)")
    ax.set_ylabel("Profit")

    ax.grid(
        alpha=0.3
    )

    # Zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    plt.tight_layout()

    save_chart(
        fig,
        "20_discount_vs_profit.png"
    )

    plt.close(fig)

    print("Chart 20 completed.")



###### CHART 21 — SALES VS PROFIT


def sales_vs_profit(df):
    """
    Create a scatter plot showing the relationship between
    sales and profit.

    Business Purpose:
    Helps identify transactions with high sales but low or
    negative profit and transactions that generate strong
    profitability.

    Each point represents an individual sales transaction.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 21: Sales vs Profit...")

    data = df[
        ["Sales", "Profit"]
    ].dropna().copy()

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.scatter(
        data["Sales"],
        data["Profit"],
        alpha=0.6
    )

    ax.set_title(
        "Sales vs Profit",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Sales")
    ax.set_ylabel("Profit")

    ax.grid(
        alpha=0.3
    )

    # Zero reference line
    ax.axhline(
        0,
        linewidth=1
    )

    plt.tight_layout()

    save_chart(
        fig,
        "21_sales_vs_profit.png"
    )

    plt.close(fig)

    print("Chart 21 completed.")



###### CHART 22 — QUANTITY BY CATEGORY


def quantity_by_category(df):
    """
    Create a bar chart showing total quantity sold by
    product category.

    Business Purpose:
    Compares product volume across categories and helps
    management understand which categories have the highest
    sales quantity.

    Parameters:
    df : pandas.DataFrame
        Preprocessed retail sales dataset.

    Returns
    -------
    None
        Saves the chart as a high-resolution PNG image.
    """

    print("Creating Chart 22: Quantity by Category...")

    summary = (
        df.groupby(
            "Category",
            as_index=False
        )["Quantity"]
        .sum()
        .sort_values(
            "Quantity",
            ascending=False
        )
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    bars = ax.bar(
        summary["Category"],
        summary["Quantity"]
    )

    ax.set_title(
        "Quantity Sold by Product Category",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Category")
    ax.set_ylabel("Quantity Sold")

    ax.grid(
        axis="y",
        alpha=0.3
    )

    # Add data labels
    for bar in bars:

        value = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value,
            f"{value:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    save_chart(
        fig,
        "22_quantity_by_category.png"
    )

    plt.close(fig)

    print("Chart 22 completed.")


# TESTING / EXECUTION BLOCK
# CHARTS 1–22


# MAIN EXECUTION BLOCK
# RUN ALL 22 VISUALIZATIONS


if __name__ == "__main__":

    print()
    print("\n")
    print("RETAIL SALES ANALYSIS - VISUALIZATION MODULE")
    print("\n")

    
    # Import project modules
    

    from database import load_data
    from preprocessing import preprocess_data

    
    # STEP 1 — LOAD DATA
    

    print()
    print("STEP 1: Loading data from MySQL...")
    print("\n")

    try:

        df = load_data()

        print("Data loaded successfully.")
        print(f"Rows    : {len(df):,}")
        print(f"Columns : {len(df.columns):,}")

    except Exception as e:

        print("ERROR: Failed to load data.")
        print(f"Details: {e}")

        raise

    
    # STEP 2 — PREPROCESS DATA
    

    print()
    print("STEP 2: Preprocessing data...")
    print("\n")

    try:

        df = preprocess_data(df)

        print("Preprocessing completed successfully.")
        print(f"Rows after preprocessing    : {len(df):,}")
        print(f"Columns after preprocessing : {len(df.columns):,}")

    except Exception as e:

        print("ERROR: Preprocessing failed.")
        print(f"Details: {e}")

        raise

    
    # TEMPORARY CHECK — FINAL DATAFRAME COLUMNS
    

    print()
    print("FINAL DATAFRAME COLUMNS")
    print("\n")

    for i, column in enumerate(df.columns, start=1):

        print(f"{i:02d}. {column}")

    print("\n")

    
    # STEP 3 — GENERATE ALL VISUALIZATIONS
    

    print()
    print("STEP 3: Generating all 22 visualizations...")
    print("\n")

    # CHART 01

    print("\n[01/22] Sales by Category")

    sales_by_category(df)

    # CHART 02

    print("\n[02/22] Profit by Category")

    profit_by_category(df)

    # CHART 03

    print("\n[03/22] Sales by Sub-category")

    sales_by_subcategory(df)

    # CHART 04

    print("\n[04/22] Profit by Sub-category")

    profit_by_subcategory(df)

    # CHART 05

    print("\n[05/22] Sales by Region")

    sales_by_region(df)

    # CHART 06

    print("\n[06/22] Profit by Region")

    profit_by_region(df)

    # CHART 07

    print("\n[07/22] Sales by Customer Segment")

    sales_by_segment(df)

    # CHART 08

    print("\n[08/22] Profit by Customer Segment")

    profit_by_segment(df)

    # CHART 09

    print("\n[09/22] Monthly Sales Trend")

    monthly_sales(df)

    # CHART 10

    print("\n[10/22] Monthly Profit Trend")

    monthly_profit(df)

    # CHART 11

    print("\n[11/22] Top 10 Products by Sales")

    top_10_products_by_sales(df)

    # CHART 12

    print("\n[12/22] Top 10 Products by Profit")

    top_10_products_by_profit(df)

    # CHART 13

    print("\n[13/22] Bottom 10 Products by Profit")

    bottom_10_products_by_profit(df)

    # CHART 14

    print("\n[14/22] Top 10 Customers by Sales")

    top_10_customers_by_sales(df)

    # CHART 15

    print("\n[15/22] Top 10 Customers by Profit")

    top_10_customers_by_profit(df)

    # CHART 16

    print("\n[16/22] Sales by State")

    sales_by_state(df)

    # CHART 17

    print("\n[17/22] Profit by State")

    profit_by_state(df)

    # CHART 18

    print("\n[18/22] Sales by Ship Mode")

    sales_by_ship_mode(df)

    # CHART 19

    print("\n[19/22] Profit by Ship Mode")

    profit_by_ship_mode(df)

    # CHART 20

    print("\n[20/22] Discount vs Profit")

    discount_vs_profit(df)

    # CHART 21

    print("\n[21/22] Sales vs Profit")

    sales_vs_profit(df)

    # CHART 22

    print("\n[22/22] Quantity by Category")

    quantity_by_category(df)

    # COMPLETION MESSAGE

    print()
    print("\n")
    print("ALL 22 VISUALIZATIONS COMPLETED SUCCESSFULLY")
    print("\n")

    print()
    print("Generated charts:")

    print("01 - Sales by Category")
    print("02 - Profit by Category")
    print("03 - Sales by Sub-category")
    print("04 - Profit by Sub-category")
    print("05 - Sales by Region")
    print("06 - Profit by Region")
    print("07 - Sales by Customer Segment")
    print("08 - Profit by Customer Segment")
    print("09 - Monthly Sales Trend")
    print("10 - Monthly Profit Trend")
    print("11 - Top 10 Products by Sales")
    print("12 - Top 10 Products by Profit")
    print("13 - Bottom 10 Products by Profit")
    print("14 - Top 10 Customers by Sales")
    print("15 - Top 10 Customers by Profit")
    print("16 - Sales by State")
    print("17 - Profit by State")
    print("18 - Sales by Ship Mode")
    print("19 - Profit by Ship Mode")
    print("20 - Discount vs Profit")
    print("21 - Sales vs Profit")
    print("22 - Quantity by Category")

    print()
    print("All charts have been saved to the Images folder.")
    print()
    print("\n")
    print("VISUALIZATION MODULE EXECUTION COMPLETED")