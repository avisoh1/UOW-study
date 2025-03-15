-- Lecture 6 Example 2
-- Foreign key

DROP TABLE Team;

CREATE TABLE Team
(
	name VARCHAR(20),
category VARCHAR(10) NOT NULL,
score INT NOT NULL DEFAULT 0,
CONSTRAINT teamPK PRIMARY KEY(name),
CONSTRAINT teamChk1 CHECK
(category IN ('Junior', 'Family', 'Open')),
CONSTRAINT teamChk2 CHECK (score >= 0)
);

-- Insert a few rows
INSERT INTO team (name, category)
	VALUES ('t1','Junior');
INSERT INTO team (name, category)
	VALUES ('t2','Family');
INSERT INTO team (name, category)
	VALUES ('t3','Open');
INSERT INTO team (name, category)
	VALUES ('t4','Open');

-- Second table
DROP TABLE TeamMember;

CREATE TABLE TeamMember
(
	ref_no CHAR(4),
	name VARCHAR(30) NOT NULL, 
    team VARCHAR(20) NOT NULL,
    CONSTRAINT memberPK PRIMARY KEY(ref_no),
    CONSTRAINT memberFK FOREIGN KEY(team)
						REFERENCES Team(name)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
);

-- Insert rows into TeamMember table
INSERT INTO TeamMember VALUES ('m1','Alice','t99'); -- Error
INSERT INTO TeamMember VALUES ('m11','Alice','t1');
INSERT INTO TeamMember VALUES ('m21','Larry','t2');

-- UPDATE that will fail because of FOREIGN KEY constraint violation
UPDATE team SET name = 't11' WHERE name = 't1';

-- DELETE that will fail because of the same reason
DELETE FROM team WHERE name = 't2';

-- UPDATE or DELETE 't3' and 't4' will be ok
UPDATE team SET name = 't33' WHERE name = 't3';
DELETE FROM team WHERE name = 't4';

-- Quick check
SELECT * FROM team;
SELECT * FROM teamMember;