/*Avis Oh Xin Wan UOW ID:8465678
  Assignment 2 Task 1 Create Tables*/
CREATE TABLE Diploma(
	code    VARCHAR(4) 	NOT NULL,
    name 	VARCHAR(20) NOT NULL,
 CONSTRAINT Diploma_PK PRIMARY KEY(code));
 
 CREATE TABLE Module(
	code    VARCHAR(4) 	NOT NULL,
    name 	VARCHAR(30) NOT NULL,
    hours	DECIMAL(2)	NOT NULL,
    fee		DECIMAL(4)	NULL,
 CONSTRAINT Module_PK PRIMARY KEY(code));
 
CREATE TABLE Dipmod(
	dip_code    VARCHAR(5) 	NOT NULL,
    mod_code 	VARCHAR(4)  NOT NULL,
 CONSTRAINT Dipmod_FK1 FOREIGN KEY(dip_code) REFERENCES DIPLOMA(code),
 CONSTRAINT Dipmod_FK2 FOREIGN KEY(mod_code) REFERENCES MODULE(code) );
 
 CREATE TABLE Lecturer(
	emp_id    VARCHAR(4) 	NOT NULL,
    name 	  VARCHAR(25)   NOT NULL,
    dob		  DATE		    NULL,
    gender	  VARCHAR(1)	NOT NULL,
    email	  VARCHAR(35)	NOT NULL,
 CONSTRAINT Lecturer_PK PRIMARY KEY(emp_id));
 
 CREATE TABLE Specialty(
	emp_id   VARCHAR(4) 	NOT NULL,
    topic	 VARCHAR(35) 	NOT NULL,
 CONSTRAINT Specialty_FK1 FOREIGN KEY(emp_id) REFERENCES LECTURER(emp_id));