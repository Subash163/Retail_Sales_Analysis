"""
=========================================================
Retail Sales Analysis Project
File        : database.py
Description : Connects to MySQL, loads normalized tables,
              merges them into a single DataFrame.
=========================================================
"""

import pandas as pd

print("Step 1: database.py started")

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.exc import SQLAlchemyError

# Import database configuration
from config import (
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)


# =========================================================
# Create MySQL Engine
# =========================================================

def get_engine():
    """
    Creates and returns a SQLAlchemy Engine.
    """
    print("Step 2: Creating SQLAlchemy Engine")

    connection_url = URL.create(
        drivername="mysql+pymysql",
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database=DATABASE
    )

    return create_engine(connection_url)


# =========================================================
# Test Database Connection
# =========================================================

def test_connection():
    """
    Tests the MySQL database connection.

    Returns
    -------
    bool
    """
    print("Step 3: Testing Database Connection")

    try:

        engine = get_engine()

        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        print("✅ MySQL Connection Successful")

        return True

    except SQLAlchemyError as e:

        print("❌ Database Connection Failed")
        print(e)

        return False


# =========================================================
# Load Individual Tables
# =========================================================

def load_tables():
    """
    Loads all normalized tables from MySQL.

    Returns
    -------
    dict
        Dictionary containing all DataFrames.
    """
    print("Step 4: Loading Tables")

    try:

        engine = get_engine()

        customers = pd.read_sql(
            "SELECT Customer_ID, Customer_Name, Segment FROM customers", engine)

        print("Customers Loaded")

        products = pd.read_sql("""

            SELECT
                Product_ID,
                Category,
                Sub_category,
                Product_Name
            FROM products

        """, engine)

        print("Products Loaded")

        orders = pd.read_sql("""

            SELECT
                Order_ID,
                Customer_ID,
                Order_Date,
                Ship_Date,
                Ship_Mode,
                Country,
                City,
                State,
                Postal_code,
                Region
            FROM orders

        """, engine)

        print("Orders Loaded")

        sales = pd.read_sql("""

            SELECT
                Sales_ID,
                Order_ID,
                Product_ID,
                Sales,
                Quantity,
                Discount,
                Profit
            FROM sales

        """, engine)

        print("Sales Loaded")

        print("✅ Tables Loaded Successfully\n")

        return {
            "customers": customers,
            "products": products,
            "orders": orders,
            "sales": sales
        }

    except SQLAlchemyError as e:

        print("❌ Error loading tables.")
        print(e)

        return None


# =========================================================
# Merge Tables
# =========================================================

def load_data():
    """
    Merges normalized tables into a single DataFrame.

    Returns
    -------
    pandas.DataFrame
    """

    tables = load_tables()

    if tables is None:
        return None

    customers = tables["customers"]
    products = tables["products"]
    orders = tables["orders"]
    sales = tables["sales"]

    df = (
        sales
        .merge(
            orders,
            on="Order_ID",
            how="inner"
        )
        .merge(
            customers,
            on="Customer_ID",
            how="inner"
        )
        .merge(
            products,
            on="Product_ID",
            how="inner"
        )
    )

    print("✅ Tables Merged Successfully\n")

    return df


# =========================================================
# Dataset Information
# =========================================================

def dataset_info(df):
    """
    Displays dataset summary.
    """

    print("=" * 60)
    print("DATASET SUMMARY")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names\n")

    for column in df.columns:
        print(column)

    print("\nData Types\n")

    print(df.dtypes)


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Retail Sales Analysis")
    print("=" * 60)

    if test_connection():

        df = load_data()

        if df is not None:

            dataset_info(df)

            print("\nFirst Five Records\n")

            print(df.head())

        else:

            print("Dataset could not be created.")

