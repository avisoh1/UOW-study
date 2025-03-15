-- Lecture 8 (2/5/2024)
USE lecture7;
SELECT *
FROM department, course
WHERE name = offered_by;

-- Different way to write a join
SELECT * 
FROM department JOIN course
ON name = offered_by;

-- Show departments + courses
-- Show only Physics and Mathematics departments
SELECT * 
FROM department JOIN course
WHERE name = offered_by
AND   name IN ('physics','mathematics');

SELECT * 
FROM department JOIN course
WHERE name = offered_by
AND   (name = 'physics'
OR 	  name = 'mathematics');

SELECT * 
FROM 	department JOIN course
ON   	name = offered_by
WHERE 	name in ('physics','mathematics');

-- Switch to lab3 database
USE lab3;
SELECT * FROM country;
SELECT * FROM department;

-- Show region_name, country_name, city, department_name of all the departments
SELECT C.region_name, C.country_name, D.city, D.department_name
FROM country C, department D
WHERE C.country_name = D.country_name
ORDER BY C.region_name, C.country_name;

SELECT C.region_name, C.country_name, D.city, D.department_name 
FROM 	country C  JOIN department D
ON   	C.country_name = D.country_name
ORDER BY C.region_name, C.country_name;

-- Job and Employee
SELECT * FROM job;
SELECT employee_id, job_title, hire_date FROM employee;

-- Show job, salary range, employee_id, first_name, hire_date
SELECT J.job_title, J.min_salary, J.max_salary, E.employee_id, E.first_name, E.hire_date
FROM job J, employee E
WHERE J.job_title = E.job_title;

SELECT J.job_title, J.min_salary, J.max_salary, E.employee_id, E.first_name, E.hire_date
FROM job J JOIN employee E
ON J.job_title = E.job_title;

-- Same query but only employees hired in 1998
SELECT J.job_title, J.min_salary, J.max_salary, E.employee_id, E.first_name, E.hire_date
FROM job J JOIN employee E
ON J.job_title = E.job_title
WHERE YEAR(hire_date) = 1998;

-- Join 3 tables
SELECT C.region_name, C.country_name,
	   D.city, D.department_name,
       E.employee_id, E.first_name, E.job_title
FROM country C, department D, employee E
WHERE C.country_name = D.country_name
AND D.department_name = E.department_name;

SELECT C.region_name, C.country_name,
	   D.city, D.department_name,
       E.employee_id, E.first_name, E.job_title
FROM country C JOIN department D 
ON C.country_name = D.country_name
JOIN employee E
ON D.department_name = E.department_name;

-- Outer join
SELECT J.job_title, min_salary, max_salary
	   E.employee_id, first_name, E.job_title
FROM job J JOIN employee E
ON 	 J.job_title = E.job_title;

SELECT J.job_title, min_salary, max_salary
	   E.employee_id, first_name, E.job_title
FROM job J LEFT JOIN employee E
ON 	 J.job_title = E.job_title;

SELECT * FROM employee WHERE job_title = 'public accountant';

-- Find countries without department
SELECT C.region_name, C.country_name, 
	   D.department_name, D.Country_name
FROM   department D RIGHT JOIN country C
ON 	   C.country_name = D.country_name;

SELECT C.region_name, C.country_name, 
	   D.department_name, D.Country_name
FROM   Country C LEFT JOIN department D
ON 	   C.country_name = D.country_name
WHERE  D.department_name IS NULL;

-- Subquery -SELECT statement containing SELECT
SELECT *
FROM job
WHERE job_title NOT IN (SELECT job_title FROM employee); 
