import sqlite3

from src import config

class DeleteData(object):
    def __init__(self, params = None):
        self.__params = params
        self.__conn = sqlite3.connect(config.db_path)
        self.__cursor = self.__conn.cursor()

    def __del__(self):
        self.__conn.commit()
        self.__conn.close()

    def delete_class(self):
        sql = 'delete from class where id = "{0}"'.format(self.__params['id'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def delete_professional(self):
        sql = 'delete from professional where id = "{0}"'.format(self.__params['id'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def delete_departments(self):
        sql = 'delete from departments where id = "{0}"'.format(self.__params['id'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False

    def delete_user_info(self):
        sql = 'delete from user where userId = "{0}"'.format(self.__params['userId'])
        result = self.__cursor.execute(sql)
        if result.rowcount > 0:
            return True
        else:
            return False
