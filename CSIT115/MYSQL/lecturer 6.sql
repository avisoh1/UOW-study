
DROP TABLE eventHelper;

-- Example of using CREATE TABLE statement

CREATE TABLE eventHelper
(
	phone CHAR(8),
    email VARCHAR(30) NOT NULL,
    name  VARCHAR(30) NOT NULL, -- []FOR CERTAIN NOUN
    hours INT,
    CONSTRAINT helperPK PRIMARY KEY(phone),
    -- PRIMARY KEY implies NOT NULL and UNIQUE
    CONSTRAINT helperCK UNIQUE(email),
    CONSTRAINT hoursCHK CHECK(hours >= 0)
);

-- Insert statement is to add row to the table
INSERT INTO eventHelper VALUES ('90000001','alice@mail.com','Alice Tan',20);
INSERT INTO eventHelper VALUES ('90000001','james@mail.com','Jame',40); --error
INSERT INTO eventHelper VALUES ('90000002','james@mail.com','NULL',40); --error

-- Quick test to check that the table is created
SELECT * 
FROM eventHelper;