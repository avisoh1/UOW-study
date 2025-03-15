# Lab4. CREATE USER ... GRANT ...

-- (2)
CREATE USER user1 IDENTIFIED BY 'test';
CREATE USER user2 IDENTIFIED BY 'test';
CREATE USER user3 IDENTIFIED BY 'test';

-- (3)
GRANT SELECT ON lab4.* TO user1;

-- (4)
GRANT INSERT, UPDATE, DELETE ON lab4.employee
	TO user2 WITH GRANT OPTION; /*GET PERMISSION*/

-- (5)
GRANT CREATE ON lab4.* TO user3;

-- (6)
GRANT SELECT (department_name, street_address, city, country_name) ON lab4.department TO user3;

-- To verify (2)
SELECT * FROM mysql.user;

-- To verify (3)
SELECT * FROM mysql.db;

-- To verify (4)
SELECT * FROM mysql.tables_priv;

-- To verify (5)
SELECT * FROM mysql.db;

-- To verify (6)
SELECT * FROM mysql.columns_priv;

-- To verify
SELECT * FROM employee;

-- To remove all the users created in this lab
DROP USER user1;
DROP USER user2;
DROP USER user3;

select * from employee;

/*Revise*/
SELECT E.employee_id, E.department_name, 
	   Sup.department_name, Sup.employee_id, Sup.job_title
FROM employee E, employee Sup
WHERE E.supervisor_id = Sup.employee_id
AND E.department_name != Sup.department_name;
