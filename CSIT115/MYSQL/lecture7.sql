#Lecturer 7 SELECT statement (30/4)
SELECT name, code
FROM department;

SELECT cnum, title, credits
FROM course;

-- 6-credits unit course
SELECT * 
FROM course
WHERE credits = 6
AND title = 'relativity';

-- Database courses or credits = 12
SELECT * 
FROM course
WHERE title = 'databases'
OR credits = 12;

-- Courses offered by Physics department
SELECT *
FROM course
WHERE offered_by = 'physics';

-- Courses not offered by Physics department
SELECT *
FROM course
WHERE offered_by <> 'physics'; /*WHERE NOT and != also can use*/

-- To get all records including NULL
SELECT *
FROM course
WHERE offered_by != 'physics'
OR    offered_by is NULL; /* = NULL cannot use*/

-- Derived (calculated) columns 
SELECT *, budget/total_staff_number AS Average_fund
FROM department;

SELECT name, 
		budget AS Current_budget,
		budget * 1.1 AS Next_year_budget
FROM department;

-- Sort the result of a query
SELECT   offered_by, cnum, title, credits
FROM 	 course
ORDER BY offered_by DESC;
/*DESC means descending order
  ASC means ascending order (default)*/

SELECT offered_by, cnum, title, credits
FROM   course
ORDER BY offered_by, credits DESC;

-- Switch to the database used in lab 3
use lab3;
SELECT * 
FROM department;

SELECT country_name, department_name, city
FROM department
ORDER BY country_name, department_name;

-- LIKE and % _
-- % can match any number of characters
-- _ can matches 1 character
SELECT *
FROM department
WHERE department_name LIKE 'A%';

-- Employees with last_name C...
SELECT *
FROM employee
WHERE last_name LIKE 'C%';

SELECT *
FROM employee
WHERE job_title LIKE '%Manager';

-- Date-related function
-- YEAR, MONTH, DAY, CURDATE
SELECT employee_id, first_name, hire_date
FROM employee
WHERE YEAR(hire_date) = 1999;

SELECT employee_id, first_name, hire_date,
	YEAR(hire_date), MONTH(hire_date), DAY(hire_date)
FROM employee;

-- Employees hired between 1995 and 2000
SELECT employee_id, first_name, hire_date,job_title
FROM employee
WHERE YEAR(hire_date) >= 1995
AND   YEAR(hire_date) <= 2000;

SELECT employee_id, first_name, hire_date,job_title
FROM employee
WHERE hire_date >='1995-01-01' 
AND hire_date   <='2000-12-31';

-- Aggregate function
-- COUNT, SUM, MIN, MAX, AVG
-- They produce only 1 value (1 row, 1 column)
SELECT *
FROM job;
SELECT COUNT(*)
FROM job;
SELECT * FROM employee WHERE YEAR(hire_date) <= 1995;
SELECT COUNT(*) FROM employee WHERE YEAR(hire_date) <= 1995;

-- How many employees do we have?
SELECT COUNT(*) FROM employee;

-- How many employees in Accounting department?
SELECT COUNT(*) FROM employee WHERE department_name = 'Accounting';

-- MIN - smallest value in a column
-- MAX - largest value in a column
SELECT MIN(salary), MAX(salary), AVG(salary)
FROM employee
WHERE department_name = 'Accounting';

SELECT salary
FROM employee
WHERE department_name = 'Accounting';

-- GROUP BY
-- Usually used with COUNT, MIN, MAX, etc
SELECT   department_name, COUNT(*)
FROM 	 employee
GROUP BY department_name;

SELECT COUNT(*) FROM employee;

-- Show the min, max and avg salary of each department
SELECT department_name, 
	   MIN(salary) AS Poor_guy, 
       MAX(salary) AS Happy_guy, 
       AVG(salary) AS Higher_please
FROM employee
WHERE department_name IS NOT NULL
GROUP BY department_name;

-- Min and max salary according
-- to department_name and job_title
SELECT department_name, job_title, COUNT(*), 
	   MIN(salary), MAX(salary)
FROM employee
GROUP BY department_name, job_title;

-- Find the total cost (i.e. sum of salary) of each department
SELECT department_name, SUM(salary) AS Monthly_cost
FROM employee
GROUP BY department_name;

-- Show the number of employees hired in each year?
SELECT YEAR(hire_date), COUNT(*) AS Employees_hired
FROM employee
GROUP BY YEAR(hire_date);

SELECT YEAR(hire_date), department_name, COUNT(*) AS Employees_hired
FROM employee
GROUP BY YEAR(hire_date), department_name;

-- Join
-- SELECT from multiple tables and combine the rows

-- Department and Employee
SELECT department_name, country_name FROM department;
SELECT employee_id, department_name FROM employee;

SELECT D.department_name, E.employee_id,E.department_name
FROM department D, employee E
WHERE D.department_name = E.department_name;

-- Switching back to the Department, Course database
use lecture7;

SELECT * FROM department;
SELECT * FROM course;

SELECT *
FROM department, course 
WHERE department.name = course.offered_by;



