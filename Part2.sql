USE TEST;

# Write a query to get Product list (name, unit price) of ten most expensive products.

SELECT ProductName, UnitPrice FROM Products
ORDER BY UnitPrice DESC LIMIT 10;

#Number of units in stock by Category(Category Name) and supplier country?

SELECT Categories.CategoryName, 
Suppliers.Country, 
Products.UnitsInStock
FROM Categories
INNER JOIN Products ON Products.CategoryID = Categories.CategoryID
INNER JOIN Suppliers ON Suppliers.SupplierID = Products.SupplierID
ORDER BY Products.UnitsInStock;


# Find out the quartely orders for each product for the year 1997?


SELECT a.ProductName, 
    d.CompanyName, 
    YEAR(OrderDate) AS OrderYear,
    FORMAT(sum(CASE QUARTER(c.OrderDate) WHEN '1' 
        THEN b.UnitPrice*b.Quantity*(1-b.Discount) ELSE 0 END), 0) "Qtr 1",
    FORMAT(sum(CASE QUARTER(c.OrderDate) WHEN '2' 
        then b.UnitPrice*b.Quantity*(1-b.Discount) ELSE 0 END), 0) "Qtr 2",
    FORMAT(sum(CASE QUARTER(c.OrderDate) WHEN '3' 
        then b.UnitPrice*b.Quantity*(1-b.Discount) ELSE 0 END), 0) "Qtr 3",
    FORMAT(sum(CASE QUARTER(c.OrderDate) WHEN '4' 
        then b.UnitPrice*b.Quantity*(1-b.Discount) ELSE 0 END), 0) "Qtr 4" 
FROM Products a 
INNER JOIN OrderDetails b ON a.ProductID = b.ProductID
INNER JOIN Orders c ON c.OrderID = b.OrderID
INNER JOIN Customers d ON d.CustomerID = c.CustomerID 
WHERE c.OrderDate BETWEEN DATE('1997-01-01') AND DATE('1997-12-31')
GROUP BY a.ProductName, 
    d.CompanyName, 
    YEAR(OrderDate)
ORDER BY a.ProductName, d.CompanyName;

# Give the name of employees and the city where they live for employees who have sold to customers in the same city?


SELECT DISTINCT Employees.FirstName, 
Employees.LastName, 
Employees.City
FROM Employees
INNER JOIN Customers ON Customers.City = Employees.City
ORDER BY Employees.FirstName;

# Give the names of employees who are strictly older than any employee who lives in London.


SELECT  DISTINCT E1.FirstName, E1.LastName
FROM Employees E1 , Employees E2
WHERE E1.BirthDate < E2.BirthDate AND  E2.City ='London';





