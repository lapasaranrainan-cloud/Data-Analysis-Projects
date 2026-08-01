USE superstore;

-- SELECT ALL
SELECT * FROM sales;

-- Total Sales:
SELECT
	ROUND(SUM(Sales),2) AS Total_Sales
FROM sales;

-- Sales by Region
SELECT
	Region,
	ROUND(SUM(Sales),2) AS Total_Sales
FROM sales
GROUP BY Region;

-- Sales by Category
SELECT 
	Category,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM sales
GROUP BY Category;

-- Top 10 Products
SELECT 
	Product_Name,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;

-- Sales by Year
SELECT
	Order_Year,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM sales
GROUP BY Order_Year
ORDER BY Order_Year ASC;

-- Customers with Highest Sales
SELECT	
	Customer_Name,
    ROUND(SUM(Sales),2) AS Total_Sales
FROM sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC;

-- Determine the average sales for every state within each region.
SELECT 
    Region,
	State,
	ROUND(AVG(Sales),2) AS Average_Sales
FROM sales
GROUP BY State, Region
ORDER BY Region;

-- Running Total of Sales by Year
SELECT
	Order_Year,
    ROUND(SUM(Sales),2) AS Yearly_Sales,
    ROUND(SUM(SUM(Sales)) OVER(
		ORDER BY Order_Year
        ), 2) AS Running_Total
FROM sales
GROUP BY Order_Year;