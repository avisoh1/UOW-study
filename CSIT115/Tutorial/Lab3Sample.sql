-- ALTER TABLE statement is used to change the structure of a table without dropping/creating the table.
CREATE TABLE sample
(
	c1 INT,
    c2 INT DEFAULT 0,
    CONSTRAINT samplePK PRIMARY KEY(c1)
);

-- Add sample record
INSERT INTO sample VALUES (1,1);
INSERT INTO sample VALUES (2,2);

-- Add column 
ALTER TABLE sample ADD COLUMN c3 INT NOT NULL;
ALTER TABLE sample ADD COLUMN c4 CHAR(4) NOT NULL;

-- Add constraint
ALTER TABLE sample 
ADD CONSTRAINT c3Chk CHECK (c3 >= 0 AND c3<= 100);

-- Test the CHECK constraint
INSERT INTO sample VALUES (99,99,101,'ZZZZ');

-- To confirm that an empty string ' ' is added in c4
INSERT INTO sample VALUES(3,3,3,'xxxx');
UPDATE sample SET c3 = -10 WHERE c1 = 1;

-- CHECK
SELECT * FROM sample;
SELECT * FROM sample WHERE c4 = 'xxxx';
SELECT * FROM sample WHERE c4 = ' ';