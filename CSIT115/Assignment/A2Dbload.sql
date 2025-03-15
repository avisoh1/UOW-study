-- CSIT115 Assignment 2
--   Sample records

DELETE FROM Enrolment;
DELETE FROM OfferedCourse;
DELETE FROM Course;
DELETE FROM Qualification;
DELETE FROM Trainer;
DELETE FROM Trainee;

-- Trainer
INSERT INTO Trainer VALUES ('T001', 'Ding Dong', '1980-10-20', 8);
INSERT INTO Trainer VALUES ('T002', 'Fong Ping', '1983-11-20', 7);
INSERT INTO Trainer VALUES ('T003', 'Heng Hoon', '1983-05-15', 6);
INSERT INTO Trainer VALUES ('T004', 'Heng Yong', '1983-11-20', 6);
INSERT INTO Trainer VALUES ('T005', 'Jing Ling', '1986-11-20', 4);
INSERT INTO Trainer VALUES ('T006', 'Jing Hong', '1991-11-20', 4);
INSERT INTO Trainer VALUES ('T007', 'Ling Teck', '1995-11-20', 3);
INSERT INTO Trainer VALUES ('T008', 'Liew Ming', '1998-11-20', 3);
INSERT INTO Trainer VALUES ('T009', 'Mah Cheng', '1999-11-20', 2);
INSERT INTO Trainer VALUES ('T010', 'Mok Liang', '2000-11-20', 1);
INSERT INTO Trainer VALUES ('T021', 'Loo Kwang', '1993-05-20', 3);
INSERT INTO Trainer VALUES ('T022', 'Long Tian', '1993-08-20', 3);
INSERT INTO Trainer VALUES ('T031', 'Ming Yuan', '1995-03-28', 3);
INSERT INTO Trainer VALUES ('T032', 'Ning Ning', '1995-09-28', 5);

-- Qualification
INSERT INTO Qualification VALUES ('T001', 'Bsc Science');
INSERT INTO Qualification VALUES ('T001', 'Oracle DBA');
INSERT INTO Qualification VALUES ('T002', 'Bsc Science');
INSERT INTO Qualification VALUES ('T003', 'Bsc Science');
INSERT INTO Qualification VALUES ('T004', 'Bsc Engineering');
INSERT INTO Qualification VALUES ('T005', 'Bsc Engineering');
INSERT INTO Qualification VALUES ('T006', 'Bsc Business');
INSERT INTO Qualification VALUES ('T007', 'Bsc Business');
INSERT INTO Qualification VALUES ('T008', 'Bsc Business');
INSERT INTO Qualification VALUES ('T009', 'Bsc IT');
INSERT INTO Qualification VALUES ('T009', 'Java Developer');
INSERT INTO Qualification VALUES ('T010', 'Java Architect');
INSERT INTO Qualification VALUES ('T021', 'Bsc Arts');
INSERT INTO Qualification VALUES ('T022', 'Bsc Arts');
INSERT INTO Qualification VALUES ('T031', 'Bsc Arts');
INSERT INTO Qualification VALUES ('T032', 'Bsc Arts');
-- Trainee
INSERT INTO Trainee VALUES ('R001', 'Low Cindy', '1980-03-15', 20, 'Finance');
INSERT INTO Trainee VALUES ('R002', 'Lim Henry', '1982-03-23', 17, 'Accounting');
INSERT INTO Trainee VALUES ('R003', 'Lee Lucas', '1983-04-12', 16, 'Engineering');
INSERT INTO Trainee VALUES ('R004', 'Lin Ringo', '1983-04-12', 16, 'Engineering');
INSERT INTO Trainee VALUES ('R005', 'Mok Clara', '1984-05-09', 14, 'Accounting');
INSERT INTO Trainee VALUES ('R006', 'Han Jinny', '1984-06-04', 14, 'Accounting');
INSERT INTO Trainee VALUES ('R007', 'Tin Eddie', '1984-07-03', 13, 'Finance');
INSERT INTO Trainee VALUES ('R008', 'Koo Bella', '1985-10-19', 12, 'Human Resource');
INSERT INTO Trainee VALUES ('R009', 'Mah Jones', '1985-10-18', 12, 'Human Resource');
INSERT INTO Trainee VALUES ('R010', 'Sim Tonny', '1985-10-15', 13, 'Education');
INSERT INTO Trainee VALUES ('R011', 'Yan Daiyu', '1986-04-15', 10, 'Education');
INSERT INTO Trainee VALUES ('R012', 'Loo Kenya', '1986-04-15', 10, 'Education');
INSERT INTO Trainee VALUES ('R013', 'Woo Robin', '1986-01-10', 11, 'Education');
INSERT INTO Trainee VALUES ('R014', 'Han Nolan', '1986-01-10', 11, 'Healthcare');
INSERT INTO Trainee VALUES ('R015', 'Low Tyler', '1986-01-10', 11, 'Healthcare');
INSERT INTO Trainee VALUES ('R016', 'Dee Helen', '1990-01-11', 12, 'Food and Beverage');
INSERT INTO Trainee VALUES ('R017', 'Foo Mandy', '1991-02-12', 12, 'Food and Beverage');
INSERT INTO Trainee VALUES ('R018', 'Koo David', '1992-03-13', 11, 'Food and Beverage');
INSERT INTO Trainee VALUES ('R019', 'Nee Choon', '1993-04-14', 10, 'Food and Beverage');
INSERT INTO Trainee VALUES ('R020', 'Poh Keong', '1993-05-15', 10, 'Food and Beverage');

