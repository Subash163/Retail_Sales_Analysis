## Data Validation Retail Sales Analysis

##Check 1 : Row Counts
SELECT 'Customers' AS Table_Name, COUNT(*) AS Total_Rows
FROM Customers
UNION ALL
SELECT 'Products', COUNT(*)
FROM Products
UNION ALL
SELECT 'Orders', COUNT(*)
FROM Orders
UNION ALL
SELECT 'Sales', COUNT(*)
FROM Sales;

##Check 2 : Orders without Customers
SELECT *
FROM Orders o
LEFT JOIN Customers c
ON o.Customer_ID = c.Customer_ID
WHERE c.Customer_ID IS NULL;

##Check 3: Sales without Orders
SELECT *
FROM Sales s
LEFT JOIN Orders o
ON s.Order_ID = o.Order_ID
WHERE o.Order_ID IS NULL;

##Check 4 : Sales without Products
SELECT *
FROM Sales s
LEFT JOIN Products p
ON s.Product_ID = p.Product_ID
WHERE p.Product_ID IS NULL;

##Check 5 : Duplicate Customers
SELECT
Customer_ID,
COUNT(*)
FROM Customers
GROUP BY Customer_ID
HAVING COUNT(*)>1;

##Check 6 : Duplicate Orders
SELECT
Order_ID,
COUNT(*)
FROM Orders
GROUP BY Order_ID
HAVING COUNT(*)>1;

##Check 7 : Duplicate Products
SELECT
Product_ID,
COUNT(*)
FROM Products
GROUP BY Product_ID
HAVING COUNT(*)>1;

##Check 8 : Sales Record Validation
SELECT
COUNT(*) AS Sales_Rows,
COUNT(DISTINCT Order_ID) AS Orders,
COUNT(DISTINCT Product_ID) AS Products
FROM Sales;