-- CSIT115 Assignemnt 2
--   Create tables

DROP TABLE IF EXISTS Enrolment;
DROP TABLE IF EXISTS OfferedCourse;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Qualification;
DROP TABLE IF EXISTS Trainer;
DROP TABLE IF EXISTS Trainee;

CREATE TABLE Trainer
(
    empId      CHAR(4),
    name       VARCHAR(30) NOT NULL,
    dob        DATE        NOT NULL,
    trainYears INT         DEFAULT 1,
    CONSTRAINT TrainerPK PRIMARY KEY (empId),
    CONSTRAINT dobCHK    CHECK (dob < SYSDATE()),
    CONSTRAINT yearCHK   CHECK (trainYears >= 1)
);
CREATE TABLE Qualification
(
    trainer     CHAR(4),
    certificate VARCHAR(25),
    CONSTRAINT QualificationPK PRIMARY KEY (trainer, certificate),
    CONSTRAINT QualificationFK FOREIGN KEY (trainer) REFERENCES Trainer (empId)
                               ON DELETE CASCADE
                               ON UPDATE CASCADE
);
CREATE TABLE Trainee
(
    refId      CHAR(4),
    name       VARCHAR(30) NOT NULL,
    dob        DATE        NOT NULL,
    workYears  INT         NOT NULL DEFAULT 0,
    workType   VARCHAR(30),
    CONSTRAINT TraineePK PRIMARY KEY (refId),
    CONSTRAINT TdobCHK   CHECK (dob < SYSDATE()),
    CONSTRAINT TyearCHK  CHECK (workYears >= 0)
);
CREATE TABLE Course
(
    code     CHAR(4),
    category VARCHAR(20) NOT NULL,
    name     VARCHAR(30) NOT NULL,
    level    INT         DEFAULT 1,
    CONSTRAINT CoursePK PRIMARY KEY (code),
    CONSTRAINT levelCHK CHECK (level >= 1)
);
CREATE TABLE OfferedCourse
(
    code      CHAR(4),
    startDate DATE,
    endDate   DATE    NOT NULL,
    duration  INT     DEFAULT 1,
    trainer   CHAR(4) NOT NULL,
    CONSTRAINT OfferedCoursePK PRIMARY KEY (code, startDate),
    CONSTRAINT OfferedFK FOREIGN KEY (trainer) REFERENCES Trainer (empId) ,
    CONSTRAINT durationCHK CHECK (duration >= 1)
);
CREATE TABLE Enrolment
(
    eRef    CHAR(4),
	trainee CHAR(4)     NOT NULL,
    oCourse CHAR(4)     NOT NULL,
    oDate   DATE        NOT NULL,
    eType   VARCHAR(20) NOT NULL DEFAULT 'Self-sponsored',
    grade   VARCHAR(15),
    CONSTRAINT EnrolmentPK PRIMARY KEY (eRef),
    CONSTRAINT EnrolmentFK1 FOREIGN KEY (trainee) REFERENCES Trainee (refId)
                                                  ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT EnrolmentFK2 FOREIGN KEY (oCourse, oDate) REFERENCES OfferedCourse (code, startDate),
    CONSTRAINT eTypeCHK CHECK (eType IN ('Self-sponsored', 'Sponsored', 'Free')),
    CONSTRAINT gradeCHK CHECK (grade IN ('Completed', 'Incomplete', 'Good'))
);

-- Check tables
-- SELECT * FROM Trainer;
-- SELECT * FROM Qualification;
-- SELECT * FROM Trainee;
-- SELECT * FROM Course;
-- SELECT * FROM OfferedCourse;
-- SELECT * FROM enrolment;
