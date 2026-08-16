CREATE DATABASE Retail_Sales_Analysis;
USE Retail_Sales_Analysis;

CREATE TABLE stg_retail_sales
(
    row_id INT,
    order_id VARCHAR(30),
    order_date VARCHAR(20),
    ship_date VARCHAR(20),
    ship_mode VARCHAR(50),

    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    segment VARCHAR(50),

    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    region VARCHAR(50),

    product_id VARCHAR(30),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),

    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(10,4)
);

CREATE TABLE customers (
	Customer_ID VARCHAR(20) PRIMARY KEY,
    Customer_Name VARCHAR(100) NOT NULL,
    Segment VARCHAR(20) NOT NULL
);

CREATE TABLE products (
	Product_ID VARCHAR(30) PRIMARY KEY,
    Category VARCHAR(50) NOT NULL,
    Sub_category VARCHAR(50) NOT NULL,
    Product_name VARCHAR(255) NOT NULL
);

CREATE TABLE orders (
	Order_ID VARCHAR(30) PRIMARY KEY,
    Customer_ID VARCHAR(20) NOT NULL,
    Order_Date DATE NOT NULL,
    Ship_Date DATE NOT NULL,
    Ship_Mode VARCHAR(50) NOT NULL,
    Counry VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    Postal_code VARCHAR(20) NOT NULL,
    Region VARCHAR(30) NOT NULL,
    
    CONSTRAINT chk_ship_date
		CHECK (Ship_Date >= Order_Date),
        
	CONSTRAINT fk_orders_customer
		FOREIGN KEY (Customer_ID) 
        REFERENCES Customers (Customer_ID)
);

CREATE TABLE sales (
	Sales_ID INT AUTO_INCREMENT PRIMARY KEY,
    Order_ID VARCHAR(30) NOT NULL,
    Product_ID VARCHAR(30) NOT NULL,
    Sales DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL,
    Discount DECIMAL(5,2) NOT NULL,
    Profit DECIMAL(10,4) NOT NULL,
    
    CONSTRAINT fk_sales_order
		FOREIGN KEY (Order_ID)
        REFERENCES orders (Order_ID),
        
	CONSTRAINT fk_sales_product
		FOREIGN KEY (Product_ID)
        REFERENCES products (Product_ID)
);

Use retail_sales_analysis;
INSERT INTO customers (
	Customer_ID,
    Customer_Name,
	Segment
)

SELECT DISTINCT 
	Customer_ID,
    Customer_Name,
	Segment
FROM stg_retail_sales;

INSERT INTO Products
(
    Product_ID,
    Category,
    Sub_Category,
    Product_Name
)
SELECT
    Product_ID,
    MAX(Category),
    MAX(Sub_Category),
    MAX(Product_Name)
FROM stg_retail_sales
GROUP BY Product_ID;

INSERT INTO Orders
(
    Order_ID,
    Customer_ID,
    Order_Date,
    Ship_Date,
    Ship_Mode,
    Country,
    City,
    State,
    Postal_Code,
    Region
)
SELECT DISTINCT
    Order_ID,
    Customer_ID,
    Order_Date,
    Ship_Date,
    Ship_Mode,
    Country,
    City,
    State,
    Postal_Code,
    Region
FROM stg_retail_sales;

INSERT INTO Sales
(
    Order_ID,
    Product_ID,
    Sales,
    Quantity,
    Discount,
    Profit
)

SELECT
    Order_ID,
    Product_ID,
    Sales,
    Quantity,
    Discount,
    Profit
FROM stg_retail_sales;





