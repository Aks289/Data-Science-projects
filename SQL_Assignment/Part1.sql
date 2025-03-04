
# DDL statements to modify the tables according to the given datatypes stored in the database test
USE TEST;
ALTER TABLE Categories
MODIFY CategoryID INT(11),
MODIFY CategoryName VARCHAR(15),
MODIFY Description MEDIUMTEXT;
ALTER TABLE Customers
MODIFY CustomerID VARCHAR(5),
MODIFY CompanyName VARCHAR(40),
MODIFY ContactName VARCHAR(30),
MODIFY ContactTitle VARCHAR(30),
MODIFY Address VARCHAR(60),
MODIFY City VARCHAR(15),
MODIFY Region VARCHAR(15),
MODIFY PostalCode VARCHAR(10),
MODIFY Country VARCHAR(15),
MODIFY Phone VARCHAR(24),
MODIFY Fax VARCHAR(24);
ALTER TABLE Employees
MODIFY EmployeeID INT(11),
MODIFY LastName VARCHAR(20),
MODIFY FirstName VARCHAR(10),
MODIFY Title VARCHAR(30),
MODIFY TitleOfCourtesy VARCHAR(25),
MODIFY BirthDate DATETIME,
MODIFY HireDate DATETIME,
MODIFY Address VARCHAR(60),
MODIFY City VARCHAR(15),
MODIFY Region VARCHAR(15),
MODIFY PostalCode VARCHAR(10),
MODIFY Country VARCHAR(15),
MODIFY HomePhone VARCHAR(24),
MODIFY Extension VARCHAR(4),
MODIFY Notes MEDIUMTEXT,
MODIFY ReportsTo INT(11),
MODIFY PhotoPath VARCHAR(255),
MODIFY Salary FLOAT;

ALTER TABLE EmployeeTerritories
MODIFY EmployeeID INT(11),
MODIFY TerritoryID VARCHAR(20);

ALTER TABLE Orders
MODIFY OrderID INT(11),
MODIFY CustomerID VARCHAR(5),
MODIFY EmployeeID INT(11),
MODIFY OrderDate DATETIME,
MODIFY RequiredDate DATETIME,
MODIFY ShippedDate DATETIME,
MODIFY ShipVia INT(11),
MODIFY Freight DECIMAL(10,4),
MODIFY ShipName VARCHAR(40),
MODIFY ShipAddress VARCHAR(60),
MODIFY ShipCity VARCHAR(15),
MODIFY ShipRegion VARCHAR(15),
MODIFY ShipPostalCode VARCHAR(10),
MODIFY ShipCountry VARCHAR(15);

ALTER TABLE OrderDetails
MODIFY OrderID INT(11),
MODIFY ProductID INT(11),
MODIFY UnitPrice DECIMAL(10,4),
MODIFY Quantity SMALLINT(2),
MODIFY Discount DOUBLE(8,0);

ALTER TABLE Products
MODIFY ProductID INT(11),
MODIFY ProductName VARCHAR(40),
MODIFY SupplierID INT(11),
MODIFY CategoryID INT(11),
MODIFY QuantityPerUnit VARCHAR(20),
MODIFY UnitPrice DECIMAL(10,4),
MODIFY UnitsInStock SMALLINT(2),
MODIFY UnitsOnOrder SMALLINT(2),
MODIFY ReOrderLevel SMALLINT(2),
MODIFY Discontinued BIT(1);

ALTER TABLE Region
MODIFY RegionID INT(11),
MODIFY RegionDescription VARCHAR(50);

ALTER TABLE Shippers
MODIFY ShipperID INT(11),
MODIFY CompanyName VARCHAR(40),
MODIFY Phone VARCHAR(24);

ALTER TABLE Suppliers
MODIFY SupplierID INT(11),
MODIFY CompanyName VARCHAR(40),
MODIFY ContactName VARCHAR(30),
MODIFY ContactTitle VARCHAR(30),
MODIFY Address VARCHAR(60),
MODIFY City VARCHAR(15),
MODIFY Region VARCHAR(15),
MODIFY PostalCode VARCHAR(10),
MODIFY Country VARCHAR(15),
MODIFY Phone VARCHAR(24),
MODIFY Fax VARCHAR(24),
MODIFY HomePage MEDIUMTEXT;

ALTER TABLE Territories
MODIFY TerritoryID VARCHAR(20),
MODIFY TerritoryDescription VARCHAR(50),
MODIFY RegionID INT(11);




