INSERT INTO Trainee VALUES ('R021', 'Bee Hanna', '2003-01-27', 0, 'NA');
INSERT INTO Trainee VALUES ('R022', 'Liew Cody', '2003-02-23', 0, 'NA');
INSERT INTO Trainee VALUES ('R023', 'Sim Fiona', '2003-03-09', 0, 'NA');
INSERT INTO Trainee VALUES ('R024', 'Yeo Mindy', '2004-04-03', 0, 'NA');
INSERT INTO Trainee VALUES ('R025', 'Lin Eddie', '2004-05-11', 0, 'NA');
INSERT INTO Trainee VALUES ('R026', 'Fei Larry', '2004-06-12', 0, 'NA');
INSERT INTO Trainee VALUES ('R027', 'Pin Ginny', '2005-07-08', 0, 'NA');
INSERT INTO Trainee VALUES ('R028', 'Tang Ping', '2005-08-12', 0, 'NA');
INSERT INTO Trainee VALUES ('R029', 'Tong Ling', '2005-09-22', 0, 'NA');
INSERT INTO Trainee VALUES ('R030', 'Song Ming', '2005-10-13', 0, 'NA');
INSERT INTO Trainee VALUES ('R031', 'Sing Long', '2006-07-13', 0, 'NA');
INSERT INTO Trainee VALUES ('R032', 'Sing Xing', '2006-08-23', 0, 'NA');
INSERT INTO Trainee VALUES ('R033', 'Wang Ying', '2006-01-21', 0, 'NA');
INSERT INTO Trainee VALUES ('R034', 'Kong Ming', '2006-01-03', 0, 'NA');
INSERT INTO Trainee VALUES ('R035', 'New Huang', '2007-02-23', 0, 'NA');
INSERT INTO Trainee VALUES ('R036', 'Song Ming', '2007-03-19', 0, 'NA');
INSERT INTO Trainee VALUES ('R037', 'Ding Hong', '2007-04-19', 0, 'NA');
INSERT INTO Trainee VALUES ('R038', 'Gong Ting', '2007-04-19', 0, 'NA');
INSERT INTO Trainee VALUES ('R039', 'Wang Ping', '2007-02-19', 0, 'NA');
INSERT INTO Trainee VALUES ('R040', 'Xing Ying', '2007-03-19', 0, 'NA');

-- Course
INSERT INTO Course VALUES ('C001', 'IT', 'Internet Architecture', 1);
INSERT INTO Course VALUES ('C002', 'IT', 'Ecommerce Architecture', 2);
INSERT INTO Course VALUES ('C003', 'IT', 'Programming', 3);
  -- Business
INSERT INTO Course VALUES ('C011', 'Business', 'Shorthand Writing', 1);
INSERT INTO Course VALUES ('C012', 'Business', 'Accounting', 2);
  -- Language
INSERT INTO Course VALUES ('C021', 'Language', 'Japanese', 1);
INSERT INTO Course VALUES ('C022', 'Language', 'Korean 1', 1);
INSERT INTO Course VALUES ('C023', 'Language', 'Korean 2', 2);
  -- Dessert
