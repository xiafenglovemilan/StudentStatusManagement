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

    def select_user_info(self):
        sql = 'select name, typeId, college, sex, age, major, class, birthday ' \
                'from user where name = "%s" ' % self.__params
        print(sql)
        result = self.__cursor.execute(sql)
        user_info = {}
        for row in result:
            user_info['name'] = row[0]
            user_info['type'] = row[1]
            user_info['college'] = row[2]
            user_info['sex'] = row[3]
            user_info['age'] = row[4]
            user_info['major'] = row[5]
            user_info['class'] = row[6]
            user_info['birthday'] = row[7]
        return user_info
