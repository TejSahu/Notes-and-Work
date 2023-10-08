SELECT (COUNT(DISTINCT SALESMAN_ID))
FROM ORDERS;

ALTER TABLE DEPARTMENT ADD CONSTRAINT UNIQUE_KEY_DEPTNAME UNIQUE (DEPTNAME);


       
SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

CREATE INDEX index_name
ON table_name (column1, column2, ...);


#EXPLAIN PLAN QUERIES
EXPLAIN PLAN FOR
SELECT * FROM your_table WHERE your_condition;
SET AUTOTRACE ON;
SET AUTOTRACE OFF;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);



SELECT ID, Name, Salary FROM employees
UNION
SELECT ID, Name, Salary FROM contractors;
The number of columns and their data types must be the same in both SELECT queries for the UNION operator to work. If the column names are not the same, you can use aliases to ensure the result set has meaningful column names.

# How to use index
SELECT /*+ INDEX (columnname indexname)*/ employee_id, department_id
  FROM employees 
  WHERE department_id > 50;
  
CREATE INDEX index_name
ON table_name (column1, column2, ...);

SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;

CREATE INDEX index_name
ON table_name (column1, column2, ...);


#EXPLAIN PLAN QUERIES
EXPLAIN PLAN FOR
SELECT * FROM your_table WHERE your_condition;
SET AUTOTRACE ON;
SET AUTOTRACE OFF;

SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY);




SELECT ID, Name, Salary FROM employees
UNION
SELECT ID, Name, Salary FROM contractors;
The number of columns and their data types must be the same in both SELECT queries for the UNION operator to work. If the column names are not the same, you can use aliases to ensure the result set has meaningful column names.


#  Change postgres password
ALTER USER postgres PASSWORD '<new-password>';
Or in one line

sudo -u postgres psql -c "ALTER USER postgres PASSWORD '<new-password>';"


# Make index INVISIBLE
To make an index invisible, run the following query:

SQL
ALTER TABLE your_table_name;
ALTER INDEX your_index_name INVISIBLE;
You can now run any applicable queries to see how performance is impacted. If you realize you still need this index, you can make it visible again with:

SQL
ALTER TABLE your_table_name;
ALTER INDEX your_index_name VISIBLE;
