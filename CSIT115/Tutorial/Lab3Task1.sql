INSERT INTO EMPLOYEE VALUES 
        ( 300
        , 'Harry'
        , 'Potter'
        , 'harrypotter@gmail.com'
        , '515.123.8182'
        , STR_TO_DATE('10-02-2010', '%d-%m-%Y')
        , 'Programmer'
        , 7000
        , NULL
        , 102
        , 'Information Technology'
        );
        
SELECT * FROM employee;

DELETE FROM jobhistory WHERE employee_id = 206;

DELETE FROM employee WHERE employee_id = 206;
        
SELECT * FROM Location;

SELECT * FROM Department WHERE department_name = 'Human Resources';

INSERT INTO LOCATION VALUES
    ( '100 Century Avenue'
	, '200120'
	, 'ShangHai'
	, 'NULL'
	, 'China' );

UPDATE DEPARTMENT 
SET street_address = '100 Century Avenue',
	postal_code = 200120,
	city = 'ShangHai',
	country_name = 'China'
    WHERE department_name = 'Human Resources';