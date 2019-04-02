import sqlite3

from src import config

class SelectData(object):
    def __init__(self, params):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.close()

    def select_password(self):
        result = self.__cursor.execute('select * from user where name = "%s"' % self.__params)
        pass_wd = ""
        for row in result:
            pass_wd = row[9]
        return pass_wd
