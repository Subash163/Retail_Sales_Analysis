"""
Retail Sales Analysis Project
File        : preprocessing.py
Description : Data validation and feature engineering
"""

import pandas as pd

###### DATA VALIDATION

def check_shape(df):
    return df.shape


def check_data_types(df):
    return df.dtypes


def check_missing_values(df):
    return df.isnull().sum()


def check_duplicate_rows(df):
    return df.duplicated().sum()


def check_unique_values(df):
    return df.nunique()


def statistical_summary(df):
    return df.describe(include="all")


###### DATE VALIDATION

def validate_dates(df):
    """
    Converts date columns to datetime format.
    """
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])
    return df


def shipping_validation(df):
    """
    Checks if any order was shipped before the order date.
    """
    invalid_orders = df[df["Ship_Date"] < df["Order_Date"]]
    return invalid_orders


###### FEATURE ENGINEERING

def create_features(df):
    # Order Year
    df["Order_Year"] = df["Order_Date"].dt.year

    # Order Month Number
    df["Order_Month_No"] = df["Order_Date"].dt.month

    # Month Name
    df["Order_Month"] = df["Order_Date"].dt.month_name()

    # Quarter
    df["Quarter"] = df["Order_Date"].dt.quarter

    # Day Name
    df["Day_Name"] = df["Order_Date"].dt.day_name()

    # Week Number
    df["Week_Number"] = df["Order_Date"].dt.isocalendar().week

    # Processing Days
    df["Processing_Days"] = (
        df["Ship_Date"] -
        df["Order_Date"]
    ).dt.days

    # Profit Margin
    df["Profit_Margin"] = (
        df["Profit"] /
        df["Sales"].replace(0, pd.NA)
    ) * 100

    # Average Selling Price
    df["Average_Selling_Price"] = (
        df["Sales"] /
        df["Quantity"].replace(0, pd.NA)
    )
    return df


###### BUSINESS VALIDATION

def negative_profit_orders(df):
    """
    Returns orders having negative profit.
    """
    return df[df["Profit"] < 0]


def high_discount_orders(df):
    """
    Returns orders with discount greater than 40%.
    """
    return df[df["Discount"] > 0.40]


def top_categories(df):
    """
    Sales by Category.
    """
    return (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

def top_subcategories(df):
    """
    Sales by Sub-category.
    """
    return (
        df.groupby("Sub_category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )


###### FINAL PREPROCESSING PIPELINE

def preprocess_data(df):
    """
    Complete preprocessing pipeline.
    """
    df = validate_dates(df)
    df = create_features(df)
    return df
if __name__ == "__main__":

    from database import load_data
    print("\n")
    print("Preprocessing Started")
    print("\n")
    df = load_data()
    print("\nOriginal Shape")
    print(df.shape)
    df = preprocess_data(df)
    print("\nProcessed Shape")
    print(df.shape)
    print("\nMissing Values")
    print(check_missing_values(df))
    print("\nDuplicate Rows")
    print(check_duplicate_rows(df))
    print("\nData Types")
    print(check_data_types(df))
    print("\nFirst Five Records")
    print(df.head())