INSERT INTO Course VALUES ('C031', 'Dessert', 'Cupcakes', 1);
INSERT INTO Course VALUES ('C032', 'Dessert', 'Brownies', 2);
INSERT INTO Course VALUES ('C033', 'Dessert', 'Puddings', 3);
-- ---------------------------------------------------------
-- OfferedCourse
-- ---------------------------------------------------------
  -- IT
INSERT INTO OfferedCourse VALUES ('C001', '2022-01-17', '2022-01-17', 1, 'T001');
INSERT INTO OfferedCourse VALUES ('C002', '2022-03-26', '2022-03-26', 1, 'T001');
INSERT INTO OfferedCourse VALUES ('C001', '2022-05-27', '2022-05-27', 1, 'T001');
INSERT INTO OfferedCourse VALUES ('C001', '2023-01-28', '2023-01-28', 1, 'T002');
INSERT INTO OfferedCourse VALUES ('C002', '2023-05-23', '2023-05-23', 1, 'T002');
  -- Business
INSERT INTO OfferedCourse VALUES ('C011', '2022-01-03', '2022-01-03', 1, 'T006');
INSERT INTO OfferedCourse VALUES ('C011', '2022-05-03', '2022-05-03', 1, 'T006');
INSERT INTO OfferedCourse VALUES ('C011', '2022-09-05', '2022-09-05', 1, 'T007');
INSERT INTO OfferedCourse VALUES ('C011', '2022-11-02', '2022-11-02', 1, 'T007');
INSERT INTO OfferedCourse VALUES ('C012', '2023-01-02', '2023-01-03', 2, 'T008');
INSERT INTO OfferedCourse VALUES ('C012', '2023-03-02', '2023-03-03', 2, 'T008');
INSERT INTO OfferedCourse VALUES ('C012', '2023-05-03', '2023-05-04', 2, 'T008');
INSERT INTO OfferedCourse VALUES ('C012', '2023-07-04', '2023-07-05', 2, 'T008');
  -- Language
INSERT INTO OfferedCourse VALUES ('C021', '2022-08-21', '2022-08-23', 3, 'T021');
INSERT INTO OfferedCourse VALUES ('C022', '2022-08-24', '2022-12-26', 3, 'T022');
INSERT INTO OfferedCourse VALUES ('C023', '2022-08-27', '2022-08-29', 3, 'T022');

INSERT INTO OfferedCourse VALUES ('C021', '2023-04-21', '2023-04-23', 3, 'T021');
INSERT INTO OfferedCourse VALUES ('C022', '2023-04-24', '2023-04-26', 3, 'T022');
INSERT INTO OfferedCourse VALUES ('C023', '2023-04-27', '2023-04-29', 3, 'T022');
  -- Dessert
INSERT INTO OfferedCourse VALUES ('C031', '2022-02-14', '2022-02-14', 1, 'T031');
INSERT INTO OfferedCourse VALUES ('C031', '2022-04-14', '2022-04-14', 1, 'T031');
INSERT INTO OfferedCourse VALUES ('C031', '2022-06-14', '2022-06-14', 1, 'T031');
INSERT INTO OfferedCourse VALUES ('C031', '2022-08-14', '2023-08-14', 1, 'T031');
INSERT INTO OfferedCourse VALUES ('C032', '2023-02-15', '2023-02-15', 1, 'T032');
INSERT INTO OfferedCourse VALUES ('C032', '2023-04-15', '2023-04-15', 1, 'T032');
INSERT INTO OfferedCourse VALUES ('C032', '2023-06-15', '2023-06-15', 1, 'T032');
INSERT INTO OfferedCourse VALUES ('C032', '2023-08-15', '2023-08-15', 1, 'T032');
-- ------------------------------------------------------------------------------
-- Enrolment
-- ------------------------------------------------------------------------------
  -- IT
      -- C001
INSERT INTO Enrolment VALUES ('E001', 'R011', 'C001', '2022-01-17', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E002', 'R012', 'C001', '2022-01-17', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E003', 'R013', 'C001', '2022-01-17', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E004', 'R014', 'C001', '2022-01-17', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E005', 'R015', 'C001', '2022-01-17', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E006', 'R031', 'C001', '2022-01-17', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E007', 'R032', 'C001', '2022-01-17', 'Self-sponsored', 'Completed');
      -- C001
