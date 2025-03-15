/*Avis Oh Xin Wan UOW ID:8465678
  Assignment 2 Task 1 Alter Tables*/
SELECT * FROM Diploma;
SELECT * FROM Module;
SELECT * FROM Dipmod;
SELECT * FROM Lecturer;
SELECT * FROM Specialty;

-- B) ALTER TABLE STATEMENTS
-- Add a column called head to the Diploma table. The column serves as a foreign key to the Lecturer table.
ALTER TABLE Diploma
ADD COLUMN head VARCHAR(30) NULL,
ADD CONSTRAINT Diploma_FK1 FOREIGN KEY(head)
	REFERENCES Lecturer(emp_id)
    ON UPDATE CASCADE
    ON DELETE SET NULL;

INSERT INTO Lecturer VALUES 
        ( 'E001'
        , 'Tan Xiu Kee'
        , STR_TO_DATE('10-02-1972', '%d-%m-%Y')
        ,'F'
        ,'xktan@outlook.com'
        );
        
INSERT INTO Diploma VALUES 
        ( 'DipIT'
        , 'Diploma in Information Technology'
        , 'E001'
        );

-- When the lecturer who is the head of a diploma changes his emp_id, Diploma.head must be updated automatically.
UPDATE Lecturer
SET emp_id = 'E002'
WHERE email = 'xktan@outlook.com';

-- When a lecturer who is the head of a diploma leaves the institute and his record is deleted. Diploma.head must be set to null automatically.
DELETE FROM Lecturer
WHERE emp_id='E002';
