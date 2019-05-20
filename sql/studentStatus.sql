--
-- 由SQLiteStudio v3.2.1 产生的文件 周一 5月 20 17:28:04 2019
--
-- 文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：class
DROP TABLE IF EXISTS class;
CREATE TABLE class (id INTEGER PRIMARY KEY, describe VARCHAR NOT NULL, professId INTEGER NOT NULL);

-- 表：classTime
DROP TABLE IF EXISTS classTime;
CREATE TABLE classTime (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR, week INTEGER);

-- 表：course
DROP TABLE IF EXISTS course;
CREATE TABLE course (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR);

-- 表：courseTable
DROP TABLE IF EXISTS courseTable;
CREATE TABLE courseTable (id INTEGER PRIMARY KEY AUTOINCREMENT, classTimeId INTEGER, userId INTEGER, courseId INTEGER, classId INTEGER, semesterId INTEGER);

-- 表：departments
DROP TABLE IF EXISTS departments;
CREATE TABLE departments (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR UNIQUE NOT NULL);

-- 表：grade
DROP TABLE IF EXISTS grade;
CREATE TABLE grade (id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER NOT NULL, courseId INTEGER, grade DOUBLE, semesterId INTEGER);

-- 表：professional
DROP TABLE IF EXISTS professional;
CREATE TABLE professional (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR, departId INTEGER);

-- 表：semester
DROP TABLE IF EXISTS semester;
CREATE TABLE semester (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR);

-- 表：user
DROP TABLE IF EXISTS user;
CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER, name VARCHAR (50) NOT NULL, passwd VARCHAR (10) NOT NULL, formerName VARCHAR, idNo VARCHAR, typeId INTEGER NOT NULL, sex CHAR, age INT, classId INTEGER, birthday DATE, national VARCHAR, nativePlace VARCHAR, politicalLandscape VARCHAR, admissionDate DATE, mail VARCHAR, schoolYear VARCHAR, memo VARCHAR);

-- 表：userType
DROP TABLE IF EXISTS userType;
CREATE TABLE userType (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR (50) NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
