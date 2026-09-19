"""
Retail Sales Analysis Project
File        : eda.py
Description : Business summaries and KPI calculations
"""

import pandas as pd


###### OVERALL BUSINESS KPIs

def overall_kpis(df):
    """
    Returns overall business KPIs.
    """

    return {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Total Profit": round(df["Profit"].sum(), 2),
        "Total Orders": df["Order_ID"].nunique(),
        "Total Customers": df["Customer_ID"].nunique(),
        "Total Products": df["Product_ID"].nunique(),
        "Total Quantity": df["Quantity"].sum(),
        "Average Sales": round(df["Sales"].mean(), 2),
        "Average Profit": round(df["Profit"].mean(), 2),
        "Average Discount": round(df["Discount"].mean(), 2)
    }


###### SALES SUMMARY

def sales_summary(df):

    return (
        df.groupby("Category")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum"),
            Quantity=("Quantity","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### SUB CATEGORY SUMMARY

def subcategory_summary(df):

    return (
        df.groupby(["Category","Sub_category"])
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### CUSTOMER SUMMARY

def customer_summary(df):

    return (
        df.groupby(["Customer_ID","Customer_Name"])
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum"),
            Orders=("Order_ID","nunique")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### PRODUCT SUMMARY

def product_summary(df):

    return (
        df.groupby("Product_Name")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum"),
            Quantity=("Quantity","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### REGION SUMMARY

def region_summary(df):

    return (
        df.groupby("Region")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### STATE SUMMARY

def state_summary(df):

    return (
        df.groupby("State")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### CITY SUMMARY

def city_summary(df):

    return (
        df.groupby("City")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### SEGMENT SUMMARY

def segment_summary(df):

    return (
        df.groupby("Segment")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### SHIP MODE SUMMARY

def shipmode_summary(df):

    return (
        df.groupby("Ship_Mode")
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Sales",ascending=False)
    )


###### MONTHLY SALES TREND

def monthly_sales(df):

    return (
        df.groupby(["Order_Year","Order_Month_No","Order_Month"])
        .agg(
            Total_Sales=("Sales","sum"),
            Total_Profit=("Profit","sum")
        )
        .reset_index()
        .sort_values(["Order_Year","Order_Month_No"])
    )


###### TOP 10 CUSTOMERS

def top_customers(df):

    return customer_summary(df).head(10)


###### TOP 10 PRODUCTS

def top_products(df):

    return product_summary(df).head(10)


###### LOSS MAKING PRODUCTS

def loss_products(df):

    return (
        df.groupby("Product_Name")
        .agg(
            Total_Profit=("Profit","sum")
        )
        .sort_values("Total_Profit")
        .head(10)
    )


###### HIGH DISCOUNT PRODUCTS

def high_discount_products(df):

    return (
        df.groupby("Product_Name")
        .agg(
            Average_Discount=("Discount","mean")
        )
        .sort_values("Average_Discount",ascending=False)
        .head(10)
    )


###### CORRELATION MATRIX

def correlation_matrix(df):

    return df[
        [
            "Sales",
            "Profit",
            "Quantity",
            "Discount",
            "Processing_Days",
            "Profit_Margin"
        ]
    ].corr()