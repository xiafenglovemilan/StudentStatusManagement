import sqlite3

conn = sqlite3.connect('/Users/xiafeng/studentStatus.db')

cursor = conn.cursor()

cursor.execute("insert into permission (id, describe) values (1, '超级管理员')")

conn.commit();

conn.close();

