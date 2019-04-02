import sqlite3

class InsertStudent(object):

    def insert_data(self, tablename, values):
        if self.cursor:
            self.cursor.execute("insert into % (id, describe) values (%)" % (tablename, values))
        self.conn.commit();

    def connect_database(self):
        self.conn = sqlite3.connect('/Users/xiafeng/studentStatus.db')
        self.cursor = self.conn.cursor()

