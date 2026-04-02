-- When Commands written in .sql file it can read all the commands together

-- How to it through .sql file:
-- Option 1: sqlite3 practice.db < practice.sql
-- Option 2: .read practice.sql
-- Option 3: 

-- Basic SQLite Operations: CREATE, INSERT, SELECT, UPDATE, DELETE, DROP 

--Create table:
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
);

-- INSERT data:
INSERT INTO students (name, marks) VALUES ('John', 86);
INSERT INTO students (name, marks) VALUES ('Ben', 94);
INSERT INTO students (name, marks) VALUES ('Kat', 78);
INSERT INTO students (name, marks) VALUES ('Kevin', 53);
INSERT INTO students (name, marks) VALUES ('Mike', 100);
INSERT INTO students (name, marks) VALUES ('Joe', 41);
INSERT INTO students (name, marks) VALUES ('Dan', 67);

-- SELECT date (display tabel): 
SELECT * FROM students;                              -- Displays entire TABLE
SELECT * FROM students WHERE marks > 70;             -- With condition that marks are more then 70 
SELECT name FROM students;                           -- Only display's the column with only names
SELECT marks FROM students;                          -- Only display's the column with only marks

-- UPDATE data: 
UPDATE students
SET marks = 100
where name = "Ben";
SELECT * FROM students;

-- DELETE date:
DELETE FROM students 
Where name = 'Mike';

-- DROP table:
-- DROP TABLE students;                             -- This will reset the table to blank.  



-- DDL: Data Definition Language 
-- DML: Date Manipulation Language