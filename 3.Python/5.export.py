"""
            RETAIL SALES ANALYSIS PROJECT

File Name : export.py

Purpose
---
This module is responsible for exporting processed
datasets generated during the Retail Sales Analysis
project.

"""


###### IMPORT LIBRARIES


import os
import pandas as pd


###### CREATE EXPORT FOLDER

EXPORT_FOLDER = "Exports"
os.makedirs(EXPORT_FOLDER, exist_ok=True)


###### EXPORT DATASET TO CSV

def export_csv(df,
               filename="Processed_Retail_Sales"):
    
    filepath = os.path.join(
        EXPORT_FOLDER,
        f"{filename}.csv"
    )
    df.to_csv(
        filepath,
        index=False,
        encoding="utf-8"
    )
    print("\n")
    print("CSV Export Successful")
    print(filepath)
    print("\n")


###### EXPORT DATASET TO EXCEL


def export_excel(df,
                 filename="Processed_Retail_Sales"):

    filepath = os.path.join(
        EXPORT_FOLDER,
        f"{filename}.xlsx"
    )

    df.to_excel(
        filepath,
        index=False,
        engine="openpyxl"
    )

    print("\n")
    print("Excel Export Successful")
    print(filepath)
    print("\n")


# EXPORT BOTH CSV & EXCEL


def export_dataset(df,
                   filename="Processed_Retail_Sales"):
    
    export_csv(df, filename)
    export_excel(df, filename)
    print("\nDataset exported successfully.")


###### EXPORT OVERALL KPIs


def export_kpis(df):
    
    from eda import overall_kpis

    # Generate KPI results from EDA    

    kpis = overall_kpis(df)
    
    # Convert dictionary to DataFrame


    if isinstance(kpis, dict):
        kpis = pd.DataFrame(
            list(kpis.items()),
            columns=[
                "KPI",
                "Value"
            ]
        )

    # Create output path    

    filepath = os.path.join(
        EXPORT_FOLDER,
        "Overall_KPIs.xlsx"
    )

    # Export to Excel    

    kpis.to_excel(
        filepath,
        index=False,
        engine="openpyxl"
    )
    print("Overall KPIs Exported")


###### EXPORT SALES SUMMARY


def export_sales_summary(df):
    """
    Output :
    Sales_Summary.xlsx
    """

    from eda import sales_summary
    summary = sales_summary(df)
    filepath = os.path.join(
        EXPORT_FOLDER,
        "Sales_Summary.xlsx"
    )
    summary.to_excel(
        filepath,
        engine="openpyxl"
    )
    print("Sales Summary Exported")


###### EXPORT CUSTOMER SUMMARY


def export_customer_summary(df):
    """
    Output :
    Customer_Summary.xlsx
    """

    from eda import customer_summary
    summary = customer_summary(df)
    filepath = os.path.join(
        EXPORT_FOLDER,
        "Customer_Summary.xlsx"
    )
    summary.to_excel(
        filepath,
        engine="openpyxl"
    )
    print("Customer Summary Exported")


###### EXPORT PRODUCT SUMMARY


def export_product_summary(df):
    """
    Output :
    Product_Summary.xlsx
    """
    from eda import product_summary
    summary = product_summary(df)
    filepath = os.path.join(
        EXPORT_FOLDER,
        "Product_Summary.xlsx"
    )
    summary.to_excel(
        filepath,
        engine="openpyxl"
    )
    print("Product Summary Exported")


###### EXPORT REGION SUMMARY


def export_region_summary(df):
    """
    Output :
    Region_Summary.xlsx
    """
    from eda import region_summary
    summary = region_summary(df)
    filepath = os.path.join(
        EXPORT_FOLDER,
        "Region_Summary.xlsx"
    )
    summary.to_excel(
        filepath,
        engine="openpyxl"
    )
    print("Region Summary Exported")


###### EXPORT ALL BUSINESS REPORTS


def export_reports(df):
    """
    Export all business reports.
    """

    print("\n")
    print("Exporting Business Reports...")
    print("\n")

    export_kpis(df)

    export_sales_summary(df)

    export_customer_summary(df)

    export_product_summary(df)

    export_region_summary(df)

    print("\nAll Business Reports Exported Successfully.")


###### EXPORT DATA DICTIONARY


def export_data_dictionary(df):
    """
    Export Data Dictionary.

    Creates a table containing:
    • Column Name
    • Data Type
    • Missing Values
    • Unique Values
    """
    dictionary = pd.DataFrame({
        "Column": df.columns,

        "Data Type": df.dtypes.astype(str).values,

        "Missing Values": df.isnull().sum().values,

        "Unique Values": df.nunique().values
    })

    filepath = os.path.join(
        EXPORT_FOLDER,
        "Data_Dictionary.xlsx"
    )

    dictionary.to_excel(
        filepath,
        index=False,
        engine="openpyxl"
    )

    print("Data Dictionary Exported")


###### EXPORT PROJECT METADATA


def export_metadata(df):
    """
    Export project metadata.
    """

    metadata = pd.DataFrame({
        "Property": [
            "Total Rows",
            "Total Columns",
            "Total Orders",
            "Total Customers",
            "Total Products"
        ],

        "Value": [
            len(df),
            len(df.columns),
            df["Order_ID"].nunique(),
            df["Customer_ID"].nunique(),
            df["Product_ID"].nunique()
        ]
    })

    filepath = os.path.join(
        EXPORT_FOLDER,
        "Project_Metadata.xlsx"
    )

    metadata.to_excel(
        filepath,
        index=False,
        engine="openpyxl"
    )
    print("Project Metadata Exported")


###### EXPORT PROJECT SUMMARY


def export_summary_report(df):
    """
    Export all supporting reports.
    """

    export_data_dictionary(df)

    export_metadata(df)

    print("Summary Reports Exported")


# PROJECT LOG


def project_log():

    print("\n")

    print("Retail Sales Analysis Export Completed")

    print("\n")

    print("Files exported successfully to:")

    print(EXPORT_FOLDER)

    print("\n")



###### MAIN


if __name__ == "__main__":

    from database import load_data
    from preprocessing import preprocess_data

    print("Retail Sales Export Module")
    print("\n")

    # STEP 1 — LOAD DATA

    print("\nStep 1: Loading data...")

    df = load_data()

    print(f"Rows loaded    : {len(df):,}")
    print(f"Columns loaded : {len(df.columns):,}")

    # STEP 2 — PREPROCESS DATA
    
    print("\nStep 2: Preprocessing data...")

    df = preprocess_data(df)

    print("Preprocessing completed.")

    # STEP 3 — EXPORT PROCESSED DATASET
    
    print("\nStep 3: Exporting processed dataset...")

    export_dataset(df)
    
    # STEP 4 — EXPORT BUSINESS REPORTS
    
    print("\nStep 4: Exporting business reports...")

    export_reports(df)
    
    # STEP 5 — EXPORT SUPPORTING REPORTS
    
    print("\nStep 5: Exporting supporting reports...")

    export_summary_report(df)
    
    # STEP 6 — PROJECT LOG
    
    print("\nStep 6: Creating project log...")

    project_log()
    
    # COMPLETION MESSAGE
    
    print("\n")
    print("Export Completed Successfully.")
    print("Check the Exports folder for generated files.")





   