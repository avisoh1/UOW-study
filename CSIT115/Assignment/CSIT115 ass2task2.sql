/*Avis Oh Xin Wan UOW ID:8465678
  Assignment 2 Task 2 */
-- A)
SELECT C.code, C.category, C.name, C.level
FROM course C LEFT JOIN offeredcourse O
ON C.code= O.code;

-- B) 
SELECT T.empId, T.name, T.dob, T.trainYears
FROM offeredcourse O JOIN trainer T
ON O.trainer = T.empId
GROUP BY trainer
ORDER BY trainYears DESC;

-- C)
SELECT C.code, C.category, C.name, C.level
FROM course C JOIN offeredcourse O
ON C.code= O.code;

-- D)
INSERT INTO Trainer VALUES ('T091', 'Zha Teck', '1985-10-25', 10);
INSERT INTO Qualification VALUES ('T091', 'Bsc Business, MBA');

UPDATE Qualification
SET certificate = 'Bsc Business, MBA'
WHERE trainer = 'T091';

-- E)
SELECT code, category, name, level ++1 AS new_level
FROM course
WHERE category = 'Dessert';