INSERT INTO Enrolment VALUES ('E011', 'R001', 'C001', '2022-05-27', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E012', 'R002', 'C001', '2022-05-27', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E013', 'R003', 'C001', '2022-05-27', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E014', 'R004', 'C001', '2022-05-27', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E015', 'R005', 'C001', '2022-05-27', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E016', 'R035', 'C001', '2022-05-27', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E017', 'R036', 'C001', '2022-05-27', 'Self-sponsored', 'Good');
      -- C001
INSERT INTO Enrolment VALUES ('E021', 'R021', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E022', 'R022', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E023', 'R023', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E024', 'R024', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E025', 'R025', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E026', 'R026', 'C001', '2023-01-28', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E027', 'R018', 'C001', '2023-01-28', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E028', 'R019', 'C001', '2023-01-28', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E029', 'R020', 'C001', '2023-01-28', 'Sponsored', 'Completed');
      -- C002
INSERT INTO Enrolment VALUES ('E031', 'R011', 'C002', '2022-03-26', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E032', 'R012', 'C002', '2022-03-26', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E033', 'R013', 'C002', '2022-03-26', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E034', 'R021', 'C002', '2022-03-26', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E035', 'R022', 'C002', '2022-03-26', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E036', 'R023', 'C002', '2022-03-26', 'Sponsored', 'Completed');
      -- C002
INSERT INTO Enrolment VALUES ('E051', 'R033', 'C002', '2023-05-23', 'Free', 'Completed');
INSERT INTO Enrolment VALUES ('E052', 'R034', 'C002', '2023-05-23', 'Free', 'Completed');
INSERT INTO Enrolment VALUES ('E053', 'R035', 'C002', '2023-05-23', 'Free', 'Completed');
INSERT INTO Enrolment VALUES ('E054', 'R036', 'C002', '2023-05-23', 'Free', 'Completed');
INSERT INTO Enrolment VALUES ('E055', 'R037', 'C002', '2023-05-23', 'Free', 'Completed');
      -- Business
INSERT INTO Enrolment VALUES ('E201', 'R001', 'C011', '2022-01-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E202', 'R002', 'C011', '2022-01-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E203', 'R003', 'C011', '2022-01-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E204', 'R004', 'C011', '2022-01-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E205', 'R005', 'C011', '2022-01-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E206', 'R006', 'C011', '2022-01-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E207', 'R007', 'C011', '2022-01-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E208', 'R008', 'C011', '2022-01-03', 'Self-sponsored', 'Good');
      -- C011
INSERT INTO Enrolment VALUES ('E211', 'R011', 'C011', '2022-05-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E212', 'R012', 'C011', '2022-05-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E213', 'R013', 'C011', '2022-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E214', 'R014', 'C011', '2022-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E215', 'R015', 'C011', '2022-05-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E216', 'R016', 'C011', '2022-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E217', 'R017', 'C011', '2022-05-03', 'Self-sponsored', 'Good');
      -- C011
INSERT INTO Enrolment VALUES ('E221', 'R031', 'C011', '2022-09-05', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E222', 'R032', 'C011', '2022-09-05', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E223', 'R033', 'C011', '2022-09-05', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E224', 'R034', 'C011', '2022-09-05', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E225', 'R035', 'C011', '2022-09-05', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E226', 'R036', 'C011', '2022-09-05', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E227', 'R037', 'C011', '2022-09-05', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E228', 'R038', 'C011', '2022-09-05', 'Self-sponsored', 'Completed');
      -- C011
INSERT INTO Enrolment VALUES ('E231', 'R021', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E232', 'R022', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E233', 'R023', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E234', 'R024', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E235', 'R025', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E236', 'R026', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E237', 'R027', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E238', 'R028', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E239', 'R029', 'C011', '2022-11-02', 'Self-sponsored', 'Completed');
      -- C012
INSERT INTO Enrolment VALUES ('E241', 'R011', 'C012', '2023-03-02', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E242', 'R012', 'C012', '2023-03-02', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E243', 'R013', 'C012', '2023-03-02', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E244', 'R014', 'C012', '2023-03-02', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E245', 'R015', 'C012', '2023-03-02', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E246', 'R016', 'C012', '2023-03-02', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E247', 'R017', 'C012', '2023-03-02', 'Sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E248', 'R018', 'C012', '2023-03-02', 'Sponsored', 'Good');
      -- C012
INSERT INTO Enrolment VALUES ('E251', 'R031', 'C012', '2023-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E252', 'R032', 'C012', '2023-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E253', 'R033', 'C012', '2023-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E254', 'R034', 'C012', '2023-05-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E255', 'R035', 'C012', '2023-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E256', 'R036', 'C012', '2023-05-03', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E257', 'R037', 'C012', '2023-05-03', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E258', 'R038', 'C012', '2023-05-03', 'Self-sponsored', 'Good');
      -- C012
INSERT INTO Enrolment VALUES ('E261', 'R008', 'C012', '2023-07-04', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E262', 'R009', 'C012', '2023-07-04', 'Sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E263', 'R021', 'C012', '2023-07-04', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E264', 'R022', 'C012', '2023-07-04', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E265', 'R023', 'C012', '2023-07-04', 'Self-sponsored', 'Completed');

  -- Language
INSERT INTO Enrolment VALUES ('E401', 'R001', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E402', 'R002', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E403', 'R003', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E404', 'R004', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E405', 'R005', 'C021', '2022-08-21', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E406', 'R006', 'C021', '2022-08-21', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E407', 'R007', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E408', 'R008', 'C021', '2022-08-21', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E409', 'R009', 'C021', '2022-08-21', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E410', 'R010', 'C021', '2022-08-21', 'Self-sponsored', 'Good');

INSERT INTO Enrolment VALUES ('E421', 'R011', 'C022', '2022-08-24', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E422', 'R012', 'C022', '2022-08-24', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E423', 'R013', 'C022', '2022-08-24', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E424', 'R014', 'C022', '2022-08-24', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E425', 'R015', 'C022', '2022-08-24', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E426', 'R016', 'C022', '2022-08-24', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E427', 'R017', 'C022', '2022-08-24', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E428', 'R018', 'C022', '2022-08-24', 'Self-sponsored', 'Completed');

INSERT INTO Enrolment VALUES ('E431', 'R011', 'C023', '2022-08-27', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E432', 'R012', 'C023', '2022-08-27', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E433', 'R013', 'C023', '2022-08-27', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E434', 'R014', 'C023', '2022-08-27', 'Self-sponsored', 'Good');
INSERT INTO Enrolment VALUES ('E435', 'R015', 'C023', '2022-08-27', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E436', 'R016', 'C023', '2022-08-27', 'Self-sponsored', 'Completed');

  -- Dessert
INSERT INTO Enrolment VALUES ('E601', 'R001', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E602', 'R005', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E603', 'R006', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E604', 'R008', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E605', 'R009', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E606', 'R012', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E607', 'R021', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E608', 'R022', 'C031', '2022-02-14', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E609', 'R023', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E610', 'R024', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E611', 'R025', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E612', 'R026', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E613', 'R027', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E614', 'R028', 'C031', '2022-04-14', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E615', 'R029', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E616', 'R030', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E617', 'R031', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E618', 'R032', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E619', 'R033', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E620', 'R034', 'C031', '2022-06-14', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E621', 'R035', 'C031', '2022-08-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E622', 'R016', 'C031', '2022-08-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E623', 'R017', 'C031', '2022-08-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E624', 'R018', 'C031', '2022-08-14', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E625', 'R019', 'C031', '2022-08-14', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E631', 'R001', 'C032', '2023-02-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E632', 'R005', 'C032', '2023-02-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E633', 'R006', 'C032', '2023-02-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E634', 'R008', 'C032', '2023-02-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E635', 'R009', 'C032', '2023-02-15', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E636', 'R005', 'C032', '2023-04-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E637', 'R016', 'C032', '2023-04-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E638', 'R017', 'C032', '2023-04-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E639', 'R018', 'C032', '2023-04-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E640', 'R019', 'C032', '2023-04-15', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E641', 'R021', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E642', 'R022', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E643', 'R023', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E644', 'R024', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E645', 'R025', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E646', 'R026', 'C032', '2023-06-15', 'Self-sponsored', 'Completed');
    --
INSERT INTO Enrolment VALUES ('E647', 'R027', 'C032', '2023-08-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E648', 'R028', 'C032', '2023-08-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E649', 'R029', 'C032', '2023-08-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E650', 'R030', 'C032', '2023-08-15', 'Self-sponsored', 'Completed');
INSERT INTO Enrolment VALUES ('E651', 'R031', 'C032', '2023-08-15', 'Self-sponsored', 'Completed');

-- -- Check tables
-- SELECT * FROM Trainer;
-- SELECT * FROM Qualification;
-- SELECT * FROM Trainee;
-- SELECT * FROM Course;
-- SELECT * FROM Enrolment;
-- SELECT * FROM enrolment;

