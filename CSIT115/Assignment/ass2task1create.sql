/*Avis Oh Xin Wan UOW ID:8465678
  Assignment 2 Task 1 Create Tables*/
CREATE TABLE Diploma(
	code    VARCHAR(5) 	NOT NULL,
    name 	VARCHAR(50) NOT NULL,
 CONSTRAINT Diploma_PK PRIMARY KEY(code),
 CONSTRAINT Diploma_CK UNIQUE(name));
 
 CREATE TABLE Module(
	code    VARCHAR(4) 	NOT NULL,
    name 	VARCHAR(30) NOT NULL,
    hours	DECIMAL(2)	NOT NULL,
    fee		DECIMAL(4)	NOT NULL,
 CONSTRAINT Module_PK PRIMARY KEY(code),
 CONSTRAINT Hours_CH1 CHECK (hours > 30) );
 
CREATE TABLE Dipmod(
	dip_code    VARCHAR(5) 	NOT NULL,
    mod_code 	VARCHAR(4)  NOT NULL,
 CONSTRAINT Dipmod_FK1 FOREIGN KEY(dip_code) REFERENCES Diploma(code),
 CONSTRAINT Dipmod_FK2 FOREIGN KEY(mod_code) REFERENCES Module(code) );
 
 CREATE TABLE Lecturer(
	emp_id    VARCHAR(4) 	NOT NULL,
    name 	  VARCHAR(25)   NOT NULL,
    dob		  DATE		    NOT NULL,
    gender	  VARCHAR(1)	NOT NULL,
    email	  VARCHAR(35)	NOT NULL,
 CONSTRAINT Lecturer_PK PRIMARY KEY(emp_id),
 CONSTRAINT Lecturer_CK UNIQUE(email),
 CONSTRAINT Gender_CH1 CHECK (gender = 'M' OR gender = 'F') );
 
 CREATE TABLE Specialty(
	emp_id   VARCHAR(4) 	NOT NULL,
    topic	 VARCHAR(35) 	NOT NULL,
 CONSTRAINT Specialty_FK1 FOREIGN KEY(emp_id) REFERENCES Lecturer(emp_id));