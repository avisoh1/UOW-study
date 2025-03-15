/*Avis Oh Xin Wan UOW ID:8465678
  Assignment 2 Task 2 */
-- A)
SELECT C.code, C.category, C.name, C.level
FROM course C LEFT JOIN offeredcourse O
ON C.code= O.code 
WHERE O.code IS NULL;

SELECT * FROM offeredcourse;
SELECT * FROM course;

-- B) 
SELECT T.empId, T.name, T.dob, T.trainYears
FROM offeredcourse O JOIN trainer T
ON O.trainer = T.empId
GROUP BY trainer
HAVING COUNT(trainer) >2
ORDER BY trainYears DESC;

SELECT * FROM trainer;

-- C)
SELECT C.code, C.category, C.name, C.level
FROM course C JOIN offeredcourse O
ON C.code= O.code
WHERE MONTH(startDate) = 6;

-- D)
INSERT INTO Qualification VALUES ('T091', 'Bsc Business, MBA');
INSERT INTO Trainer VALUES ('T091', 'Zha Teck', '1985-10-25', 10);

SELECT * FROM trainer;
SELECT * FROM qualification;

-- E)
UPDATE course
SET level = level ++1 
WHERE category = 'Dessert';

DROP TABLE QUALIFICATION;
DROP TABLE ENROLMENT;
DROP TABLE OFFEREDCOURSE;
DROP TABLE TRAINER;
