--
-- 由SQLiteStudio v3.2.1 产生的文件 周一 3月 25 14:46:04 2019
--
-- 文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：grade
DROP TABLE IF EXISTS grade;
CREATE TABLE grade (id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER NOT NULL, chinese DOUBLE, english DOUBLE, math DOUBLE, physics DOUBLE, chemistry DOUBLE, biology DOUBLE);

-- 表：permission
DROP TABLE IF EXISTS permission;
CREATE TABLE permission (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR (50) NOT NULL);

-- 表：user
DROP TABLE IF EXISTS user;
CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR (50), typeId INTEGER NOT NULL, college VARCHAR (50), sex BOOLEAN, age INT, major VARCHAR (50), class VARCHAR (50), birthday DATE);

-- 表：userType
DROP TABLE IF EXISTS userType;
CREATE TABLE userType (id INTEGER PRIMARY KEY AUTOINCREMENT, describe VARCHAR (50) NOT NULL, permission_id INT NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
