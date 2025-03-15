DROP TABLE course;
DROP TABLE department;
CREATE TABLE department(
  name               VARCHAR(50)  NOT NULL,
  code               CHAR(5)      NOT NULL,
  total_staff_number DECIMAL(2)   NOT NULL,
  chair              VARCHAR(50),
  budget             DECIMAL(9,1) NOT NULL,
  CONSTRAINT dept_pkey PRIMARY KEY(name),
  CONSTRAINT dept_ckey1 UNIQUE(code),
  CONSTRAINT dept_ckey2 UNIQUE(chair),
  CONSTRAINT dept_check1 CHECK (total_staff_number BETWEEN 1 AND 50)
 );
CREATE TABLE course(
  cnum       CHAR(7) NOT NULL,
  title      VARCHAR(200) NOT NULL,
  credits    DECIMAL(2) NOT NULL,
  offered_by VARCHAR(50) NULL,
  CONSTRAINT course_pkey PRIMARY KEY(cnum),
  CONSTRAINT course_check1 CHECK (credits IN (6, 12)),
  CONSTRAINT course_fkey1 FOREIGN KEY(offered_by)
				          REFERENCES department(name) ON DELETE CASCADE
  );
-- Records
INSERT INTO department
  VALUES ('Computer Science', 'CSCI', 30, 'Peter', 123456.9 );
INSERT INTO department(name, code, chair, budget, total_staff_number)
  VALUES ('Mathematics', 'MATH', NULL, 12345.6, 10);
INSERT INTO department
  VALUES('Physics','PHY',5,NULL,5000.6);
INSERT INTO department
  VALUES('Business','BUS',3,'James Bond',500000);

INSERT INTO course VALUES('CSCI235', 'Databases', 6, 'Computer Science');
INSERT INTO course (cnum, title, offered_by, credits)
                   VALUES('MATH345', 'Topology', 'Mathematics', 6);

INSERT INTO course VALUES('CSCI111', 'C++', 6, 'Computer Science');
INSERT INTO course VALUES('PHYS312', 'Relativity', 6, 'Physics');
INSERT INTO course VALUES('MATH111', 'Calculus', 12, 'Mathematics');
INSERT INTO course VALUES('MECH111', 'Mechanics', 12, 'Physics');
INSERT INTO course VALUES('MATH312', 'Relativity', 6, 'Mathematics');
INSERT INTO course VALUES('COMP999', 'C Programming', 6, NULL);

  
